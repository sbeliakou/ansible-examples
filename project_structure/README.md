# Ansible project structure and role dependencies example

## Resources:
- [Ansible Docs](http://docs.ansible.com/ansible/playbooks_best_practices.html#directory-layout)
- [Role Dependencies](http://docs.ansible.com/ansible/playbooks_roles.html#role-dependencies)
- [Role Dependencies Example](roles/common/meta/main.yml)

## Examples:

**Project structure look something like this:**
 ```sh
.
├── common.yml
├── dbservers.yml
├── filter_plugins/
│   └── some_plugin
├── inventories/
│   ├── production/
│   │   ├── group_vars/
│   │   │   ├── all
│   │   │   ├── atlanta
│   │   │   └── webservers
│   │   ├── hosts
│   │   └── host_vars/
│   │       └── db-bos-1.example.com
│   └── staging/
│       ├── group_vars/
│       │   ├── group1
│       │   └── group2
│       ├── hosts
│       └── host_vars/
│           ├── stagehost1
│           └── stagehost2
├── library/
│   └── some_module
├── README.md
├── roles/
│   ├── common/
│   │   ├── defaults/
│   │   │   └── main.yml
│   │   ├── files/
│   │   ├── handlers/
│   │   │   └── main.yml
│   │   ├── meta/
│   │   │   └── main.yml
│   │   ├── README.md
│   │   ├── tasks/
│   │   │   └── main.yml
│   │   ├── templates/
│   │   ├── tests/
│   │   │   ├── inventory
│   │   │   └── test.yml
│   │   └── vars/
│   │       └── main.yml
│   ├── dbserver/
│   │   ├── defaults/
│   │   │   └── main.yml
│   │   ├── files/
│   │   ├── handlers/
│   │   │   └── main.yml
│   │   ├── meta/
│   │   │   └── main.yml
│   │   ├── README.md
│   │   ├── tasks/
│   │   │   └── main.yml
│   │   ├── templates/
│   │   ├── tests/
│   │   │   ├── inventory
│   │   │   └── test.yml
│   │   └── vars/
│   │       └── main.yml
│   └── webserver/
│       ├── defaults/
│       │   └── main.yml
│       ├── files/
│       ├── handlers/
│       │   └── main.yml
│       ├── meta/
│       │   └── main.yml
│       ├── README.md
│       ├── tasks/
│       │   └── main.yml
│       ├── templates/
│       ├── tests/
│       │   ├── inventory
│       │   └── test.yml
│       └── vars/
│           └── main.yml
├── site.yml
└── webservers.yml
```
**Use ```“--limit”``` parameter to ansible for running only certain subsets of site.yml:**
 ```sh
$ ansible-playbook site.yml --limit webservers
```
equal to:
```sh
$ ansible-playbook webservers.yml
```
