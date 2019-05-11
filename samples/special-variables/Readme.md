| Magic Variable | Definition |
|---|---|
| ansible_check_mode | Boolean that indicates if we are in check mode or not |
| ansible_diff_mode | Boolean that indicates if we are in diff mode or not |
| ansible_forks | Integer reflecting the number of maximum forks available to this run |
| ansible_inventory_sources | List of sources used as inventory |
| inventory_file | The file name of the inventory source in which the inventory_hostname was first defined |
| inventory_hostname | The inventory name for the 'current' host being iterated over in the play |
| inventory_hostname_short | The short version of inventory_hostname |
| inventory_dir | The directory of the inventory source in which the inventory_hostname was first defined |
| ansible_play_batch | List of active hosts in the current play run limited by the serial, aka 'batch'. Failed/Unreachable hosts are not considered 'active'. |
| ansible_play_hosts | The same as ansible_play_batch |
| ansible_play_hosts_all | List of all the hosts that were targeted by the play |
| ansible_playbook_python | The path to the python interpreter being used by Ansible on the controller |
| ansible_search_path | Current search path for action plugins and lookups, i.e where we search for relative paths when you do template: src=myfile |
| ansible_verbosity | Current verbosity setting for Ansible |
| ansible_version | Dictionary/map that contains information about the current running version of ansible, it has the following keys: full, major, minor, revision and string. |
| group_names | List of groups the current host is part of |
| groups | A dictionary/map with all the groups in inventory and each group has the list of hosts that belong to it |
| hostvars | A dictionary/map with all the hosts in inventory and variables assigned to them |
| omit | Special variable that allows you to 'omit' an option in a task, i.e - user: name=bob home={{ bobs_home|default(omit)}} |
| play_hosts | Deprecated, the same as ansbile_play_batch |
| playbook_dir | The path to the directory of the playbook that was passed to the ansible-playbook command line. |
| role_names | The names of the rules currently imported into the current play. |
| role_path | The path to the dir of the currently running role |


```bash
chmod a+x varaibles.yml
./varaibles.yml
```
