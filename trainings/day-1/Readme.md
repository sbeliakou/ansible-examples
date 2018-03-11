## Rollout Local Engineering Environment

```
$ vagrant up
```

## Inventory Files

### [inventory01](inventory01)
Simplest configuration.
We need to pass all connection settings in ansible-playbook command-line arguments

```
$ ansible-playbook playbook -i inventory01 -c paramiko -u vagrant --ask-pass
$ ansible-playbook playbook -i inventory01 -c paramiko -u vagrant --private-key=~/.vagrant.d/insecure_private_key
```

### [inventory02](inventory02)
Added connection settings, ansible-playbook command gets simpler

```
$ ansible-playbook playbook -i inventory02
```

### [inventory03](inventory03)
Added aliases to actual hosts, it could help with troubleshooting

```
$ ansible-playbook playbook -i inventory03
```

## Tasks

### [Deploy Nginx](tasks/1.yml)

**Task**: 

> Deploy the latest version of Nginx on the server

```
$ ansible-playbook tasks/1.yml -i inventory03 -vv
```

### [Deploy Tomcat](tasks/2.yml)

**Task**: 

> Install Web Application Server Toolkit:
> \- Java v1.7.x
> \- Tomcat v7.x
> \- Tomcat webapps

```
$ ansible-playbook tasks/2.yml -i inventory03 -vv
```


### [Deploy Tomcat from Sources](tasks/3.yml)

**Task**: 

> Install Web Application Server Toolkit:
> \- Java v1.7.x
> \- Tomcat User/Group
> \- Tomcat Home Folder (where binaries will be installed into)
> \- Tomcat v7.x
> \- Tomcat Systemd Service File

```
$ ansible-playbook tasks/3.yml -i inventory03 -vv
```