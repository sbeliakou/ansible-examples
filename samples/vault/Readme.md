## Prerequisites:
- Ansible v2.3.1 + 

## References:
- [Ansible Valut](http://docs.ansible.com/ansible/playbooks_vault.html)
- [Best Practices with Vault](http://docs.ansible.com/ansible/playbooks_best_practices.html#variables-and-vaults)

## How to Encrypt
- [Encrypting String Variable](#encrypting-string-variable)
- [Encrypting Vars File](#encrypting-vars-file)
- [Encrypting A File](#encrypting-a-file)

### Encrypting String Variable

```sh
$ ansible-vault encrypt_string "Hello world"
```
```sh
New Vault password:
Confirm New Vault password:
!vault |
          $ANSIBLE_VAULT;1.1;AES256
          30306233623163393464333438313935306637313761303935326131633961373030643164373936
          3034353464636161613432393763653530393066623738650a386462323663333962646231383666
          30333963333136633933626133386536643538633232363162636565303963633934303130303131
          3937303838633734630a653734623833666565363033306165383062346364313134346562636366
          6133
Encryption successful
```

### Encrypting Vars File

```sh
$ ansible-vault encrypt resources/secret-variables.yml
```
```sh
New Vault password:
Confirm New Vault password:
Encryption successful
```

### Encrypting A File

```sh
$ ansible-vault encrypt resources/secret-file-for-copy.txt --vault-password-file=resources/vault-secret-password.txt
Encryption successful
```

## How to Use It in Playbook
- [Explicit Secret Variable](test-secret-variable.yml#L5)
- [Encrypted File with Secret Variables](test-secret-file.yml#L5)
- [With Template Module](test-secret-template.yml#L9)
- [With Copy Module - 1](test-secret-copy-1.yml#L6)
- [With Copy Module - 2](test-secret-copy-2.yml#L15)

## Testing Ansible Vault
- [Run With Prompting Password](#with-prompting-password)
- [Run With Password File](#with-password-file)
- [Run With Encrypted Variables File](#with-encrypted-variables-file)
- [Run With `ANSIBLE_VAULT_PASSWORD_FILE` Env Variable](#with-ansible_vault_password_file-env-variable)
- [Use Template for encrypted files](#use-template-for-encrypted-files)
- [Use COPY for encrypted files (Case 1)](#use-copy-for-encrypted-files-case-1-copy-encrypted-file)
- [Use COPY for encrypted files (Case 2)](#use-copy-for-encrypted-files-case-2-copy-encrypted-data-to-the-file)

### With Prompting Password

```sh
$ ansible-playbook test-secret-variable.yml --ask-vault-pass
```
```sh
Vault password:

PLAY [localhost] **********************************************************

TASK [debug] **************************************************************
ok: [localhost] => {
    "spoiler": "Hello world"
}

PLAY RECAP ****************************************************************
localhost                  : ok=2    changed=0    unreachable=0    failed=0
```

### With Password File:

```sh
$ ansible-playbook test-secret-variable.yml --vault-password-file resources/vault-secret-password.txt
```
```sh
PLAY [localhost] **********************************************************

TASK [debug] **************************************************************
ok: [localhost] => {
    "spoiler": "Hello world"
}

PLAY RECAP ****************************************************************
localhost                  : ok=2    changed=0    unreachable=0    failed=0
```

### With Encrypted Variables File:

```sh
$ ansible-playbook test-secret-file.yml --vault-password-file resources/vault-secret-password.txt
```
```sh
PLAY [localhost] **********************************************************

TASK [debug] **************************************************************
ok: [localhost] => {
    "spoiler": "Hello from Encrypted File"
}

PLAY RECAP ****************************************************************
localhost                  : ok=2    changed=0    unreachable=0    failed=0
```

### With `ANSIBLE_VAULT_PASSWORD_FILE` Env Variable:

```sh
$ export ANSIBLE_VAULT_PASSWORD_FILE=resources/vault-secret-password.txt
$ ansible-playbook test-secret-file.yml
```
```sh
PLAY [localhost] **********************************************************

TASK [debug] **************************************************************
ok: [localhost] => {
    "spoiler": "Hello from Encrypted File"
}

PLAY RECAP ****************************************************************
localhost                  : ok=2    changed=0    unreachable=0    failed=0
```

### Use Template for encrypted files

```sh
$ export ANSIBLE_VAULT_PASSWORD_FILE=resources/vault-secret-password.txt
$ ansible-playbook test-secret-template.yml -vv
```
```sh
PLAYBOOK: test-secret-template.yml ****************************************
1 plays in test-secret-template.yml

PLAY [localhost] **********************************************************
META: ran handlers

TASK [template] ***********************************************************
changed: [localhost] => {"changed": true, "checksum": "bc88a39730773a13272a31695bc7890f958cb4fa", "dest": "/tmp/secret-file-for-template-decrypted.txt", "gid": 20, "group": "staff", "md5sum": "808a6a2f9cbaab38ca6bd57e8734499d", "mode": "0644", "owner": "sbeliakou", "size": 85, "src": "/Users/sbeliakou/.ansible/tmp/ansible-tmp-1498153193.86-121587783886816/source", "state": "file", "uid": 501}

PLAY RECAP ****************************************************************
localhost                  : ok=1    changed=1    unreachable=0    failed=0
```
```sh
$ cat /tmp/secret-file-for-template-decrypted.txt
```
```sh
Many many secred data here

Hello from playbook variable

Many many secred data here
```

### Use COPY for encrypted files (Case 1: copy encrypted file)

```sh
$ export ANSIBLE_VAULT_PASSWORD_FILE=resources/vault-secret-password.txt
$ ansible-playbook test-secret-copy-1.yml -vv
```
```sh
PLAYBOOK: test-secret-copy-1.yml ******************************************
1 plays in test-secret-copy-1.yml

PLAY [localhost] **********************************************************
META: ran handlers

TASK [copy] ***************************************************************
changed: [localhost] => {"changed": true, "checksum": "7003459d1bbc1ac15e0fee955a9afbda740eb9fa", "dest": "/tmp/secret-file-for-copy-1-decrypted.txt", "gid": 20, "group": "staff", "md5sum": "a7e72fe96d174f4efc928f40cb98c905", "mode": "0644", "owner": "sbeliakou", "size": 31, "src": "/Users/sbeliakou/.ansible/tmp/ansible-tmp-1498153832.51-197095625773999/source", "state": "file", "uid": 501}
META: ran handlers
META: ran handlers

PLAY RECAP ****************************************************************
localhost                  : ok=1    changed=1    unreachable=0    failed=0
```
```sh
$ cat /tmp/secret-file-for-copy-decrypted.txt
```
```sh
Hello!

This is ecrypted file
```

### Use COPY for encrypted files (Case 2: copy encrypted data to the file)

```sh
$ export ANSIBLE_VAULT_PASSWORD_FILE=resources/vault-secret-password.txt
$ ansible-playbook test-secret-copy-2.yml -vv
```
```sh
PLAYBOOK: test-secret-copy-2.yml ******************************************
1 plays in test-secret-copy-2.yml

PLAY [localhost] **********************************************************
META: ran handlers

TASK [copy] ***************************************************************
changed: [localhost] => {"changed": true, "checksum": "7b502c3a1f48c8609ae212cdfb639dee39673f5e", "dest": "/tmp/secret-file-for-copy-2-decrypted.txt", "gid": 20, "group": "staff", "md5sum": "3e25960a79dbc69b674cd4ec67a72c62", "mode": "0644", "owner": "sbeliakou", "size": 11, "src": "/Users/sbeliakou/.ansible/tmp/ansible-tmp-1498153573.72-229538264253212/source", "state": "file", "uid": 501}
META: ran handlers
META: ran handlers

PLAY RECAP ****************************************************************
localhost                  : ok=1    changed=1    unreachable=0    failed=0
```
```sh
$ cat /tmp/secret-file-for-copy-2-decrypted.txt
```
```sh
Hello world
```
