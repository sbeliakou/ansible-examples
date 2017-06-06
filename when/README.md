# Ansible 'when statement' example

## Resources:

- [Ansible Docs](http://docs.ansible.com/ansible/playbooks_conditionals.html#the-when-statement)
- [Demo Playbook](example_when.yml)

## Examples:

```sh
$ ansible-playbook example_when.yml -c local
```

**Output:**

```sh

PLAY [example_when] *******************************************************

TASK [Gathering Facts] ****************************************************
ok: [localhost]

TASK [Show message according to 'When' condition] *************************
ok: [localhost] => {
    "msg": "OS: CentOS 7"
}

PLAY RECAP ****************************************************************
localhost                  : ok=2    changed=0    unreachable=0    failed=0

```

