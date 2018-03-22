## Change Log

- [X] Introducing Tags
- [X] Introducing Custom Callback Plugin
- [X] Introducing Blocks: Rescue Management and Error Handling
- [ ] Introducing Include* Directives


## Tags Examples
```
#List Playbook Tags:
$ ansible-playbook tasks/tags/vagrant.yml --list-tags
#Create VM, Provision VM, Deploy WAR, Destroy VM:
$ ansible-playbook tasks/tags/vagrant.yml -v -e @tasks/tags/deployment.json
#Create VM, Provision VM and Deploy WAR:
$ ansible-playbook tasks/tags/vagrant.yml -v -e @tasks/tags/deployment.json --skip-tags=cleanup
#Provision VM:
$ ansible-playbook tasks/tags/vagrant.yml -v -e @tasks/tags/deployment.json --tags=provision
#Deploy WAR (only):
$ ansible-playbook tasks/tags/vagrant.yml -v -e @tasks/tags/deployment.json --tags=deploy
#Destroy VM:
$ ansible-playbook tasks/tags/vagrant.yml -v -e @tasks/tags/deployment.json --tags=cleanup

# Rescue/Error Example
$ ansible-playbook tasks/blocks/rescue.yml -v

# Custom Callback Example
$ ANSIBLE_CONFIG=tasks/callback/ansible.cfg ansible-playbook tasks/callback/callback-test.yml -v
```