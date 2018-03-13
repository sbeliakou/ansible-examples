## 1. Rollout Local Engineering Environment

```
# Start Local Engineering Environment
$ vagrant up

# Provision Nginx Example
$ ansible-playbook tasks/11.yml -i inventory03 -v

# Provision Tomcat (from YUM Repo) Example
$ ansible-playbook tasks/12.yml -i inventory03 -v

# Provision Tomcat (from SRC) Example
$ ansible-playbook tasks/13.yml -i inventory03 -v

# Stop VM
$ vagrant halt

# Destroy VM
$ vagrant destroy -f
```

## 2. Inventory File
Ansible works against multiple systems in your infrastructure at the same time. It does this by selecting portions of systems listed in Ansible’s inventory, which defaults to being saved in the location /etc/ansible/hosts. You can specify a different inventory file using the -i <path> option on the command line.

[Ansible Documentation](http://docs.ansible.com/ansible/latest/intro_inventory.html)

### 2.1. [inventory01](inventory01)
> Simplest configuration.
> We need to pass all connection settings in ansible-playbook command-line arguments

```
$ ansible-playbook playbook -i inventory01 -c paramiko -u vagrant --ask-pass
$ ansible-playbook playbook -i inventory01 -c paramiko -u vagrant --private-key=~/.vagrant.d/insecure_private_key
```

### 2.2. [inventory02](inventory02)
> Added connection settings, ansible-playbook command gets simpler

```
$ ansible-playbook playbook -i inventory02
```

### 2.3. [inventory03](inventory03)
> Added aliases to actual hosts, it could help with troubleshooting

```
$ ansible-playbook playbook -i inventory03
```

## 3. Sample Playbooks

1. Deploying [Nginx](tasks/11.yml) + Sanity Tests
2. Deploying [Tomcat (yum repo)](tasks/12.yml) + Sanity Tests
3. Deploying [Tomcat (from sources)](tasks/13.yml) + Sanity Tests

## 4. Ansible [Configuration File](ansible.cfg)
Certain settings in Ansible are adjustable via a configuration file.
[Here](ansible.cfg)'s a basic (widely used) settings. Complete list of possible settings can be found [here](https://raw.githubusercontent.com/ansible/ansible/devel/examples/ansible.cfg)

1. [Disabling SSH key host checking](ansible.cfg#L4)
2. [Displaying module arguments into stdout](ansible.cfg#L15)
3. [Disabling creating *.retry files](ansible.cfg#L21)