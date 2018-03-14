#!/usr/bin/python

"""
Ansible Vagrant - VirtualBox module. Usage:

Dependency: 
- pip install pyvbox python-vagrant

- name: create host 
  vagrant_ans:
    path: /home/student/cm/ansible/day-3
    state: started
  register: result

path: required - True. Description: Path to Vagranfile. Can be either directory path, containing Vagrantfile or full path(/home/student/cm/ansible/day-3/Vagranfile i.e.)
state: required - True. Description: Set desired vm state. Options are: started, stopped, destroyed.
"""

from ansible.module_utils.basic import *
import virtualbox
import vagrant
import os

class VagrantVmController:
    def __init__(self, path):
        if os.path.isfile(path) == True:
            self.path = path[:-11]
        else:
            self.path = path
        self.vm = vagrant.Vagrant(self.path)

    def set_state(self, desired_state):
        choice_map = {
            "started": self.vm_set_started,
            "stopped": self.vm_set_stopped,
            "destroyed": self.vm_set_destroyed
        }
        try:
            #get link to the necessary function and call it.
            result = choice_map.get(desired_state)()
        except(OSError, IOError, ValueError):
            return (False, {'error:': 'error setting state to vm'})
        return result

    #get status from Vagrant library.
    def get_vagrant_running_status(self):
        return self.vm.status()[0][1]

    #get machine id - needed in vbox library
    def get_vm_id(self):
        with open(self.vm.keyfile()[:-11] + "id", 'r') as id_file:
            id = id_file.readline()
        return id
    #start virtual machine
    def vm_set_started(self):
        has_changed = False
        if self.get_vagrant_running_status() != 'running':
            try:
                self.vm.up()
            except(OSError, IOError, ValueError):
                return (False,{'error:': 'error creating vm'})
            has_changed = True

        a = self.vm.conf()
        del a['StrictHostKeyChecking'], a['UserKnownHostsFile'], a['LogLevel'], a['IdentitiesOnly'], a['PasswordAuthentication']
        a.update({'state': 'started'})
        #Get virtual machine characteristics from Vbox library, by machine id. Works only for running instances. 
        vbox_vm = virtualbox.VirtualBox().find_machine(self.get_vm_id())
        #Get os name and memory size. Almost any parameter can be extracted from this structure, if necessary.
        a.update({'os_name': vbox_vm.os_type_id, 'RAM_size': vbox_vm.memory_size})
        return (has_changed, a)

    #stop virtual machine
    def vm_set_stopped(self):
        has_changed = False
        if self.get_vagrant_running_status() == 'running':
            try:
                self.vm.halt()
            except(OSError, IOError, ValueError):
                return (False,{'error:': 'error stopping vm'})
            has_changed = True
        meta = self.vm.status()
        return (has_changed, meta)

    #destroy virtual machine
    def vm_set_destroyed(self):
        has_changed = False
        if self.get_vagrant_running_status() != 'not_created':
            try:
                self.vm.destroy()
            except(OSError, IOError, ValueError):
                return (False,{'error:': 'error destroying vm'})
            has_changed = True
        meta = self.vm.status()
        return (has_changed, meta)



def main():
    #define module params
    fields = {
        "path": {"required": True, "type": "str"},
        "state": {
            "choices": ["started", "stopped", 'destroyed'],
            "type": 'str'
        },
    }
    module = AnsibleModule(argument_spec=fields)
    #initialize virtual machine object
    vagrant_vm = VagrantVmController(module.params['path'])
    #set vm state and return result
    has_changed, result = vagrant_vm.set_state(module.params['state'])
    module.exit_json(changed=has_changed, meta=result)

if __name__ == '__main__':  
    main()