To perform this example run any docker Alpine container (preferably without pre-installed python).

Run
ansible-playbook -i <container name>, demo.yml -c docker_plugin

Connection plug-in will pre-install python inside the container.
