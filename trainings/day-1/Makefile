.PHONY: help 

help:
	@echo 'Usage:'
	@echo '  make <target>'
	@echo 
	@echo 'Targets:'
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-30s\033[0m %s\n", $$1, $$2}'
	@echo

all: vagrant nginx tomcat

vagrant:	## Vagrant Commands
	@echo "Vagrant Commands:"
	@echo "   Start VM         :   vagrant up"
	@echo "   Stop VM          :   vagrant halt"
	@echo "   Destroy VM       :   vagrant destroy -f"
	@echo "   Check VM Status  :   vagrant status"
	@echo "   SSH Log In       :   vagrant ssh"
	@echo

nginx:    ## Nginx Installation Example
	@echo "Nginx Installation:"
	@echo "   Run Playbook:   ansible-playbook tasks/11.yml -i inventory03 -v"
	@echo "   Check Service:  http://192.168.56.21"
	@echo

tomcat: tomcat-yum tomcat-src

tomcat-yum:		## Tomcat Installation from YUM Example
	@echo "Tomcat Installation from YUM Example:"
	@echo "   Run Playbook:   ansible-playbook tasks/12.yml -i inventory03 -v"
	@echo "   Check Service:  http://192.168.56.21:8080"
	@echo

tomcat-src:		## Tomcat Installation from SRC Example
	@echo "Tomcat Installation from SRC Example:"
	@echo "   Run Playbook:   ansible-playbook tasks/13.yml -i inventory03 -v"
	@echo "   Check Service:  http://192.168.56.21:8080"
	@echo