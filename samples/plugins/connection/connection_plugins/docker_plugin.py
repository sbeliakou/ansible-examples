from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

import docker
import time
from io import BytesIO
import tarfile
import os

import ansible.constants as C
from ansible.errors import AnsibleError, AnsibleFileNotFound
from ansible.module_utils._text import to_bytes, to_native
from ansible.plugins.connection import ConnectionBase, BUFSIZE

class Connection(ConnectionBase):

    ''' Specify connection type for Ansible'''
    transport = 'docker'

    def __init__(self, play_context, new_stdin, *args, **kwargs):
        super(Connection, self).__init__(play_context, new_stdin, *args, **kwargs)
        self.client = docker.APIClient(base_url='unix://var/run/docker.sock')
        self.exec_command("apk add --update python python-dev py-pip")

    def create_archive(self, artifact_file, name):
        '''Create archive to use in put_file method'''
        pw_tarstream = BytesIO()
        pw_tar = tarfile.TarFile(fileobj=pw_tarstream, mode='w')
        with open(artifact_file, 'r') as file_data:
            a = file_data.read()
            tarinfo = tarfile.TarInfo(name=name)
            tarinfo.size = len(a)
            tarinfo.mtime = time.time()
            pw_tar.addfile(tarinfo, BytesIO(a))
        pw_tarstream.seek(0)
        return pw_tarstream

    def _connect(self, port=None):
        super(Connection, self)._connect()
        if not self._connected:
            self._connected = True

    def exec_command(self, cmd, in_data=None, sudoable=False):
        ''' Run a command on the docker host '''
        super(Connection, self).exec_command(cmd, in_data=in_data, sudoable=sudoable)
        command = self.client.exec_create(self._play_context.remote_addr, '%s' % (cmd))
        try:
            exec_command = self.client.exec_start(command)
        except:
            return (1, exec_command, exec_command)
        return (0, exec_command, exec_command)

    def put_file(self, in_path, out_path):
        ''' Transfer a file from local to docker container '''
        super(Connection, self).put_file(in_path, out_path)
        with self.create_archive(in_path, out_path) as archive:
            self.client.put_archive(container=self._play_context.remote_addr, path='/', data=archive)    
        
    def fetch_file(self, in_path, out_path):
         
        """ Fetch a file from container to local. """
        super(Connection, self).fetch_file(in_path, out_path)
        stream,stat = self.client.get_archive(container=self._play_context.remote_addr, path=in_path)
        raw_data = stream.read()
        with open("%s-tar" % out_path, 'w') as file:
            file.write(raw_data)
        tar = tarfile.open("%s-tar" % out_path)
        tar.extractall(path=out_path.rsplit('/', 1)[0])
        tar.close()
        os.remove("%s-tar" % out_path)
        

    def close(self):
        """ Terminate the connection. Nothing to do for Docker"""
        super(Connection, self).close()
        self._connected = False
