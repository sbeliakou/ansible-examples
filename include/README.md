# Ansible 'include play and task' example

## Resources:

- [Ansible Docs](http://docs.ansible.com/ansible/playbooks_roles.html#task-versus-play-includes)
- [Demo Playbook](example_include.yml)

## Examples:

```sh
$ ansible-playbook example_include.yml -c local
```

**Output:**

```sh

PLAY [Example of including a play and a task] *****************************

TASK [Gathering Facts] ****************************************************
ok: [localhost]

TASK [main task] **********************************************************
ok: [localhost] => {
    "msg": "It is a main task"
}

TASK [child task] *********************************************************
ok: [localhost] => {
    "msg": "It is a child task"
}

PLAY [Child play] *********************************************************

TASK [Gathering Facts] ****************************************************
ok: [localhost]

TASK [task of child_play] *************************************************
ok: [localhost] => {
    "msg": "It is a task of a child play"
}

PLAY RECAP ****************************************************************
localhost                  : ok=5    changed=0    unreachable=0    failed=0

```

