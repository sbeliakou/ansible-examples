## Encryption

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


## Use in Playbook
- [Explicit Secret Variable](test-secret-variable.yml#L5)
- [Encrypted File with Secret Variables](test-secret-file.yml#L5)

## Testing Secret variables

With Prompting Password:

**$ ansible-playbook test-secret-variable.yml --ask-vault-pass**
```sh
Vault password:

PLAY [localhost] **********************************************************

TASK [Gathering Facts] ****************************************************
ok: [localhost]

TASK [debug] **************************************************************
ok: [localhost] => {
    "spoiler": "Hello world"
}

PLAY RECAP ****************************************************************
localhost                  : ok=2    changed=0    unreachable=0    failed=0
```

With Password File:

**$ ansible-playbook test-secret-variable.yml --vault-password-file resources/vault-secret-password.txt**
```sh
PLAY [localhost] **********************************************************

TASK [Gathering Facts] ****************************************************
ok: [localhost]

TASK [debug] **************************************************************
ok: [localhost] => {
    "spoiler": "Hello world"
}

PLAY RECAP ****************************************************************
localhost                  : ok=2    changed=0    unreachable=0    failed=0
```

With Encrypted Variables File:

**$ ansible-playbook test-secret-file.yml --vault-password-file resources/vault-secret-password.txt**
```sh
PLAY [localhost] **********************************************************

TASK [Gathering Facts] ****************************************************
ok: [localhost]

TASK [debug] **************************************************************
ok: [localhost] => {
    "spoiler": "Hello from Encrypted File"
}

PLAY RECAP ****************************************************************
localhost                  : ok=2    changed=0    unreachable=0    failed=0
```

### Use COPY for encrypted files

```sh
$ ansible-playbook test-secret-copy.yml -vv
```
```sh
PLAYBOOK: test-secret-copy.yml ********************************************
1 plays in test-secret-copy.yml

PLAY [localhost] **********************************************************
META: ran handlers

TASK [copy] ***************************************************************
changed: [localhost] => {"changed": true, "checksum": "7003459d1bbc1ac15e0fee955a9afbda740eb9fa", "dest": "/tmp/secret-file-for-copy-decrypted.txt", "gid": 20, "group": "staff", "md5sum": "a7e72fe96d174f4efc928f40cb98c905", "mode": "0644", "owner": "sbeliakou", "size": 31, "src": "/Users/sbeliakou/.ansible/tmp/ansible-tmp-1498151848.88-63302319730905/source", "state": "file", "uid": 501}
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