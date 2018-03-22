#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

DOCUMENTATION = '''
---
module: deploy_war
version_added: historical
short_description: Deploy WAR file to Tomcat
options:
    url:
        version_added: "1.0"
        description:
            - "Tomcat URL"
        required: true
        default: 'None'
    username:
        version_added: "1.0"
        description:
            - "Username for authentication on Tomcat"
        required: true
        default: None
    password:
        version_added: "1.0"
        description:
            - "Password for authentication on Tomcat"
        required: true
        default: None
    context:
        version_added: "1.0"
        description:
            - "Deployable Context Target"
        required: true
        default: None
    src:
        version_added: "1.0"
        description:
            - "Path to artifact to be deployed"
        required: true
        default: None
requirments:
    - pip install requests
description:
    - This module can be used for Tomcat remote deployment

author:
    - "Siarhei Beliakou"
    - "Vitali Ulantsau"
'''

EXAMPLES = """
# Standalone mode launch.
ansible localhost -c local -m deploy_war -a "url=http://192.168.56.100:8080 username=admin password=secret context=/helloworld src=/tmp/hello.war"

# Running module as task inside a playbook. 
# Ensure that vm(s) specified in provided Vagrantfile is running
- name: create host 
  deploy_war:
    url: http://192.168.56.100:8080
    username: admin
    password: secret
    context: /helloworld
    src: /tmp/hello.war
"""

from ansible.module_utils.basic import *
import subprocess
import requests
import os

def main():

  module = AnsibleModule(
    argument_spec = dict(
      url       = dict(required=True, type='str'),
      username  = dict(required=True, type='str'),
      password  = dict(required=True, type='str'),
      context   = dict(required=True, type='str'),
      src       = dict(required=True, type='str')
    )
  )

  url = module.params["url"]
  username = module.params["username"]
  password = module.params["password"]
  context = module.params["context"]
  src = os.path.abspath(module.params["src"])

  result = dict(
      msg='',
      changed=False,
      context=context,
      application_url="{}{}".format(url, context),
      src=src
  )

  if module.check_mode:
    return result

  if os.path.isfile(src) == False:
    result['msg'] = 'FAIL - File not found - {}'.format(src)
    module.fail_json(**result)

  mime = subprocess.Popen("/usr/bin/file --mime " + src, \
    stdout=subprocess.PIPE, \
    shell=True).communicate()[0].split(' ')[1].replace(';', '')

  if "java-archive" not in mime:
    result['msg'] = 'FAIL - Not a java-archive type - {}'.format(src)
    module.fail_json(**result)
  
  files = {'file': (os.path.basename(src), open(src, 'rb'))}
  deploy_url = "{}/manager/text/deploy?path={}&update=true".format(url, context)

  r = requests.put(url=deploy_url, auth=(username, password), files=files)

  if r.status_code == 200:
    result['msg'] = "OK - Deployed application at context path [{}]".format(context)
    result['changed'] = True
  else:
    result['msg'] = 'FAIL - Deployment Failed at context path [{}]'.format(context)
    module.fail_json(**result)
  module.exit_json(**result)
  
# include magic from lib/ansible/module_common.py
#<<INCLUDE_ANSIBLE_MODULE_COMMON>>
main()
