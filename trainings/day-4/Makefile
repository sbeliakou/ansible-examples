.PHONY: help 

help:
	@echo 'Usage:'
	@echo '  make <target>'
	@echo 
	@echo 'Targets:'
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-30s\033[0m %s\n", $$1, $$2}'
	@echo

all: tags templates blocks callback

tags:	## Tags Usage Example
	@echo "Tags Usage Examples:"
	@echo " - List Playbook Tags:"
	@echo "    ansible-playbook tasks/tags/vagrant.yml --list-tags"
	@echo
	@echo " - Create VM, Provision VM, Deploy WAR, Destroy VM:"
	@echo "    ansible-playbook tasks/tags/vagrant.yml -v -e @tasks/tags/deployment.json"
	@echo
	@echo " - Create VM, Provision VM and Deploy WAR:"
	@echo "    ansible-playbook tasks/tags/vagrant.yml -v -e @tasks/tags/deployment.json --skip-tags=cleanup"
	@echo
	@echo " - Provision VM":
	@echo "    ansible-playbook tasks/tags/vagrant.yml -v -e @tasks/tags/deployment.json --tags=provision"
	@echo
	@echo " - Deploy WAR (only):"
	@echo "    ansible-playbook tasks/tags/vagrant.yml -v -e @tasks/tags/deployment.json --tags=deploy"
	@echo 
	@echo " - Destroy VM:"
	@echo "    ansible-playbook tasks/tags/vagrant.yml -v -e @tasks/tags/deployment.json --tags=cleanup"
	@echo

blocks:		## Blocks Usage Examples
	@echo "Rescue / Error Handling"
	@echo "    ansible-playbook tasks/blocks/rescue.yml -v"
	@echo

callback:	## Callback Plugin Usage Example
	@echo "Testing Custom Callback Plugin:"
	@echo "    ANSIBLE_CONFIG=tasks/callback/ansible.cfg ansible-playbook tasks/callback/callback-test.yml -v"
	@echo 

templates:	## Templates examples
	@echo "Testing Ansible Templates:"
	@echo "    ansible-playbook tasks/templates/testing_templates.yml --tags=example0; cat /tmp/result-by-example-0.conf"
	@echo "    ansible-playbook tasks/templates/testing_templates.yml --tags=example1; cat /tmp/result-by-example-1.conf"
	@echo "    ansible-playbook tasks/templates/testing_templates.yml --tags=example2; cat /tmp/result-by-example-2.conf"
	@echo "    ansible-playbook tasks/templates/testing_templates.yml --tags=example3; cat /tmp/result-by-example-3.conf"
	@echo
