#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

DOCUMENTATION = '''
---
module: custom_module_args_python
version_added: historical
short_description: Simple Ansible Module written on Python
options:
  msg: 
    version_added: "1.0"
    description:
        - "Message to be returned by module"
    required: true
    default: 'None'
description:
    - This is an example module which returns custom message
author:
    - "Siarhei Beliakou"
'''

EXAMPLES = """
# Standalone mode launch.
ansible localhost -c local -m custom_module_args_python -a msg='message'

- custom_module_args_python:
    msg: "message"
  
"""

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
