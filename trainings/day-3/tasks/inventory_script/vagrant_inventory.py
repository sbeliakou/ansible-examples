#!/usr/bin/env python

import argparse
import os
import vagrant
import json

# Requirements:
# pip install python-vagrant

def main():
    parser = argparse.ArgumentParser(description="Parse list parameter")
    parser.add_argument("--list", default=False, action="store_true" , help="Flag to do list hosts")
    parser.add_argument("--host", default="", action="store" , help="Flag to get host")
    args = parser.parse_args()
    
    stack = vagrant.Vagrant(os.getcwd())
    current = stack.conf()

    if stack.status()[0].state == "running":
        if(args.host):
            if(args.host == current["Host"] ):
                print json.dumps({
                    "ansible_host": current["HostName"],
                    "ansible_port": current["Port"],
                    "ansible_user": current["User"],
                    "ansible_ssh_private_key_file": current["IdentityFile"]
                }, indent=4)
            else:
                print {}

        if(args.list):
            print json.dumps({
                "vagrant" : {
                    "hosts" : [
                        current["Host"]
                    ],
                    "vars": {
                        "ansible_user": current["User"],
                        "ansible_ssh_private_key_file": current["IdentityFile"]
                    }
                },
                "_meta": {
                    "hostvars": {
                        current["Host"]: {
                            "ansible_host": current["HostName"],
                            "ansible_port": current["Port"]
                        }
                    }
                }
            }, indent=4)
    else:
        print {}

if __name__ == '__main__':  
    main()