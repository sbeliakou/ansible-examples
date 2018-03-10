# Ansible local facts example

## Documentation:

- [Local facts](http://docs.ansible.com/ansible/playbooks_variables.html#local-facts-facts-d)
- [Setup module](http://docs.ansible.com/ansible/setup_module.html)

## Resources:
- [Demo Playbook](example_local-facts.yml) - *Playbook puts the facts to the `/etc/ansible/facts.d` directory and after that gets the facts*

## Overview:

Setup module is automatically called by playbooks to gather useful variables
about remote hosts that can be used in playbooks.

If a remotely managed system has an `/etc/ansible/facts.d` directory, any files in this directory ending in `.fact`, can be JSON, INI, or executable files returning JSON, and these can supply local facts in Ansible. An alternate directory can be specified using the `fact_path` play directive.

## Examples:

Module setup. Display all facts from localhost.

```sh
$ ansible localhost -m setup
```

**Output:**

```sh

localhost | SUCCESS => {
    "ansible_facts": {
        "ansible_all_ipv4_addresses": [
            "10.6.86.147",
            "192.168.99.2"
        ],
        "ansible_all_ipv6_addresses": [
            "fe80::7914:4dba:3a4e:eb5a",
            "fe80::5478:fc57:4f08:8bdb"
        ],
        "ansible_apparmor": {
            "status": "disabled"
        },
        "ansible_architecture": "x86_64",
        "ansible_bios_date": "12/01/2006",
        .
        .
        .
```
--------------------------------------------------------------------------------

Module setup. Display only facts regarding memory found by ansible on localhost and output them.

```sh
$ ansible localhost -m setup -a 'filter=ansible_*_mb'
```

**Output:**

```sh

localhost | SUCCESS => {
    "ansible_facts": {
        "ansible_memfree_mb": 1515,
        "ansible_memory_mb": {
            "nocache": {
                "free": 2116,
                "used": 1312
            },
            "real": {
                "free": 1515,
                "total": 3428,
                "used": 1913
            },
            "swap": {
                "cached": 0,
                "free": 2047,
                "total": 2047,
                "used": 0
            }
        },
        "ansible_memtotal_mb": 3428,
        "ansible_swapfree_mb": 2047,
        "ansible_swaptotal_mb": 2047
    },
    "changed": false
}

```
--------------------------------------------------------------------------------

Local facts. **INI** format:

```sh
[general]
foo=1
bar=2
```
Put `ini_example.fact` to the `/etc/ansible/facts.d` directory.

```sh
$ ansible localhost -m setup -a 'filter=ansible_local'
```


**Output:**

```sh
localhost | SUCCESS => {
    "ansible_facts": {
        "ansible_local": {
            "ini_example": {
                "general": {
                    "bar": "2",
                    "foo": "1"
                }
            }
        }
    },
    "changed": false
}
```


--------------------------------------------------------------------------------

Local facts. **JSON** format:

```sh
{
    "software": {
        "apache": {
          "version": "2.4",
          "install_src": "backport_deb"
        },
        "mysql-server": {
          "version": "5.5",
          "install_src": "manual_compile"
        },
        "redis": {
          "version": "3.0.7",
          "install_src": "manual_compile"
        }
    }
}
```
Put `json_example.fact` to the `/etc/ansible/facts.d` directory.


```sh
$ ansible localhost -m setup -a 'filter=ansible_local'
```


**Output:**

```sh
localhost | SUCCESS => {
    "ansible_facts": {
        "ansible_local": {
            "json_example": {
                "software": {
                    "apache": {
                        "install_src": "backport_deb",
                        "version": "2.4"
                    },
                    "mysql-server": {
                        "install_src": "manual_compile",
                        "version": "5.5"
                    },
                    "redis": {
                        "install_src": "manual_compile",
                        "version": "3.0.7"
                    }
                }
            }
        }
    },
    "changed": false
}
```

--------------------------------------------------------------------------------

Local facts. **Executable** script returning result in JSON format:

```sh
#!/bin/bash

JAVA_VERSION=`java -version 2>&1 | awk -F '"' '/version/ {print $2}'`

cat <<EOF
{
    "java_version" : "$JAVA_VERSION"
}
EOF
```
Put `exec_java.fact` to the `/etc/ansible/facts.d` directory. Make sure that script is executable.

```sh
$ ansible localhost -m setup -a 'filter=ansible_local'
```


**Output:**

```sh
localhost | SUCCESS => {
    "ansible_facts": {
        "ansible_local": {
            "exec_java": {
                "java_version": "1.8.0_131"
            }
        }
    },
    "changed": false
}
```

