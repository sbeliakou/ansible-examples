# Ansible custom modules example

## Resources:
- [Ansible Docs](http://docs.ansible.com/ansible/dev_guide/developing_modules.html)
- [Demo Python module](library/python-module.py)
- [Demo Bash module](library/bash-module.sh)
- [Demo Ansible Facts module](library/facts-module.py)

## Examples:

**Running ansible playbook with custom modules:**
```sh 
$ ansible-playbook python_module_example.yml -vv
```
**Output:**
 ```sh
PLAY [Using custom python module] **********************************************

TASK [setup] *******************************************************************
ok: [localhost]

TASK [Getting current time and date] *******************************************
task path: /home/vagrant/ansible-examples/modules/python_module_example.yml:5
ok: [localhost] => {"changed": false, "time": "2017-06-07 12:46:48.724681"}

TASK [Show output] *************************************************************
task path: /home/vagrant/ansible-examples/modules/python_module_example.yml:9
ok: [localhost] => {
    "result": {
        "changed": false,
        "time": "2017-06-07 12:46:48.724681"
    }
}

PLAY RECAP *********************************************************************
localhost                  : ok=3    changed=0    unreachable=0    failed=0
```

```sh
$ ansible-playbook bash_module_example.yml -vv
```
**Output:**
```sh
PLAY [Using custom bash module] ************************************************

TASK [setup] *******************************************************************
ok: [localhost]

TASK [Print some phrase] *******************************************************
task path: /home/vagrant/ansible-examples/modules/bash_module_example.yml:5
ok: [localhost] => {"changed": false, "failed": false, "phrase": "Hello_world"}

TASK [Show output] *************************************************************
task path: /home/vagrant/ansible-examples/modules/bash_module_example.yml:9
ok: [localhost] => {
    "result": {
        "changed": false,
        "failed": false,
        "phrase": "Hello_world"
    }
}

PLAY RECAP *********************************************************************
localhost                  : ok=3    changed=0    unreachable=0    failed=0
```
```sh
ansible-playbook facts_module_example.yml -vv
```
**Output:**
```sh
PLAY [Using custom ansible facts module] ***************************************

TASK [setup] *******************************************************************
ok: [localhost]

TASK [Adding custom ansible facts] *********************************************
task path: /home/vagrant/ansible-examples/modules/facts_module_example.yml:5
changed: [localhost] => {"ansible_facts": {"phrase": "Hello_World"}, "changed": true}

TASK [Show output] *************************************************************
task path: /home/vagrant/ansible-examples/modules/facts_module_example.yml:8
ok: [localhost] => {
    "phrase": "Hello_World"
}

PLAY RECAP *********************************************************************
localhost                  : ok=3    changed=1    unreachable=0    failed=0
```
