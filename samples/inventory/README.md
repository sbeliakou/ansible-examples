# Inventory

[http://docs.ansible.com/ansible/intro_inventory.html]

Example contents:
- [demo playbook](inventory_example.yml)
- [sample inventory](inventory)

```sh
ansible-playbook inventory_example.yml -i inventory
```
```sh
PLAY [Play runs on hosts in atlanta group] *********************************************************************************************************************

TASK [Gathering Facts] *****************************************************************************************************************************************
ok: [atlanta-host]

TASK [Atlanta group] *******************************************************************************************************************************************
ok: [atlanta-host] => {
    "region": "atlanta"
}

PLAY [Play runs on hosts in raleigh group] *********************************************************************************************************************

TASK [Gathering Facts] *****************************************************************************************************************************************
ok: [raleigh-host]

TASK [Raleigh group] *******************************************************************************************************************************************
ok: [raleigh-host] => {
    "region": "raleigh"
}

PLAY [Play runs in southeast group that includes atlanta and raleigh] ******************************************************************************************

TASK [Gathering Facts] *****************************************************************************************************************************************
ok: [atlanta-host]
ok: [raleigh-host]

TASK [Southeast group] *****************************************************************************************************************************************
ok: [atlanta-host] => {
    "region": "atlanta"
}
ok: [raleigh-host] => {
    "region": "raleigh"
}

PLAY [Play runs in usa group that includes southeast] **********************************************************************************************************

TASK [Gathering Facts] *****************************************************************************************************************************************
ok: [atlanta-host]
ok: [raleigh-host]

TASK [USA group] ***********************************************************************************************************************************************
ok: [atlanta-host] => {
    "region": "atlanta"
}
ok: [raleigh-host] => {
    "region": "raleigh"
}

PLAY [dbservers:webservers] ************************************************************************************************************************************

TASK [Gathering Facts] *****************************************************************************************************************************************
ok: [web1]
ok: [db2]
ok: [db1]
ok: [web2]

TASK [task runs on dbservers or webservers] ********************************************************************************************************************
ok: [db1] => {
    "hostvars[inventory_hostname][\"ansible_fqdn\"]": "ubuntu-box"
}
ok: [db2] => {
    "hostvars[inventory_hostname][\"ansible_fqdn\"]": "ubuntu-box"
}
ok: [web1] => {
    "hostvars[inventory_hostname][\"ansible_fqdn\"]": "ubuntu-box"
}
ok: [web2] => {
    "hostvars[inventory_hostname][\"ansible_fqdn\"]": "ubuntu-box"
}

PLAY [dbservers:!backup] ***************************************************************************************************************************************

TASK [Gathering Facts] *****************************************************************************************************************************************
ok: [db1]

TASK [task runs on hosts that are in dbservers AND NOT in backup] **********************************************************************************************
ok: [db1] => {
    "hostvars[inventory_hostname]['ansible_fqdn']": "ubuntu-box"
}

PLAY [dbservers:webservers:!backup] ****************************************************************************************************************************

TASK [Gathering Facts] *****************************************************************************************************************************************
ok: [db1]
ok: [web1]

TASK [task runs on hosts that are in dbservers,webservers AND NOT in backup] ***********************************************************************************
ok: [db1] => {
    "hostvars[inventory_hostname].ansible_fqdn": "ubuntu-box"
}
ok: [web1] => {
    "hostvars[inventory_hostname].ansible_fqdn": "ubuntu-box"
}

PLAY [webservers:&backup] **************************************************************************************************************************************

TASK [Gathering Facts] *****************************************************************************************************************************************
ok: [web2]

TASK [task runs on hosts that are in webservers AND in backup] *************************************************************************************************
ok: [web2] => {
    "hostvars[inventory_hostname].ansible_fqdn": "ubuntu-box"
}

PLAY [webservers[0]:backup[-1]] ********************************************************************************************************************************

TASK [Gathering Facts] *****************************************************************************************************************************************
ok: [web1]
ok: [web2]

TASK [task runs on the first host in webservers and on the last host in backup] ********************************************************************************
ok: [web1] => {
    "hostvars[inventory_hostname].ansible_fqdn": "ubuntu-box"
}
ok: [web2] => {
    "hostvars[inventory_hostname].ansible_fqdn": "ubuntu-box"
}

PLAY RECAP *****************************************************************************************************************************************************
atlanta-host               : ok=6    changed=0    unreachable=0    failed=0   
db1                        : ok=6    changed=0    unreachable=0    failed=0   
db2                        : ok=2    changed=0    unreachable=0    failed=0   
raleigh-host               : ok=6    changed=0    unreachable=0    failed=0   
web1                       : ok=6    changed=0    unreachable=0    failed=0   
web2                       : ok=6    changed=0    unreachable=0    failed=0 
```
