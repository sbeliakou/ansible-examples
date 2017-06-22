## Encryption

**$ ansible-vault encrypt_string "Hello world"**
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

**$ ansible-vault encrypt resources/secret-variables.yml**
```sh
New Vault password:
Confirm New Vault password:
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