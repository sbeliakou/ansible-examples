#!/bin/bash

source $1

printf '{"failed": false, "changed": false, "phrase": "%s"}' "$phrase"

exit 0
