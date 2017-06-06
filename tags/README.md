# Ansible tags example

Using ```--tags ``` key:
 ```sh
$ ansible-playbook example-tags.yml -c local --tags "tag 1"
```
Output:
 ```sh
 [WARNING]: Host file not found: /etc/ansible/hosts

 [WARNING]: provided hosts list is empty, only localhost is available


PLAY [Tags example] ************************************************************

TASK [setup] *******************************************************************
ok: [localhost]

TASK [run playbook with tag 1] *************************************************
ok: [localhost] => {
    "msg": "runs when you use tag1"
}

TASK [reuse tag 1] *************************************************************
ok: [localhost] => {
    "msg": "runs when you use tag1 (reuse)"
}

TASK [using special tag always] ************************************************
ok: [localhost] => {
    "msg": "Always runs"
}

PLAY RECAP *********************************************************************
localhost                  : ok=4    changed=0    unreachable=0    failed=0
```
Using ```--skip-tags ``` key:
```sh
$ ansible-playbook example-tags.yml -c local --skip-tags "always,tag 1"
```
Output:
```sh
 [WARNING]: Host file not found: /etc/ansible/hosts

 [WARNING]: provided hosts list is empty, only localhost is available


PLAY [Tags example] ************************************************************

TASK [run playbook with tag 2] *************************************************
ok: [localhost] => {
    "msg": "runs when you use tag2"
}

PLAY RECAP *********************************************************************
localhost                  : ok=1    changed=0    unreachable=0    failed=0
```

See [documentation](http://docs.ansible.com/ansible/playbooks_tags.html) for more details.
