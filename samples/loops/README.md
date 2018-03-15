# Ansible custom modules example

## Resources:
- [Ansible Docs](http://docs.ansible.com/ansible/playbooks_loops.html)

- [Demo playbook standart loop](standart-loop-example.yml)
- [Demo playbook loop with indexes](loops-with-indexes.yml)
- [Demo playbook nested loop](nested-loop-example.yml)
- [Demo playbook looping over hashes](looping-over-hashes-example.yml)
- [Demo playbook looping over files](looping-over-files-example.yml)
- [Demo playbook looping over fileglobs](looping-over-fileglobs-example.yml)
- [Demo playbook looping-over parallel sets data](looping-over-parallel-sets-data-example.yml)
- [Demo playbook looping over subelements](looping-over-subelements-example.yml)
- [Demo playbook looping over integer sequences](looping-over-integer-sequences-example.yml)
- [Demo playbook random choices](random-choices-example.yml)
- [Demo playbook iterating over result](iterating-over-result-example.yml)
- [Demo playbook of using register with a loop](looping-with-register.yml)
- [Demo playbook of do-until loop](loop-do-until.yml)
- [Demo playbook of loop control label](loop-control.yml)
## Examples:

**Running ansible playbook with different loops:**
- [Demo playbook standart loop](standart-loop-example.yml)
```sh 
$ ansible-playbook standart-loop-example.yml -vv
```
**Output:**
 ```sh
PLAY [Standart Loops Example] **************************************************

TASK [setup] *******************************************************************
ok: [localhost]

TASK [print several users] *****************************************************
task path: /home/vagrant/ansible-examples/loops/standart-loop-example.yml:5
ok: [localhost] => (item={u'name': u'bob', u'groups': u'root'}) => {
    "item": {
        "groups": "root",
        "name": "bob"
    },
    "msg": "User bob will be addedd to group root"
}
ok: [localhost] => (item={u'name': u'alice', u'groups': u'wheel'}) => {
    "item": {
        "groups": "wheel",
        "name": "alice"
    },
    "msg": "User alice will be addedd to group wheel"
}

PLAY RECAP *********************************************************************
localhost                  : ok=2    changed=0    unreachable=0    failed=0
```
- [Demo playbook nested loop](nested-loop-example.yml)
```sh
$ ansible-playbook nested-loop-example.yml -vv
```
**Output:**
```sh
PLAY [Nested Loops Example] ****************************************************

TASK [setup] *******************************************************************
ok: [localhost]

TASK [print several users with multiple groups] ********************************
task path: /home/vagrant/ansible-examples/loops/nested-loop-example.yml:5
ok: [localhost] => (item=[u'bob', u'root']) => {
    "item": [
        "bob",
        "root"
    ],
    "msg": "User bob will be added to group root"
}
ok: [localhost] => (item=[u'bob', u'wheel']) => {
    "item": [
        "bob",
        "wheel"
    ],
    "msg": "User bob will be added to group wheel"
}
ok: [localhost] => (item=[u'alice', u'root']) => {
    "item": [
        "alice",
        "root"
    ],
    "msg": "User alice will be added to group root"
}
ok: [localhost] => (item=[u'alice', u'wheel']) => {
    "item": [
        "alice",
        "wheel"
    ],
    "msg": "User alice will be added to group wheel"
}

PLAY RECAP *********************************************************************
localhost                  : ok=2    changed=0    unreachable=0    failed=0
```

- [Demo playbook loop with indexes](loops-with-indexes.yml)
```sh
$ ansible-playbook loops-with-indexes.yml
```
**Output:**
```sh
PLAY [localhost] ***************************************************************

TASK [Gathering Facts] *********************************************************
ok: [localhost]

TASK [indexed loop demo] *******************************************************
ok: [localhost] => (item=(0, u'apple')) => {
    "changed": false,
    "item": [
        0,
        "apple"
    ],
    "msg": "apple at position 0"
}
ok: [localhost] => (item=(1, u'pear')) => {
    "changed": false,
    "item": [
        1,
        "pear"
    ],
    "msg": "pear at position 1"
}
ok: [localhost] => (item=(2, u'banana')) => {
    "changed": false,
    "item": [
        2,
        "banana"
    ],
    "msg": "banana at position 2"
}
ok: [localhost] => (item=(3, u'kiwi')) => {
    "changed": false,
    "item": [
        3,
        "kiwi"
    ],
    "msg": "kiwi at position 3"
}

PLAY RECAP *********************************************************************
localhost                  : ok=2    changed=0    unreachable=0    failed=0
```

- [Demo playbook looping over hashes](looping-over-hashes-example.yml)
```sh
$ ansible-playbook looping-over-hashes-example.yml -vv
```
**Output:**
```sh
PLAY [Looping over Hashes Example] *********************************************

TASK [setup] *******************************************************************
ok: [localhost]

TASK [Print phone records] *****************************************************
task path: /home/vagrant/ansible-examples/loops/looping-over-hashes-example.yml:14
ok: [localhost] => (item={'key': u'alice', 'value': {u'name': u'Alice Appleworth', u'telephone': u'123-456-7890'}}) => {
    "item": {
        "key": "alice",
        "value": {
            "name": "Alice Appleworth",
            "telephone": "123-456-7890"
        }
    },
    "msg": "User alice is Alice Appleworth (123-456-7890)"
}
ok: [localhost] => (item={'key': u'bob', 'value': {u'name': u'Bob Bananarama', u'telephone': u'987-654-3210'}}) => {
    "item": {
        "key": "bob",
        "value": {
            "name": "Bob Bananarama",
            "telephone": "987-654-3210"
        }
    },
    "msg": "User bob is Bob Bananarama (987-654-3210)"
}

PLAY RECAP *********************************************************************
localhost                  : ok=2    changed=0    unreachable=0    failed=0
```

- [Demo playbook looping over files](looping-over-files-example.yml)
```sh
$ ansible-playbook looping-over-files-example.yml -vv
```
**Output:**
```sh
PLAY [Looping over Files Example] **********************************************

TASK [setup] *******************************************************************
ok: [localhost]

TASK [Print content of each file] **********************************************
task path: /home/vagrant/ansible-examples/loops/looping-over-files-example.yml:5
ok: [localhost] => (item=This is content of second file) => {
    "item": "This is content of second file",
    "msg": "This is content of second file"
}
ok: [localhost] => (item=This is content of first file) => {
    "item": "This is content of first file",
    "msg": "This is content of first file"
}

PLAY RECAP *********************************************************************
localhost                  : ok=2    changed=0    unreachable=0    failed=0
```
- [Demo playbook looping over fileglobs](looping-over-fileglobs-example.yml)
```sh
$ ansible-playbook looping-over-fileglobs-example.yml -vv 
```
**Output:**
```sh
PLAY [Looping over Fileglobs Example] ******************************************

TASK [setup] *******************************************************************
ok: [localhost]

TASK [Show full path to each file in folder] ***********************************
task path: /home/vagrant/ansible-examples/loops/looping-over-fileglobs-example.yml:5
ok: [localhost] => (item=/home/vagrant/ansible-examples/loops/files/second_file) => {
    "item": "/home/vagrant/ansible-examples/loops/files/second_file",
    "msg": "/home/vagrant/ansible-examples/loops/files/second_file"
}
ok: [localhost] => (item=/home/vagrant/ansible-examples/loops/files/third_file) => {
    "item": "/home/vagrant/ansible-examples/loops/files/third_file",
    "msg": "/home/vagrant/ansible-examples/loops/files/third_file"
}
ok: [localhost] => (item=/home/vagrant/ansible-examples/loops/files/first_file) => {
    "item": "/home/vagrant/ansible-examples/loops/files/first_file",
    "msg": "/home/vagrant/ansible-examples/loops/files/first_file"
}

PLAY RECAP *********************************************************************
localhost                  : ok=2    changed=0    unreachable=0    failed=0
```
- [Demo playbook looping-over parallel sets data](looping-over-parallel-sets-data-example.yml)
```sh
$ ansible-playbook looping-over-parallel-sets-data-example.yml -vv
```
**Output:**
```sh
PLAY [Looping over Parallel Sets of Data Example] ******************************

TASK [setup] *******************************************************************
ok: [localhost]

TASK [Print letters with appropriate numbers] **********************************
task path: /home/vagrant/ansible-examples/loops/looping-over-parallel-sets-data-example.yml:9
ok: [localhost] => (item=[u'd', 4]) => {
    "item": [
        "d",
        4
    ],
    "msg": "d and 4"
}
ok: [localhost] => (item=[u'c', 3]) => {
    "item": [
        "c",
        3
    ],
    "msg": "c and 3"
}
ok: [localhost] => (item=[u'b', 2]) => {
    "item": [
        "b",
        2
    ],
    "msg": "b and 2"
}
ok: [localhost] => (item=[u'a', 1]) => {
    "item": [
        "a",
        1
    ],
    "msg": "a and 1"
}

PLAY RECAP *********************************************************************
localhost                  : ok=2    changed=0    unreachable=0    failed=0
```
- [Demo playbook looping over subelements](looping-over-subelements-example.yml)
```sh
$ ansible-playbook looping-over-subelements-example.yml
```
**Output:**
```sh
PLAY [Looping over Subelements Example] ****************************************

TASK [setup] *******************************************************************
ok: [localhost]

TASK [Print users with appropriate file content] *******************************
ok: [localhost] => (item=({u'name': u'bob', u'properties': {u'password': [u'bob-789'], u'groups': [u'root', u'wheel']}}, u'files/second_file')) => {
    "item": [
        {
            "name": "bob",
            "properties": {
                "groups": [
                    "root",
                    "wheel"
                ],
                "password": [
                    "bob-789"
                ]
            }
        },
        "files/second_file"
    ],
    "msg": "User bob wrote 'This is content of second file' in file files/second_file"
}
ok: [localhost] => (item=({u'name': u'alice', u'properties': {u'password': [u'alice-123'], u'groups': [u'root', u'wheel']}}, u'files/first_file')) => {
    "item": [
        {
            "name": "alice",
            "properties": {
                "groups": [
                    "root",
                    "wheel"
                ],
                "password": [
                    "alice-123"
                ]
            }
        },
        "files/first_file"
    ],
    "msg": "User alice wrote 'This is content of first file' in file files/first_file"
}

TASK [Print users with appropriate properties] *********************************
ok: [localhost] => (item=({u'files': [u'files/second_file'], u'name': u'bob', u'properties': {u'groups': [u'root', u'wheel']}}, u'bob-789')) => {
    "item": [
        {
            "files": [
                "files/second_file"
            ],
            "name": "bob",
            "properties": {
                "groups": [
                    "root",
                    "wheel"
                ]
            }
        },
        "bob-789"
    ],
    "msg": "User bob is in groups root,wheel and has password bob-789"
}
ok: [localhost] => (item=({u'files': [u'files/first_file'], u'name': u'alice', u'properties': {u'groups': [u'root', u'wheel']}}, u'alice-123')) => {
    "item": [
        {
            "files": [
                "files/first_file"
            ],
            "name": "alice",
            "properties": {
                "groups": [
                    "root",
                    "wheel"
                ]
            }
        },
        "alice-123"
    ],
    "msg": "User alice is in groups root,wheel and has password alice-123"
}

PLAY RECAP *********************************************************************
localhost                  : ok=3    changed=0    unreachable=0    failed=0
```
- [Demo playbook looping over integer sequences](looping-over-integer-sequences-example.yml)
```sh
$ ansible-playbook looping-over-integer-sequences-example.yml -vv
```
**Output:**
```sh
PLAY [Looping over Integer Sequences Example] **********************************

TASK [setup] *******************************************************************
ok: [localhost]

TASK [Print even numbers from 0 to 10 in format "number-X"] ********************
task path: /home/vagrant/ansible-examples/loops/looping-over-integer-sequences-example.yml:5
ok: [localhost] => (item=number-8) => {
    "item": "number-8",
    "msg": "number-8"
}
ok: [localhost] => (item=number-6) => {
    "item": "number-6",
    "msg": "number-6"
}
ok: [localhost] => (item=number-4) => {
    "item": "number-4",
    "msg": "number-4"
}
ok: [localhost] => (item=number-2) => {
    "item": "number-2",
    "msg": "number-2"
}
ok: [localhost] => (item=number-0) => {
    "item": "number-0",
    "msg": "number-0"
}
ok: [localhost] => (item=number-16) => {
    "item": "number-16",
    "msg": "number-16"
}
ok: [localhost] => (item=number-14) => {
    "item": "number-14",
    "msg": "number-14"
}
ok: [localhost] => (item=number-12) => {
    "item": "number-12",
    "msg": "number-12"
}
ok: [localhost] => (item=number-10) => {
    "item": "number-10",
    "msg": "number-10"
}

TASK [Print numbers from 1 to 3] ***********************************************
task path: /home/vagrant/ansible-examples/loops/looping-over-integer-sequences-example.yml:9
ok: [localhost] => (item=3) => {
    "item": "3",
    "msg": "3"
}
ok: [localhost] => (item=2) => {
    "item": "2",
    "msg": "2"
}
ok: [localhost] => (item=1) => {
    "item": "1",
    "msg": "1"
}

PLAY RECAP *********************************************************************
localhost                  : ok=3    changed=0    unreachable=0    failed=0
```
- [Demo playbook random choices](random-choices-example.yml)
```sh
$ ansible-playbook random-choices-example.yml -vv
```
**Output:**
```sh
PLAY [Random Choices Example] **************************************************

TASK [setup] *******************************************************************
ok: [localhost]

TASK [Print random phrase"] ****************************************************
task path: /home/vagrant/ansible-examples/loops/random-choices-example.yml:5
ok: [localhost] => (item=drink from the goblet) => {
    "item": "drink from the goblet",
    "msg": "drink from the goblet"
}

PLAY RECAP *********************************************************************
localhost                  : ok=2    changed=0    unreachable=0    failed=0
```

**Output (second time):**
```sh
PLAY [Random Choices Example] **************************************************

TASK [setup] *******************************************************************
ok: [localhost]

TASK [Print random phrase"] ****************************************************
task path: /home/vagrant/ansible-examples/loops/random-choices-example.yml:5
ok: [localhost] => (item=go through the door) => {
    "item": "go through the door",
    "msg": "go through the door"
}

PLAY RECAP *********************************************************************
localhost                  : ok=2    changed=0    unreachable=0    failed=0
```
- [Demo playbook iterating-over-result](iterating-over-result-example.yml)
```sh
$ ansible-playbook iterating-over-result-example.yml -vv 
```
**Output:**
```sh
PLAY [Iterating Over The Results of a Program Execution Example] ***************

TASK [setup] *******************************************************************
ok: [localhost]

TASK [Show result of 'cat files/third_file' row by row] ************************
task path: /home/vagrant/ansible-examples/loops/iterating-over-result-example.yml:5
changed: [localhost] => (item=line 1) => {"changed": true, "cmd": "echo line 1", "delta": "0:00:00.002682", "end": "2017-06-08 12:43:45.635561", "item": "line 1", "rc": 0, "start": "2017-06-08 12:43:45.632879", "stderr": "", "stdout": "line 1", "stdout_lines": ["line 1"], "warnings": []}
changed: [localhost] => (item=line 2) => {"changed": true, "cmd": "echo line 2", "delta": "0:00:00.002423", "end": "2017-06-08 12:43:45.747711", "item": "line 2", "rc": 0, "start": "2017-06-08 12:43:45.745288", "stderr": "", "stdout": "line 2", "stdout_lines": ["line 2"], "warnings": []}
changed: [localhost] => (item=line 3) => {"changed": true, "cmd": "echo line 3", "delta": "0:00:00.002779", "end": "2017-06-08 12:43:45.843368", "item": "line 3", "rc": 0, "start": "2017-06-08 12:43:45.840589", "stderr": "", "stdout": "line 3", "stdout_lines": ["line 3"], "warnings": []}
changed: [localhost] => (item=) => {"changed": true, "cmd": "echo ", "delta": "0:00:00.002672", "end": "2017-06-08 12:43:45.942876", "item": "", "rc": 0, "start": "2017-06-08 12:43:45.940204", "stderr": "", "stdout": "", "stdout_lines": [], "warnings": []}

TASK [debug] *******************************************************************
task path: /home/vagrant/ansible-examples/loops/iterating-over-result-example.yml:11
ok: [localhost] => {
    "result": {
        "changed": true,
        "msg": "All items completed",
        "results": [
            {
                "_ansible_item_result": true,
                "_ansible_no_log": false,
                "_ansible_parsed": true,
                "changed": true,
                "cmd": "echo line 1",
                "delta": "0:00:00.002682",
                "end": "2017-06-08 12:43:45.635561",
                "invocation": {
                    "module_args": {
                        "_raw_params": "echo line 1",
                        "_uses_shell": true,
                        "chdir": null,
                        "creates": null,
                        "executable": null,
                        "removes": null,
                        "warn": true
                    },
                    "module_name": "command"
                },
                "item": "line 1",
                "rc": 0,
                "start": "2017-06-08 12:43:45.632879",
                "stderr": "",
                "stdout": "line 1",
                "stdout_lines": [
                    "line 1"
                ],
                "warnings": []
            },
            {
                "_ansible_item_result": true,
                "_ansible_no_log": false,
                "_ansible_parsed": true,
                "changed": true,
                "cmd": "echo line 2",
                "delta": "0:00:00.002423",
                "end": "2017-06-08 12:43:45.747711",
                "invocation": {
                    "module_args": {
                        "_raw_params": "echo line 2",
                        "_uses_shell": true,
                        "chdir": null,
                        "creates": null,
                        "executable": null,
                        "removes": null,
                        "warn": true
                    },
                    "module_name": "command"
                },
                "item": "line 2",
                "rc": 0,
                "start": "2017-06-08 12:43:45.745288",
                "stderr": "",
                "stdout": "line 2",
                "stdout_lines": [
                    "line 2"
                ],
                "warnings": []
            },
            {
                "_ansible_item_result": true,
                "_ansible_no_log": false,
                "_ansible_parsed": true,
                "changed": true,
                "cmd": "echo line 3",
                "delta": "0:00:00.002779",
                "end": "2017-06-08 12:43:45.843368",
                "invocation": {
                    "module_args": {
                        "_raw_params": "echo line 3",
                        "_uses_shell": true,
                        "chdir": null,
                        "creates": null,
                        "executable": null,
                        "removes": null,
                        "warn": true
                    },
                    "module_name": "command"
                },
                "item": "line 3",
                "rc": 0,
                "start": "2017-06-08 12:43:45.840589",
                "stderr": "",
                "stdout": "line 3",
                "stdout_lines": [
                    "line 3"
                ],
                "warnings": []
            },
            {
                "_ansible_item_result": true,
                "_ansible_no_log": false,
                "_ansible_parsed": true,
                "changed": true,
                "cmd": "echo ",
                "delta": "0:00:00.002672",
                "end": "2017-06-08 12:43:45.942876",
                "invocation": {
                    "module_args": {
                        "_raw_params": "echo ",
                        "_uses_shell": true,
                        "chdir": null,
                        "creates": null,
                        "executable": null,
                        "removes": null,
                        "warn": true
                    },
                    "module_name": "command"
                },
                "item": "",
                "rc": 0,
                "start": "2017-06-08 12:43:45.940204",
                "stderr": "",
                "stdout": "",
                "stdout_lines": [],
                "warnings": []
            }
        ]
    }
}

PLAY RECAP *********************************************************************
localhost                  : ok=3    changed=1    unreachable=0    failed=0
```


- [Demo playbook of using register with a loop](looping-with-register.yml)
```sh
$ ansible-playbook looping-with-register.yml
```
**Output:**
```sh
PLAY [localhost] ***************************************************************

TASK [Gathering Facts] *********************************************************
ok: [localhost]

TASK [debug] *******************************************************************
ok: [localhost] => (item=one) => {
    "changed": false,
    "item": "one"
}
ok: [localhost] => (item=two) => {
    "changed": false,
    "item": "two"
}

TASK [debug] *******************************************************************
ok: [localhost] => {
    "looprg": {
        "changed": false,
        "msg": "All items completed",
        "results": [
            {
                "_ansible_ignore_errors": null,
                "_ansible_item_result": true,
                "_ansible_no_log": false,
                "_ansible_verbose_always": true,
                "changed": false,
                "failed": false,
                "item": "one"
            },
            {
                "_ansible_ignore_errors": null,
                "_ansible_item_result": true,
                "_ansible_no_log": false,
                "_ansible_verbose_always": true,
                "changed": false,
                "failed": false,
                "item": "two"
            }
        ]
    }
}

PLAY RECAP ********************************************************************
localhost                  : ok=3    changed=0    unreachable=0    failed=0
```

- [Demo playbook of do-until loop](loop-do-until.yml)
```sh
$ ansible-playbook loop-do-until.yml
```
**Output:**
```sh
PLAY [localhost] ***************************************************************

TASK [Gathering Facts] *********************************************************
ok: [localhost]

TASK [command] *****************************************************************
changed: [localhost] => {"changed": true, "cmd": "sleep 10 &", "delta": "0:00:01.011679", "end": "2018-03-13 21:54:10.539652", "rc": 0, "start": "2018-03-13 21:54:09.527973", "stderr": "", "stderr_lines": [], "stdout": "", "stdout_lines": []}

TASK [command] *****************************************************************
FAILED - RETRYING: command (11 retries left).
FAILED - RETRYING: command (10 retries left).
FAILED - RETRYING: command (9 retries left).
FAILED - RETRYING: command (8 retries left).
FAILED - RETRYING: command (7 retries left).
FAILED - RETRYING: command (6 retries left).
FAILED - RETRYING: command (5 retries left).
changed: [localhost] => {"attempts": 8, "changed": true, "cmd": "ps -ef | grep 'sleep 10' | grep -v grep || echo", "delta": "0:00:00.070893", "end": "2018-03-13 21:54:20.163543", "rc": 0, "start": "2018-03-13 21:54:20.092650", "stderr": "", "stderr_lines": [], "stdout": "", "stdout_lines": []}

PLAY RECAP *********************************************************************
localhost                  : ok=3    changed=2    unreachable=0    failed=0
```