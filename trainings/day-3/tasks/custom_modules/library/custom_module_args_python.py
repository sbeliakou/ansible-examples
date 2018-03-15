#!/usr/bin/python
# -*- coding: utf-8 -*-
#

DOCUMENTATION = '''
---
Simple Ansible Module with Args

- simple_module_args_python:
    msg: Hello from module
'''

from ansible.module_utils.basic import *

def main():
  module = AnsibleModule(
    argument_spec = dict(
      msg       = dict(required=True, type='str')
    )
  )

  msg = module.params["msg"]

  results = {}

  results.update({
    "changed": True,
    "msg": msg
  })

  module.exit_json(**results)
  
# include magic from lib/ansible/module_common.py
#<<INCLUDE_ANSIBLE_MODULE_COMMON>>
main()
