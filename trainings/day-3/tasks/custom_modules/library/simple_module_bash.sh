#!/bin/bash

# Module Argumets are passed to Module in a file
# ./module_name file_with_argumets

[ -f "$1" ] && source $1

cat << EOF
{
	"changed": true,
	"msg": "${msg}"
}
EOF






















