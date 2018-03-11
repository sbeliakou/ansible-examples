## Change Log

- Introducing roles: Nginx, Java, Tomcat
- Introducing handlers (in roles)
- Introducing Facts usage
- Introducing Registered Variables
- Inventory file becomes more clean
- Ansible config file contains reference to the project inventory file (to be used by default). It simplifies operations: just `ansible-playbook playbook.yml -v` enough now.

## Cheat sheet
```
# Start Local Engineering Environment
$ vagrant up

# Provision Nginx Example
$ ansible-playbook tasks/21.yml -v

# Provision Java Example
$ ansible-playbook tasks/22.yml -v

# Provision Tomcat Example
$ ansible-playbook tasks/23.yml -v

# Explore Installed Software and Configuration 
$ ansible app -m setup -a 'filter=ansible_local'

# Stop VM
$ vagrant halt

# Destroy VM
$ vagrant destroy -f
```