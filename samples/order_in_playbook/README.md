# Ansible 'Order in playbook' example

## Resources:

- [Ansible Docs](http://docs.ansible.com/ansible/playbooks_roles.html#roles)
- [Demo Playbook](example_order.yml)

## Examples:

```sh
$ ansible-playbook example_order.yml -c local
```

**Output:**

```sh

PLAY [Order in playbook] **************************************************

TASK [Gathering Facts] ****************************************************
ok: [localhost]

TASK [Example of pre_task] ************************************************
ok: [localhost] => {
    "msg": "Good morning!"
}

TASK [some_role : Example of role_task] ***********************************
ok: [localhost] => {
    "msg": "This is a task from 'some_role'"
}

TASK [Example of main task] ***********************************************
changed: [localhost]

RUNNING HANDLER [Some trigger] ********************************************
ok: [localhost] => {
    "msg": "Something triggers me to say Hello!"
}

TASK [Example of post-task] ***********************************************
ok: [localhost] => {
    "msg": "Good evening!"
}

PLAY RECAP ****************************************************************
localhost                  : ok=6    changed=1    unreachable=0    failed=0

```

