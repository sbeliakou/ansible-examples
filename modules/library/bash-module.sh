#!/bin/bash

source $1

##------Checking input variables---------

if [ -z "$phrase" ]; then
    printf '{"failed": true, "msg": "Missing required arguments: phrase"}'
    exit 1
fi

printf '{"failed": false, "changed": false, "phrase": "%s"}' "$phrase"

exit 0
