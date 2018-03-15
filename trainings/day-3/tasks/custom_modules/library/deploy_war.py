#!/usr/bin/python
# -*- coding: utf-8 -*-
#

DOCUMENTATION = '''
---
'''

from ansible.module_utils.basic import *
import subprocess
import requests
import os

def main():

  # http://192.168.56.23:8080/manager/text/deploy?path=/samplewar&update=true
  module = AnsibleModule(
    argument_spec = dict(
      url       = dict(required=True, type='str'),
      username  = dict(required=True, type='str'),
      password  = dict(required=True, type='str'),
      context   = dict(required=True, type='str'),
      src       = dict(required=True, type='str')
    )
  )

  result = dict(
      msg='',
      changed=False,
      context='',
      application_url='',
      src=''
  )

  if module.check_mode:
    return result

  url = module.params["url"]
  username = module.params["username"]
  password = module.params["password"]
  context = module.params["context"]
  src = module.params["src"]

  if os.path.isfile(src) == False:
    result['msg'] = 'FAIL - File not found - {}'.format(src)
    module.fail_json(**result)

  mime = subprocess.Popen("/usr/bin/file --mime " + "/home/vitali/ans_ex/ansible-examples/trainings/day-3/sample.war", shell=True, stdout=subprocess.PIPE).communicate()[0].split(' ')[1].replace(';', '')
  if "java-archive" not in mime:
    result['msg'] = 'FAIL - Not a java-archive type - {}'.format(src)
    module.fail_json(**result)
  
  files = {'file': (os.path.basename(src), open(src, 'rb'))}
  deploy_url = "{}/manager/text/deploy?path={}&update=true".format(url, context)

  r = requests.put(url=deploy_url, auth=(username, password), files=files)

  if r.status_code == 200:
    result['msg'] = "OK - Deployed application at context path [{}]".format(context)
    result['changed'] = True
    result['context'] = context
    result['application_url'] = "{}{}".format(url, context)
    result['src'] = src
  else:
    result['msg'] = 'FAIL - Deployment Failed at context path [{}]'.format(context)
    module.fail_json(**result)
  module.exit_json(**result)
  
# include magic from lib/ansible/module_common.py
#<<INCLUDE_ANSIBLE_MODULE_COMMON>>
main()
