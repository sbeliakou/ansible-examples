## Environement Configuration
- [Vargantfile](Vagrantfile)
- [Ansible Inventory File](inventory)
- [Ansible Configuration File](ansible.cfg)

## Change Log

- [X] Introducing Custom Filter: MongoDB SRC URL selector
- [X] Introducing Custom Filter: Corporate Email Composer
- [X] Introducing Custom Module: Vagrant management (python)
- [X] Introducing Module Tomcat WAR Deployment
- [X] Introducing Playbook to Spin up Environment, Install Tomcat Server, Deploy WAR file
- [X] Introducing add_host Module
- [X] Introducing Dynamic Inventory Script
- [X] Ansible config file contains reference to the folder with custom modules. It simplifies operations, don't need to add `-M path/` or set `ANSIBLE_LIBRARY` env variable

## Cheat sheet
```
# Start Local Engineering Environment
$ vagrant up

# Figure out what Mongo Archive will be downloaded
$ ansible-playbook tasks/mongodb_selector_filter/mongodb_url_select.yml

# Stop VM
$ vagrant halt

# Destroy VM
$ vagrant destroy -f

# Generate a List of emails by Users List
$ ansible-playbook tasks/corporate_emails/corporate_email.yml

# Testing Modules
$ ansible localhost -m custom_module_bash.sh
$ ansible localhost -m custom_module_args_bash -a 'msg="hello from my bash module"'
$ ansible localhost -m custom_module_python
$ ansible localhost -m custom_module_args_python -a 'msg="hello from my python module"'

# Testing Modules in Playbook
$ ansible-playbook tasks/custom_modules/testing_modules.yml -v

# Tomcat Stack
$ ansible-playbook tasks/vagrant_management/vagrant.yml -v \
  -e vagrantfile=./ \
  -e @tasks/vagrant_management/deployment.json \
  -e application_war=$(pwd)/sample.war

```

## Examples Specification

### 1. Custom Filter: MongoDB SRC URL selector
### 2. Custom Filter: Corporate Email Composer
### 3. Custom Module: Vagrant management (python, bash)
### 4. Module Tomcat WAR Deployment
### 5. Playbook to Spin up Environment, Install Tomcat Server, Deploy WAR file