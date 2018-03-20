#!/usr/bin/env python

DOCUMENTATION = '''
---
module: custom_module_python
version_added: historical
short_description: Simple Ansible Module written on Python

description:
    - This is an example module which returns current date
author:
    - "Siarhei Beliakou"
'''

EXAMPLES = """
# Standalone mode launch.
ansible localhost -c local -m custom_module_python

- custom_module_python:
  
"""

import datetime
import json

date = str(datetime.datetime.now())
print json.dumps({
  "time": date
})


