## Checking Ansible playbooks with Ansible Lint

### Ansible Lint:
- [ansible-lint on github](https://github.com/ansible/ansible-lint)
- [ansible-lint on docs.ansible.com](https://docs.ansible.com/ansible-lint/)
- [default rules description](https://docs.ansible.com/ansible-lint/rules/default_rules.html)

### Usage:
```bash
$ docker run -v $(pwd):/opt/work sbeliakou/ansible-check:3.5.1 example.yml
example.yml:9:
       7:   tasks:
       8:   - name: unset variable
 ->    9:     action: command echo {{thisvariable}} is not set in this playbook
      10:
      11:   - name: trailing whitespace


    [E301] Commands should not change things if nothing needs doing
    Commands should either read information (and thus set changed_when) or not do something if it has already been done (using creates/removes) or only do it if another check has a particular result (when)

example.yml:12:
      10:
      11:   - name: trailing whitespace
 ->   12:     action: command echo do nothing
      13:
      14:   - name: git check


    [E301] Commands should not change things if nothing needs doing
    Commands should either read information (and thus set changed_when) or not do something if it has already been done (using creates/removes) or only do it if another check has a particular result (when)
...
```

```bash
$ alias ansible-check='docker run -v $(pwd):/opt/work sbeliakou/ansible-check:3.5.1'
$ ansible-check play.yml
play.yml:5:
       3:   tasks:
       4:   - name: a bad play
 ->    5:     action: command service blah restart


    [E301] Commands should not change things if nothing needs doing
    Commands should either read information (and thus set changed_when) or not do something if it has already been done (using creates/removes) or only do it if another check has a particular result (when)

    [E303] service used in place of service module
    Executing a command when there is an Ansible module is generally a bad idea

```