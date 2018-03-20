.PHONY: help 

help:
	@echo 'Usage:'
	@echo '  make <target>'
	@echo 
	@echo 'Targets:'
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-30s\033[0m %s\n", $$1, $$2}'
	@echo

all: vagrant nginx java tomcat

up:			## Start VM
	@vagrant up

down:		## Stop VM
	@vagrant halt

destroy:	## Destroy VM
	@vagrant destroy -f

vagrant:	## Vagrant Commands
	@echo "Vagrant Commands:"
	@echo "   Start VM         :   vagrant up"
	@echo "   Stop VM          :   vagrant halt"
	@echo "   Destroy VM       :   vagrant destroy -f"
	@echo "   Check VM Status  :   vagrant status"
	@echo "   SSH Log In       :   vagrant ssh"
	@echo

nginx:      ## Nginx Installation with Role Example
	@echo "Nginx Installation:"
	@echo "   Run Playbook  :  ansible-playbook tasks/21.yml -v"
	@echo "   Check Service :  http://192.168.56.22"
	@echo

java:       ## Java Installation with Role Example
	@echo "Java Role PLaybook"
	@echo "   Run Playbook  :  ansible-playbook tasks/22.yml -v"
	@echo "   Check Facts   :  ansible appserver01 -m setup -a 'filter=ansible_local'"
	@echo 

tomcat:		## Tomcat Installation with Role Example
	@echo "Nginx&Tomcat Installation Example:"
	@echo "   Run Playbook  :  ansible-playbook tasks/23.yml -v"
	@echo "   Check Facts   :  ansible appserver01 -m setup -a 'filter=ansible_local'"
	@echo "   Check Service :  http://192.168.56.22:8080"
	@echo