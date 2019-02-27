## Using Ansible Vault

Password Files:
```
$ cat a_password_file
secret phrase A

$ cat b_password_file
secret phrase B
```

Ensrypting secrets:
```
$ ansible-vault encrypt_string --vault-id dev@a_password_file 'Dev Stack Secret'
!vault |
          $ANSIBLE_VAULT;1.2;AES256;dev
          66363164613536343663356639383363386264303662643332643761653333323638373237623638
          3037353732393836346134643364396165636433373235640a393539363530626261386236376230
          64313739393537363638323362373863653566303266653061396336303736376230363239333639
          3463336365653864630a623232393861653066333031643562623837333063613334636639343464
          33383234393662353630303331636536663165646432373863393331633064613963
Encryption successful

$ ansible-vault encrypt_string --vault-id prod@b_password_file 'Prod Stack Secret'
!vault |
          $ANSIBLE_VAULT;1.2;AES256;prod
          31613838353831343631353338383665393036643364313433353630636363643030376262653239
          3265343231383736633730656534663531313166363233320a316462396666643965373266663830
          36633066363634303032366532656161326431613831663931356137393838386134323139653963
          3331366462313566640a366365656236643062333362373337366466383138353565663662636136
          34303539373964623237613235663263613932653966383534386335333137656138
Encryption successful
```

```
$ ansible-playbook test.yml --vault-id a_password_file --vault-id b_password_file

PLAY [localhost] *************************************************************************

TASK [debug] *****************************************************************************
ok: [localhost] => {
    "spoiler1": "String to be ENCRYPTED"
}

TASK [debug] *****************************************************************************
ok: [localhost] => {
    "spoiler2": "Dev Stack Secret"
}

TASK [debug] *****************************************************************************
ok: [localhost] => {
    "spoiler3": "Prod Stack Secret"
}

PLAY RECAP *******************************************************************************
localhost                  : ok=3    changed=0    unreachable=0    failed=0
```
