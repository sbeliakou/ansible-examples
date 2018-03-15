#!/bin/bash

# ---
# Simple Ansible Module without Args
# 
# - simple_module_bash:
#     msg: Hello from module

cat << EOF
{
	"time": "$(date +'%Y-%m-%d %T')"
}
EOF


