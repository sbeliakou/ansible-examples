# Templates/jinja2

[http://docs.ansible.com/ansible/template_module.html#template-templates-a-file-out-to-a-remote-server]


- [demo playbook](vhost.yml)
- [virtual host template](templates/virtual-host.conf.j2)
- [generated config](templates/virtual-host.conf)

```sh
$ ansible-playbook vhost.yml
```

```sh
PLAY ***************************************************************************

TASK [setup] *******************************************************************
ok: [localhost]

TASK [Generating virtual hosts config] *****************************************
changed: [localhost]

PLAY RECAP *********************************************************************
localhost                  : ok=2    changed=1    unreachable=0    failed=0   
```

Generated virtual hosts config:
```sh
<VirtualHost *:80>
  ServerName www.domain.com
  DocumentRoot /www/domain_com
  <Directory "/www/domain_com">
    AllowOverride All
    Options -Indexes FollowSymLinks
    Order allow,deny
    Allow from all
  </Directory>
</VirtualHost>

<VirtualHost *:80>
  ServerName www.domain.by
  DocumentRoot /www/domain_by
  ServerAdmin webmaster@domain.by
  <Directory "/www/domain_by">
    AllowOverride All
    Options -Indexes FollowSymLinks
    Order allow,deny
    Allow from all
  </Directory>
</VirtualHost>
```
