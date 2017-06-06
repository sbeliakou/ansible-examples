# Ansible local facts example

## Resources:

- [Ansible Docs](http://docs.ansible.com/ansible/playbooks_variables.html#local-facts-facts-d)
- [Demo Playbook](example_local-facts.yml)

## Example:

```sh
$ ansible-playbook example_local-facts.yml -c local
```

**Output:**

```sh

PLAY [Setting local facts] *************************************************

TASK [Gathering Facts] *****************************************************
ok: [localhost]

TASK [Ensure directory for ansible facts exists] ***************************
changed: [localhost]

TASK [Ensure example fact exists] ******************************************
changed: [localhost]

PLAY [Getting local fact] **************************************************

TASK [Gathering Facts] *****************************************************
ok: [localhost]

TASK [Display variable 'foo'] **********************************************
ok: [localhost] => {
    "msg": "foo = 1"
}

PLAY RECAP *****************************************************************
localhost                  : ok=5    changed=2    unreachable=0    failed=0

```

