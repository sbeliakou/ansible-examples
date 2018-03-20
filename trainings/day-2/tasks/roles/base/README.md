Base Role
=========

The role can be used for provisioning common system configuration:
- EPEL Repository
- Python PIP Utility
- Useful Python packages: requests
- Ans to enable Ansible Facts.d directory

Requirements
------------

The role has no requiremens

Role Variables
--------------

```
pip_packages:
  - requests
```

Dependencies
------------

The role has no dependencies on other roles

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: base }

License
-------

BSD

Author Information
------------------

An optional section for the role authors to include contact information, or a website (HTML is not allowed).
