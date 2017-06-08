# Variables

[http://docs.ansible.com/ansible/playbooks_variables.html]

Example contents:
- [demo playbook](vars_example.yml)
- [sample inventory](inventory)

```sh
$ ansible-playbook vars_example.yml -i inventory
```
```sh
PLAY ***************************************************************************

TASK [setup] *******************************************************************
ok: [localhost]

TASK [debug] *******************************************************************
ok: [localhost] => {
    "myvar": "myvar defined in group vars"
}

PLAY ***************************************************************************

TASK [setup] *******************************************************************
ok: [localhost]

TASK [debug] *******************************************************************
ok: [localhost] => {
    "myvar": "myvar defined in playbook"
}

PLAY ***************************************************************************

TASK [setup] *******************************************************************
ok: [localhost]

TASK [Example of the builtin variable ansible-version] *************************
ok: [localhost] => {
    "ansible_version": {
        "full": "2.0.0.2", 
        "major": 2, 
        "minor": 0, 
        "revision": 0, 
        "string": "2.0.0.2"
    }
}

PLAY RECAP *********************************************************************
localhost                  : ok=6    changed=0    unreachable=0    failed=0   

```

Example of passing variables on the command line
```sh
$ ansible-playbook vars_example.yml -i inventory -e "myvar='myvar defined in the command line'"
```
```sh
PLAY ***************************************************************************

TASK [setup] *******************************************************************
ok: [localhost]

TASK [debug] *******************************************************************
ok: [localhost] => {
    "myvar": "myvar defined in the command line"
}

PLAY ***************************************************************************

TASK [setup] *******************************************************************
ok: [localhost]

TASK [debug] *******************************************************************
ok: [localhost] => {
    "myvar": "myvar defined in the command line"
}

PLAY ***************************************************************************

TASK [setup] *******************************************************************
ok: [localhost]

TASK [Example of the builtin variable ansible-version] *************************
ok: [localhost] => {
    "ansible_version": {
        "full": "2.0.0.2", 
        "major": 2, 
        "minor": 0, 
        "revision": 0, 
        "string": "2.0.0.2"
    }
}

PLAY RECAP *********************************************************************
localhost                  : ok=6    changed=0    unreachable=0    failed=0   

```
