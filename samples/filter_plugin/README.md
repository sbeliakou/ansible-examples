# Filter plugin

[http://docs.ansible.com/ansible/dev_guide/developing_plugins.html#filter-plugins]

Example contents:
- [demo playbook](filter_example.yml)
- [ansible config](ansible.cfg)
- [filter plugin](filter/filter_plugin.py)

Usage:
```sh
$ ansible-playbook filter_example.yml
```

Output:
```sh
PLAY ***************************************************************************

TASK [setup] *******************************************************************
ok: [localhost]

TASK [First filter usage example] **********************************************
ok: [localhost] => {
    "msg": "test processed with one_filter"
}

TASK [Second filter usage example] *********************************************
ok: [localhost] => {
    "msg": "one - two - three processed with another_filter"
}

PLAY RECAP *********************************************************************
localhost                  : ok=3    changed=0    unreachable=0    failed=0   

```
