#!/usr/bin/python
# -*- coding: utf-8 -*-
#

DOCUMENTATION = '''
---
Simple Ansible Module

- simple_module:
    msg: Hello from module
'''

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

