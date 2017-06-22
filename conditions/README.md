# Ansible 'Condions' examples

## Resources:

- [Ansible Docs](http://docs.ansible.com/ansible/playbooks_conditionals.html)
- [Demo Playbook when-variables](example_conditions_variables.yml)
- [Demo Playbook when-succeeded](example_conditions_succeeded.yml)
- [Demo Playbook when-default](example_conditions_default.yml)
- [Demo Playbook when-(un)defined](example_conditions_defined.yml)
- [Demo Playbook when-register](example_conditions_register.yml)
- [Demo Playbook when-boolean](example_conditions_boolean.yml)
- [Demo Playbook when-item](example_conditions_when-item.yml)
- [Demo Playbook when-search](example_conditions_when-search.yml)

## Examples:


### Condition based on variables:

- [Demo Playbook when-variables](example_conditions_variables.yml)

```sh
$ ansible-playbook example_conditions_variables.yml -c local
```

**Output:**

```sh

PLAY [Statement is based on variables] *******************************************************************

TASK [Gathering Facts] ***********************************************************************************
ok: [localhost]

TASK [Echo something on Debian systems] ******************************************************************
skipping: [localhost]

TASK [Echo something on CentOS 7 systems] ****************************************************************
ok: [localhost] => {
    "msg": "OS is CentOS 7"
}

PLAY RECAP ***********************************************************************************************
localhost                  : ok=2    changed=0    unreachable=0    failed=0
```

----------

### Condition based on success or failure of registering:

- [Demo Playbook when-succeeded](example_conditions_succeeded.yml)

```sh
$ ansible-playbook example_conditions_succeeded.yml -c local
```

**Output:**

```sh

PLAY [Statement based on the result of registering] ******************************************************

TASK [Gathering Facts] ***********************************************************************************
ok: [localhost]

TASK [Echo something] ************************************************************************************
ok: [localhost] => {
    "msg": "Hello world!"
}

TASK [Do it if the result of the first step was failed] **************************************************
skipping: [localhost]

TASK [Do it if the result of the first step was succeeded] ***********************************************
ok: [localhost] => {
    "msg": "Everything is OK"
}

TASK [Do it if the result of the first step was skipped] *************************************************
skipping: [localhost]

PLAY RECAP ***********************************************************************************************
localhost                  : ok=3    changed=0    unreachable=0    failed=0
```


----------


### Condition when + using the |default filter:

- [Demo Playbook when-default](example_conditions_default.yml)

```sh
$ ansible-playbook example_conditions_default.yml -c local
```

**Output:**

```sh

PLAY [Using when + default filter] ***********************************************************************

TASK [Gathering Facts] ***********************************************************************************
ok: [localhost]

TASK [When list does not exist step is using default. Default is empty --> SKIP it] **********************

TASK [When mylist does not exist step is using default. Mylist exists --> DO it] *************************
skipping: [localhost] => (item=2)
skipping: [localhost] => (item=0)
ok: [localhost] => (item=10) => {
    "item": 10,
    "msg": 10
}
ok: [localhost] => (item=8) => {
    "item": 8,
    "msg": 8
}
ok: [localhost] => (item=6) => {
    "item": 6,
    "msg": 6
}
skipping: [localhost] => (item=4)

PLAY RECAP ***********************************************************************************************
localhost                  : ok=2    changed=0    unreachable=0    failed=0

```


----------


### Condition based on (un)defined variables:

- [Demo Playbook when-(un)defined](example_conditions_defined.yml)

```sh
$ ansible-playbook  example_conditions_register.yml -c local
```

**Output:**

```sh

PLAY [Check registered variable for emptiness] ***********************************************************

TASK [Gathering Facts] ***********************************************************************************
ok: [localhost]

TASK [debug] *********************************************************************************************
ok: [localhost] => {
    "msg": "I've got a 'power' and am not afraid to use it!"
}

TASK [fail] **********************************************************************************************
fatal: [localhost]: FAILED! => {"changed": false, "failed": true, "msg": 
       "Bailing out. this play requires 'bar'"} to retry, use: --limit 
	   @/root/ansible/examples/ansible-examples/conditions/example_conditions_defined.retry

PLAY RECAP ***********************************************************************************************
localhost                  : ok=2    changed=0    unreachable=0    failed=1
```

----------


### Condition based on registered variables:

- [Demo Playbook when-register](example_conditions_register.yml)

```sh
$ ansible-playbook  example_conditions_register.yml -c local
```

**Output:**

```sh

PLAY [Check registered variable for emptiness] ***********************************************************

TASK [Gathering Facts] ***********************************************************************************
ok: [localhost]

TASK [Ensure directory exists] ***************************************************************************
changed: [localhost]

TASK [list contents of directory] ************************************************************************
changed: [localhost]

TASK [check contents for emptiness] **********************************************************************
ok: [localhost] => {
    "msg": "Directory is empty"
}

PLAY RECAP ***********************************************************************************************
localhost                  : ok=4    changed=2    unreachable=0    failed=0

```

----------


### Condition based on a variable’s boolean value:

- [Demo Playbook when-boolean](example_conditions_boolean.yml)

```sh
$ ansible-playbook  example_conditions_boolean.yml -c local
```

**Output:**

```sh

PLAY [Execution of a task based on a variable’s boolean value] *******************************************

TASK [Gathering Facts] ***********************************************************************************
ok: [localhost]

TASK [Step when epic is True] ****************************************************************************
ok: [localhost] => {
    "msg": "This certainly is epic!"
}

TASK [Step when epic is not True] ************************************************************************
skipping: [localhost]

PLAY RECAP ***********************************************************************************************
localhost                  : ok=2    changed=0    unreachable=0    failed=0
```

----------


### Condition 'when item':

- [Demo Playbook when-item](example_conditions_when-item.yml)

```sh
$ ansible-playbook  example_conditions_when-item.yml -c local
```

**Output:**

```sh
PLAY [Combining when with with_items] ********************************************************************

TASK [Gathering Facts] ***********************************************************************************
ok: [localhost]

TASK [statement WHEN is processed separately for each item] **********************************************
skipping: [localhost] => (item=4)
skipping: [localhost] => (item=2)
skipping: [localhost] => (item=0)
ok: [localhost] => (item=10) => {
    "item": 10,
    "msg": "10 is > 5 "
}
ok: [localhost] => (item=8) => {
    "item": 8,
    "msg": "8 is > 5 "
}
ok: [localhost] => (item=6) => {
    "item": 6,
    "msg": "6 is > 5 "
}

PLAY RECAP ***********************************************************************************************
localhost                  : ok=2    changed=0    unreachable=0    failed=0
```

### Condition 'when search':

- [Demo Playbook when-search](example_conditions_when-search.yml)

```sh
$ ansible-playbook  example_conditions_when-search.yml
```

**Output:**

```sh
PLAYBOOK: example_conditions_when-search.yml ***********************************
1 plays in example_conditions_when-search.yml

PLAY [localhost] ***************************************************************

TASK [setup] *******************************************************************
ok: [localhost]

TASK [debug] *******************************************************************
task path: /private/tmp/example_conditions_when-search.yml:9
ok: [localhost] => (item=asdfasdfasdfAAAasdfasdfasdf) => {
    "item": "asdfasdfasdfAAAasdfasdfasdf",
    "msg": "Variable contains 'AAA' -> 'asdfasdfasdfAAAasdfasdfasdf'"
}
skipping: [localhost] => (item=qweqwerqweqweqqweqweqweqweq)  => {"changed": false, "item": "qweqwerqweqweqqweqweqweqweq", "skip_reason": "Conditional check failed", "skipped": true}

PLAY RECAP *********************************************************************
localhost                  : ok=2    changed=0    unreachable=0    failed=0
```
