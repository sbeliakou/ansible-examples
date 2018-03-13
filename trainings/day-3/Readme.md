## Environement Configuration
- [Vargantfile](Vagrantfile)
- [Ansible Inventory File](inventory)
- [Ansible Configuration File](ansible.cfg)

## Change Log

- [X] Introducing Custom Filter: MongoDB SRC URL selector
- [X] Introducing Custom Filter: Corporate Email Composer
- [ ] Introducing Custom Module: Vagrant management (python, bash)
- [ ] Introducing Role Tomcat WAR Deployment
- [ ] Introducing Playbook to Spin up Environment, Install Tomcat Server, Deploy WAR file
- [ ] Introducing add_host Module

## Cheat sheet
```
# Start Local Engineering Environment
$ vagrant up

# Figure out what Mongo Archive will be downloaded
$ ansible-playbook tasks/mongodb_selector_filter/mongodb_url_select.yml

# Generate a List of emails by Users List
$ ansible-playbook tasks/corporate_emails/corporate_email.yml

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