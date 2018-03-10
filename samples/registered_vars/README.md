# Registered vars / set_fact
[http://docs.ansible.com/ansible/playbooks_variables.html#registered-variables]

Example playbook
```
$ ansible-playbook playbook.yml
```
```
PLAY ***************************************************************************

TASK [setup] *******************************************************************
ok: [localhost]

TASK [Shell step 'cat playbook.yml'. Output is registered to result variable] **
changed: [localhost]

TASK [Registering custom fact from the formatted result variable] **************
ok: [localhost]

TASK [Output of result.stdout] *************************************************
ok: [localhost] => {
    "result.stdout": "- hosts: localhost\n  connection: local\n  tasks:\n    - name: \"Shell step 'cat playbook.yml'. Output is registered to result variable\"\n      shell: cat playbook.yml\n      register: result\n    - name: \"Registering custom fact from the formatted result variable\"\n      set_fact: from_yaml=\"{# result.stdout | from_yaml #}\"\n    - name: \"Output of result.stdout\"\n      debug: var=result.stdout\n    - name: \"Output of the custom fact\"\n      debug: var=from_yaml"
}

TASK [Output of the custom fact] ***********************************************
ok: [localhost] => {
    "from_yaml": [
        {
            "connection": "local", 
            "hosts": "localhost", 
            "tasks": [
                {
                    "name": "Shell step 'cat playbook.yml'. Output is registered to result variable", 
                    "register": "result", 
                    "shell": "cat playbook.yml"
                }, 
                {
                    "name": "Registering custom fact from the formatted result variable", 
                    "set_fact": "from_yaml=\"{# result.stdout | from_yaml"
                }, 
                {
                    "debug": "var=result.stdout", 
                    "name": "Output of result.stdout"
                }, 
                {
                    "debug": "var=from_yaml", 
                    "name": "Output of the custom fact"
                }
            ]
        }
    ]
}

PLAY RECAP *********************************************************************
localhost                  : ok=5    changed=1    unreachable=0    failed=0   

```
