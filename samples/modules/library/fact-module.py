#!/usr/bin/python

import sys
import json
import shlex


args_file = sys.argv[1]
args_data = file(args_file).read()

arguments = shlex.split(args_data)
result = {}
result["ansible_facts"] = {}
for arg in arguments:

    if "=" in arg:

        key, value = arg.split("=")
        result["ansible_facts"][key] = value

result['changed'] = True 
print(json.dumps(result))
