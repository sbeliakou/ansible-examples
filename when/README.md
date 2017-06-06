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

TASK [debug] **************************************************************
ok: [localhost] => {
    "msg": "System epbyminw5865-t1 has gateway 10.6.86.1"
}

PLAY RECAP ****************************************************************
localhost                  : ok=2    changed=0    unreachable=0    failed=0

```

