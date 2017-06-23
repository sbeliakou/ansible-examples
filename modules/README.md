# Ansible custom modules example

## Resources:
- [Ansible Docs](http://docs.ansible.com/ansible/dev_guide/developing_modules.html)
- [Building a simle modules](http://docs.ansible.com/ansible/dev_guide/developing_modules_general.html)
- [Testing modules](http://docs.ansible.com/ansible/dev_guide/developing_modules_general.html#testing-your-module)
- [Return values common to all modules](http://docs.ansible.com/ansible/common_return_values.html)
- [Demo Python module](library/python-module.py)
- [Demo Python Boilerplate module](library/boilerplate.py)
- [Demo Bash module](library/bash-module.sh)
- [Demo Ansible Facts module](library/fact-module.py)
- [Demo playbook with custom modules](custom_modules_examples.yml)

Custom modules can be written in any language and should be placed in the library folder by default. Extension is not required. You should test your module before using (See more information about module testing [here](http://docs.ansible.com/ansible/dev_guide/developing_modules_general.html#testing-your-module). 
## Testing examples:
```sh
$ git clone git://github.com/ansible/ansible.git
$ source ansible/hacking/env-setup
$ ansible/hacking/test-module -m library/bash-module.sh -a "phrase=Hello_world"
```
**Output:**
```sh
* including generated source, if any, saving to: /home/vagrant/.ansible_module_generated
***********************************
RAW OUTPUT
{"failed": false, "changed": false, "phrase": "Hello_world"}

***********************************
PARSED OUTPUT
{
    "changed": false,
    "failed": false,
    "phrase": "Hello_world"
}
```
```sh
$ ansible/hacking/test-module -m library/python-module.py
```
**Output:**
```sh
* including generated source, if any, saving to: /home/vagrant/.ansible_module_generated
***********************************
RAW OUTPUT
{"time": "2017-06-23 07:28:37.142400"}


***********************************
PARSED OUTPUT
{
    "time": "2017-06-23 07:28:37.142400"
}
```
```sh
$ ansible/hacking/test-module -m library/boilerplate.py -a "file=directory owner=vagrant mode=0755 recurse=True"
```
**Output:**
```sh
* including generated source, if any, saving to: /home/vagrant/.ansible_module_generated
* ansiballz module detected; extracted module source to: /home/vagrant/debug_dir
***********************************
RAW OUTPUT

{"owner": "vagrant", "permossions": "0755", "changed": true, "created": "directory", "invocation": {"module_args": {"owner": "vagrant", "recurse": true, "mode": "0755", "file": "directory"}}}


***********************************
PARSED OUTPUT
{
    "changed": true,
    "created": "directory",
    "invocation": {
        "module_args": {
            "file": "directory",
            "mode": "0755",
            "owner": "vagrant",
            "recurse": true
        }
    },
    "owner": "vagrant",
    "permossions": "0755"
}
```
```sh
$ ansible/hacking/test-module -m library/fact-module.py -a "myfact=myvalue"
```
**Output:**
```sh
* including generated source, if any, saving to: /home/vagrant/.ansible_module_generated
***********************************
RAW OUTPUT
{"changed": true, "ansible_facts": {"myfact": "myvalue"}}


***********************************
PARSED OUTPUT
{
    "ansible_facts": {
        "myfact": "myvalue"
    },
    "changed": true
}
```

## Running ansible playbook with custom modules:

```sh
$ ansible-playbook custom_modules_examples.yml -vv
```
**Output:**
```sh
PLAY [Examples Of Using Custom Modules] ****************************************

TASK [setup] *******************************************************************
ok: [localhost]

TASK [Using simple bash module] ************************************************
task path: /home/vagrant/playbooks/ansible-examples/modules/custom_modules_examples.yml:5
ok: [localhost] => {"changed": false, "failed": false, "phrase": "Hello_world"}

TASK [Show output] *************************************************************
task path: /home/vagrant/playbooks/ansible-examples/modules/custom_modules_examples.yml:9
ok: [localhost] => {
    "result": {
        "changed": false,
        "failed": false,
        "phrase": "Hello_world"
    }
}

TASK [Using simple python module] **********************************************
task path: /home/vagrant/playbooks/ansible-examples/modules/custom_modules_examples.yml:12
ok: [localhost] => {"changed": false, "time": "2017-06-23 08:24:16.712942"}

TASK [Show output] *************************************************************
task path: /home/vagrant/playbooks/ansible-examples/modules/custom_modules_examples.yml:16
ok: [localhost] => {
    "result": {
        "changed": false,
        "time": "2017-06-23 08:24:16.712942"
    }
}

TASK [Using module boilerplate] ************************************************
task path: /home/vagrant/playbooks/ansible-examples/modules/custom_modules_examples.yml:19
changed: [localhost] => {"changed": true, "created": "directory", "owner": "vagrant", "permossions": "0755"}

TASK [Show output] *************************************************************
task path: /home/vagrant/playbooks/ansible-examples/modules/custom_modules_examples.yml:23
ok: [localhost] => {
    "result": {
        "changed": true,
        "created": "directory",
        "owner": "vagrant",
        "permossions": "0755"
    }
}

TASK [Using module for adding custom ansible fact] *****************************
task path: /home/vagrant/playbooks/ansible-examples/modules/custom_modules_examples.yml:26
changed: [localhost] => {"ansible_facts": {"myfact": "myvalue"}, "changed": true}

TASK [Show output] *************************************************************
task path: /home/vagrant/playbooks/ansible-examples/modules/custom_modules_examples.yml:29
ok: [localhost] => {
    "myfact": "myvalue"
}

PLAY RECAP *********************************************************************
localhost                  : ok=9    changed=2    unreachable=0    failed=0

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
