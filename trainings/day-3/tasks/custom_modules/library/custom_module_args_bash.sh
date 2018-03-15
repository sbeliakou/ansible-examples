#!/bin/bash

# ---
# Simple Ansible Module with Args
# 
# - simple_module_bash:
#     msg: Hello from module
#
# Ansible passes arguments to the module as file
#   ./module_name file_with_argumets

[ -f "$1" ] && source $1

if [ -z "${msg}" ]; then
    printf '{"failed": true, "msg": "Missing required arguments: msg"}'
    exit 1
fi

cat << EOF
{
    "changed": true,
    "msg": "${msg}"
}
EOF

exit 0




















