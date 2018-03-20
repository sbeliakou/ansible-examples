## Testing Inventory Script
```
$ ./vagrant_inventory.py --list
{
    "vagrant": {
        "hosts": [
            "default"
        ],
        "vars": {
            "ansible_user": "vagrant",
            "ansible_private_key_file": "~/.vagrant.d/insecure_private_key"
        }
    },
    "_meta": {
        "hostvars": {
            "default": {
                "ansible_port": "2200",
                "ansible_host": "127.0.0.1"
            }
        }
    }
}
```

```
$ ./vagrant_inventory.py --host default
{
    "ansible_port": "2200",
    "ansible_ssh_user": "vagrant",
    "ansible_ssh_private_key_file": "~/.vagrant.d/insecure_private_key",
    "ansible_host": "127.0.0.1"
}
```

## Playbook
```yaml
- hosts: vagrant

  tasks:
  - debug: var=inventory_hostname
```

## Testing Playbook

```
$ ansible-playbook test-vagrant-inventory.yml -i vagrant_inventory.py
```
```
PLAY [vagrant] *****************************************************************

TASK [Gathering Facts gather_subset=all, gather_timeout=10] ********************
ok: [default]

TASK [debug var=inventory_hostname] ********************************************
ok: [default] => {
    "inventory_hostname": "default"
}

PLAY RECAP *********************************************************************
default                    : ok=2    changed=0    unreachable=0    failed=0
```