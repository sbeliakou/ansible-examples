# Strategies

[http://docs.ansible.com/ansible/playbooks_strategies.html]

Example contents:
- [demo playbook](strategy_example.yml)
- [sample inventory](inventory)

To run this example you should add a couple of hosts to the inventory
and configure connectivity between ansible host and these hosts.

Example of a linear strategy (default):
```sh
strategy:linear
```
```sh
$ ansible-playbook strategy_example.yml -i inventory
```
```sh
PLAY ***************************************************************************

TASK [setup] *******************************************************************
ok: [localhost]
ok: [35.184.194.164]
ok: [35.184.156.100]

TASK [First step] **************************************************************
ok: [localhost] => {
    "msg": "Step 1. Something is done here"
}
ok: [35.184.194.164] => {
    "msg": "Step 1. Something is done here"
}
ok: [35.184.156.100] => {
    "msg": "Step 1. Something is done here"
}

TASK [Second step] *************************************************************
ok: [localhost] => {
    "msg": "Step 2. Something is done here"
}
ok: [35.184.194.164] => {
    "msg": "Step 2. Something is done here"
}
ok: [35.184.156.100] => {
    "msg": "Step 2. Something is done here"
}

TASK [Third step] **************************************************************
ok: [localhost] => {
    "msg": "Step 3. Something is done here"
}
ok: [35.184.194.164] => {
    "msg": "Step 3. Something is done here"
}
ok: [35.184.156.100] => {
    "msg": "Step 3. Something is done here"
}

PLAY RECAP *********************************************************************
35.184.156.100             : ok=4    changed=0    unreachable=0    failed=0   
35.184.194.164             : ok=4    changed=0    unreachable=0    failed=0   
localhost                  : ok=4    changed=0    unreachable=0    failed=0   

```

Example of a free strategy, which allows each host to run until the end
 of the play as fast as it can.
```sh
strategy:free
```
```sh
$ ansible-playbook strategy_example.yml -i inventory
```
```sh
PLAY ***************************************************************************

TASK [setup] *******************************************************************

TASK [setup] *******************************************************************

TASK [setup] *******************************************************************
ok: [localhost]

TASK [First step] **************************************************************
ok: [localhost] => {
    "msg": "Step 1. Something is done here"
}

TASK [Second step] *************************************************************
ok: [localhost] => {
    "msg": "Step 2. Something is done here"
}

TASK [Third step] **************************************************************
ok: [localhost] => {
    "msg": "Step 3. Something is done here"
}
ok: [35.184.194.164]
ok: [35.184.156.100]

TASK [First step] **************************************************************

TASK [First step] **************************************************************
ok: [35.184.194.164] => {
    "msg": "Step 1. Something is done here"
}
ok: [35.184.156.100] => {
    "msg": "Step 1. Something is done here"
}

TASK [Second step] *************************************************************

TASK [Second step] *************************************************************
ok: [35.184.194.164] => {
    "msg": "Step 2. Something is done here"
}
ok: [35.184.156.100] => {
    "msg": "Step 2. Something is done here"
}

TASK [Third step] **************************************************************

TASK [Third step] **************************************************************
ok: [35.184.156.100] => {
    "msg": "Step 3. Something is done here"
}
ok: [35.184.194.164] => {
    "msg": "Step 3. Something is done here"
}

PLAY RECAP *********************************************************************
35.184.156.100             : ok=4    changed=0    unreachable=0    failed=0   
35.184.194.164             : ok=4    changed=0    unreachable=0    failed=0   
localhost                  : ok=4    changed=0    unreachable=0    failed=0   

```
