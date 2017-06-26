# Filters

- [Filters](http://docs.ansible.com/ansible/playbooks_filters.html)
- [Tests](https://docs.ansible.com/ansible/playbooks_tests.html)

## Filter examples:
- formatting data filter ([formatting.yml](formatting.yml))
- list filter ([list.yml](list.yml))
- theory filter ([theory.yml](theory.yml))
- random number filter ([random.yml](random.yml))
- math filter ([math.yml](math.yml))
- ip address filter ([ip.yml](ip.yml))
- hashing filter ([hash.yml](hash.yml))
- omit, mandatory, default filter ([omit_mandatory_default.yml](omit_mandatory_default.yml))

### Filters For Formatting Data
```
$ ansible-playbook formatting.yml
```
```
PLAY ***************************************************************************

TASK [setup] *******************************************************************
ok: [localhost]

TASK [command] *****************************************************************
changed: [localhost]

TASK [set_fact] ****************************************************************
ok: [localhost]

TASK [Shell output of the current playbook] ************************************
ok: [localhost] => {
    "result.stdout": "- hosts: localhost\n  connection: local\n  tasks:\n    - shell: cat formatting.yml\n      register: result\n    - set_fact: from_yaml=\"{# result.stdout | from_yaml #}\"\n    - name: \"Shell output of the current playbook\"\n      debug: var=result.stdout\n    - name: \"YAML-formatted output of the current playbook\"\n      debug: var=from_yaml"
}

TASK [YAML-formatted output of the current playbook] ***************************
ok: [localhost] => {
    "from_yaml": [
        {
            "connection": "local", 
            "hosts": "localhost", 
            "tasks": [
                {
                    "register": "result", 
                    "shell": "cat formatting.yml"
                }, 
                {
                    "set_fact": "from_yaml=\"{# result.stdout | from_yaml"
                }, 
                {
                    "debug": "var=result.stdout", 
                    "name": "Shell output of the current playbook"
                }, 
                {
                    "debug": "var=from_yaml", 
                    "name": "YAML-formatted output of the current playbook"
                }
            ]
        }
    ]
}

PLAY RECAP *********************************************************************
localhost                  : ok=5    changed=1    unreachable=0    failed=0   
```
### List Filters
```
$ ansible-playbook list.yml
```
```
PLAY ***************************************************************************

TASK [setup] *******************************************************************
ok: [localhost]

TASK [Min value of the list [1,2,3,4,5]] ***************************************
ok: [localhost] => {
    "msg": "1"
}

TASK [Max value of the list [1,2,3,4,5]] ***************************************
ok: [localhost] => {
    "msg": "5"
}

TASK [Random list from the list [1,2,3,4,5]] ***********************************
ok: [localhost] => {
    "msg": [
        3, 
        2, 
        1, 
        4, 
        5
    ]
}

PLAY RECAP *********************************************************************
localhost                  : ok=4    changed=0    unreachable=0    failed=0   
```
### Theory Filters
```
$ ansible-playbook theory.yml
```
```
PLAY ***************************************************************************

TASK [setup] *******************************************************************
ok: [localhost]

TASK [A unique set from a list [1,2,1,3,1]] ************************************
ok: [localhost] => {
    "msg": [
        1, 
        2, 
        3
    ]
}

TASK [A union of list [1,2,1,3,1] and list [4,5,4,6,1]] ************************
ok: [localhost] => {
    "msg": [
        1, 
        2, 
        3, 
        4, 
        5, 
        6
    ]
}

TASK [An intersection of list [1,2,1,3,1] and list [4,5,4,6,1]] ****************
ok: [localhost] => {
    "msg": [
        1
    ]
}

TASK [A difference between list [1,2,1,3,1] and list [4,5,4,6,1]] **************
ok: [localhost] => {
    "msg": [
        2, 
        3
    ]
}

TASK [A symmetric difference between list [1,2,1,3,1] and list [4,5,4,6,1]] ****
ok: [localhost] => {
    "msg": [
        2, 
        3, 
        4, 
        5, 
        6
    ]
}

PLAY RECAP *********************************************************************
localhost                  : ok=6    changed=0    unreachable=0    failed=0   
```
### Random Number Filters
```
$ ansible-playbook random.yml
```
```
PLAY ***************************************************************************

TASK [setup] *******************************************************************
ok: [localhost]

TASK [A random number from list [1,2,1,3,1]] ***********************************
ok: [localhost] => {
    "msg": "2"
}

TASK [A random number from 0 to 100 but in steps of 10] ************************
ok: [localhost] => {
    "msg": "30"
}

TASK [A random number from 1 to 100 but in steps of 10] ************************
ok: [localhost] => {
    "msg": "31"
}

PLAY RECAP *********************************************************************
localhost                  : ok=4    changed=0    unreachable=0    failed=0   
```
### Math Filters
```
$ ansible-playbook math.yml
```
```
PLAY ***************************************************************************

TASK [setup] *******************************************************************
ok: [localhost]

TASK [The power of 4] **********************************************************
ok: [localhost] => {
    "msg": "16.0"
}

TASK [The square root of 4] ****************************************************
ok: [localhost] => {
    "msg": "2.0"
}

PLAY RECAP *********************************************************************
localhost                  : ok=3    changed=0    unreachable=0    failed=0   
```
### IP Address Filters
```
$ ansible-playbook ip.yml
```
```
PLAY ***************************************************************************

TASK [setup] *******************************************************************
ok: [localhost]

TASK [Test if a string '192.168.0.1' is a valid IP address] ********************
ok: [localhost] => {
    "msg": "192.168.0.1"
}

TASK [Test if a string '192.168.257.1' is a valid IP address] ******************
ok: [localhost] => {
    "msg": false
}

TASK [Test if a string '192.168.0.1' is a valid IPv6 address] ******************
ok: [localhost] => {
    "msg": false
}

TASK [Get the IP address itself from a CIDR '192.0.2.1/24'] ********************
ok: [localhost] => {
    "msg": "192.0.2.1"
}

PLAY RECAP *********************************************************************
localhost                  : ok=5    changed=0    unreachable=0    failed=0   
```
### Hashing Filters
```
$ ansible-playbook hash.yml
```
```
PLAY ***************************************************************************

TASK [setup] *******************************************************************
ok: [localhost]

TASK [Sha1 hash of a string 'test1'] *******************************************
ok: [localhost] => {
    "msg": "b444ac06613fc8d63795be9ad0beaf55011936ac"
}

TASK [Md5 hash of a string 'test1'] ********************************************
ok: [localhost] => {
    "msg": "5a105e8b9d40e1329780d62ea2265d8a"
}

TASK [Checksum of a string 'test2'] ********************************************
ok: [localhost] => {
    "msg": "109f4b3c50d7b0df729d299bc6f8e9ef9066971f"
}

TASK [Sha512 password hash (random salt)] **************************************
ok: [localhost] => {
    "msg": "$6$amhGqKCZbnICa549$rspPoJPGLnWdDzCr5TBllTXDW5VQsMkF2Ad4mLdVdAIR7iepYG5820sx/5t0XfHAGZ4a6AWPWIHQoEBt8CkUt."
}

PLAY RECAP *********************************************************************
localhost                  : ok=5    changed=0    unreachable=0    failed=0   
```
### Omit, mandatory, default Filters
```
$ ansible-playbook omit_mandatory_default.yml
```
```
PLAY [localhost] **************************************************************************************************************************************************************************************************

TASK [Gathering Facts] ********************************************************************************************************************************************************************************************
ok: [localhost]

TASK [example of default filter] **********************************************************************************************************************************************************************************
ok: [localhost] => {
    "msg": "myvar value is defined"
}

PLAY [localhost] **************************************************************************************************************************************************************************************************

TASK [Gathering Facts] ********************************************************************************************************************************************************************************************
ok: [localhost]

TASK [example of default filter] **********************************************************************************************************************************************************************************
ok: [localhost] => {
    "msg": "myvar value is default"
}

PLAY [localhost] **************************************************************************************************************************************************************************************************

TASK [Gathering Facts] ********************************************************************************************************************************************************************************************
ok: [localhost]

TASK [touch files with an optional mode] **************************************************************************************************************************************************************************
changed: [localhost] => (item={u'path': u'/tmp/foo'})
changed: [localhost] => (item={u'path': u'/tmp/bar'})
changed: [localhost] => (item={u'path': u'/tmp/baz', u'mode': u'0444'})

PLAY [localhost] **************************************************************************************************************************************************************************************************

TASK [Gathering Facts] ********************************************************************************************************************************************************************************************
ok: [localhost]

TASK [touch files with a mandatory mode] **************************************************************************************************************************************************************************
fatal: [localhost]: FAILED! => {"failed": true, "msg": "Mandatory variable not defined."}
	to retry, use: --limit @/home/shreben/ansible/ansible-examples/filters/omit_mandatory_default.retry

PLAY RECAP ********************************************************************************************************************************************************************************************************
localhost                  : ok=7    changed=1    unreachable=0    failed=1   

```
