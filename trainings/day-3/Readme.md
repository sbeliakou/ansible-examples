## Environement Configuration
- [Vargantfile](Vagrantfile)
- [Ansible Inventory File](inventory)
- [Ansible Configuration File](ansible.cfg)

## Change Log

- [X] Introducing Custom Filter: MongoDB SRC URL selector
- [X] Introducing Custom Filter: Corporate Email Composer
- [ ] Introducing Custom Module: Vagrant management (python)
- [ ] Introducing Module Which Deploys WAR into Tomcat
- [ ] Introducing Playbook to Spin up Environment, Install Tomcat Server, Deploy WAR file
- [ ] Introducing add_host Module

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
$ ansible localhost -M tasks/custom_modules/library/ -m time_test_bash.sh
$ ansible localhost -M tasks/custom_modules/library/ -m simple_module_bash -a 'msg="hello from my module"'
$ ansible localhost -M tasks/custom_modules/library/ -m timetest
$ ansible localhost -M tasks/custom_modules/library/ -m simple_module -a 'msg="hello from my module"'

```

## Examples Specification

### 1. Custom Filter: MongoDB SRC URL selector
### 2. Custom Filter: Corporate Email Composer
### 3. Custom Module: Vagrant management (python, bash)
### 4. Role Tomcat WAR Deployment
### 5. Playbook to Spin up Environment, Install Tomcat Server, Deploy WAR file