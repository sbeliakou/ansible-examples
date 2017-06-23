# Ansible custom modules example

## Resources:
- [Ansible Docs](http://docs.ansible.com/ansible/dev_guide/developing_modules.html)
- [Testing modules](http://docs.ansible.com/ansible/dev_guide/developing_modules_general.html#testing-your-module)
- [Return values common to all modules](http://docs.ansible.com/ansible/common_return_values.html)
- [Demo Python module](library/python-module.py)
- [Demo Python Boilerplate module](library/boilerplate.py)
- [Demo Bash module](library/bash-module.sh)
- [Demo Ansible Facts module](library/fact-module.py)

Custom modules can be written in any language and should be placed in the library folder by default.

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
$ ansible-playbook facts_module_example.yml -vv
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

```sh
$ ansible-playbook python_module_boilerplate_example.yml -vv
```
**Output:**
```sh
PLAY [Using custom module boilerplate] ******************************************

TASK [Gathering Facts] **********************************************************
ok: [localhost]
META: ran handlers

TASK [Show some info] ***********************************************************
task path: /home/vagrant/playbooks/ansible-examples/modules/python_module_boilerplate_example.yml:5
changed: [localhost] => {"changed": true, "created": "directory", "failed": false, "owner": "vagrant", "permossions": "0755"}

TASK [Show output] **************************************************************
task path: /home/vagrant/playbooks/ansible-examples/modules/python_module_boilerplate_example.yml:9
ok: [localhost] => {
    "failed": false,
    "result": {
        "changed": true,
        "created": "directory",
        "failed": false,
        "owner": "vagrant",
        "permossions": "0755"
    }
}
META: ran handlers
META: ran handlers

PLAY RECAP ********************************************************************
localhost                  : ok=3    changed=1    unreachable=0    failed=0
```
**If module support check mode, you can execute ansible-playbook with ```--check``` key (See more information about check mode [here](http://docs.ansible.com/ansible/playbooks_checkmode.html) ):**
```sh
$ ansible-playbook python_module_boilerplate_example.yml --check
```
```sh
PLAY [Using custom module boilerplate] **************************************

TASK [Gathering Facts] ******************************************************
ok: [localhost]

TASK [Show some info] *******************************************************
changed: [localhost]

TASK [Show output] ***********************************************************
ok: [localhost] => {
    "failed": false,
    "result": {
        "changed": true,
        "created": "directory",
        "failed": false,
        "owner": "vagrant",
        "permossions": "0755"
    }
}

PLAY RECAP *******************************************************************
localhost                  : ok=3    changed=1    unreachable=0    failed=0

```

**Module testing with :**
```sh
$ ansible/hacking/test-module -m ./library/python-module.py
```
**Output:**
```sh
***********************************
RAW OUTPUT
{"time": "2017-06-22 10:14:47.017274"}


***********************************
PARSED OUTPUT
{
    "time": "2017-06-22 10:14:47.017274"
}
```
