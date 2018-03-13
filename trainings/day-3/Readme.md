## Environement Configuration
- [Vargantfile](Vagrantfile)
- [Ansible Inventory File](inventory)
- [Ansible Configuration File](ansible.cfg)

## Change Log

- Introducing vars_files directive
- Introducing Custom Filter: MongoDB SRC URL selector
- Introducing Custom Filter: Corporate Email Composer
- Introducing Custom Module: Vagrant management (python, bash)
- Introducing Role Tomcat WAR Deployment
- Introducing Playbook to Spin up Environment, Install Tomcat Server, Deploy WAR file
- Introducing add_host Module

## Cheat sheet
```
# Start Local Engineering Environment
$ vagrant up

TBD

# Stop VM
$ vagrant halt

# Destroy VM
$ vagrant destroy -f
```

## Examples Specification

### 1. Custom Filter: MongoDB SRC URL selector
### 2. Custom Filter: Corporate Email Composer
### 3. Custom Module: Vagrant management (python, bash)
### 4. Role Tomcat WAR Deployment
### 5. Playbook to Spin up Environment, Install Tomcat Server, Deploy WAR file