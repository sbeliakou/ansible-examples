#!/usr/bin/env python

DOCUMENTATION = '''
---
Simple Ansible Module without Args

- simple_module_python:
    msg: Hello from module
'''

import datetime
import json

date = str(datetime.datetime.now())
print json.dumps({
  "time": date
})


