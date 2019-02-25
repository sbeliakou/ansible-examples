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
       8:   - command: echo hello world
 ->    9:
      10:   - name: trailing whitespace
      11:     command: echo do nothing


    [E301] Commands should not change things if nothing needs doing
    Commands should either read information (and thus set changed_when) or not do something if it has already been done (using creates/removes) or only do it if another check has a particular result (when)

    [E502] All tasks should be named
    All tasks should have a distinct name for readability and for --start-at-task to work
...
```

```bash
$ alias ansible-check='docker run -v $(pwd):/opt/work sbeliakou/ansible-check:3.5.1'
$ ansible-check play.yml
play.yml:5:
       3:   tasks:
       4:   - name: a bad play
 ->    5:     shell: service blah restart
       6:     sudo: yes


    [E103] Deprecated sudo
    Instead of sudo/sudo_user, use become/become_user.

    [E301] Commands should not change things if nothing needs doing
    Commands should either read information (and thus set changed_when) or not do something if it has already been done (using creates/removes) or only do it if another check has a particular result (when)

    [E303] service used in place of service module
    Executing a command when there is an Ansible module is generally a bad idea

    [E305] Use shell only when shell functionality is required
    Shell should only be used when piping, redirecting or chaining commands (and Ansible would be preferred for some of those!)

```
