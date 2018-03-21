.PHONY: help 

help:
	@echo 'Usage:'
	@echo '  make <target>'
	@echo 
	@echo 'Targets:'
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-30s\033[0m %s\n", $$1, $$2}'
	@echo

loops:		## Ansible Loops Examples
	@echo "Ansible Loops Examples:"
	@echo "    https://github.com/sbeliakou/ansible-examples/tree/develop/samples/loops"
	@echo

conditions: ## Ansible Conditions Examples
	@echo "Ansible Conditions Examples:"
	@echo "    https://github.com/sbeliakou/ansible-examples/tree/develop/samples/conditions"
	@echo

filters:	## Ansible Jinja2 Filters Examples
	@echo "Ansible Jinja2 Filters Examples:"
	@echo "    https://github.com/sbeliakou/ansible-examples/tree/develop/samples/filters"
	@echo 
	@echo "Custom Filters:"
	@echo "    $ ansible-playbook tasks/mongodb_selector_filter/mongodb_url_select.yml"
	@echo "    $ ansible-playbook tasks/corporate_emails/corporate_email.yml"


modules:	## Testing Custom Modules
	@echo "Testing Modules"
	@echo "    $ ansible localhost -m custom_module_bash.sh"
	@echo "    $ ansible localhost -m custom_module_args_bash -a 'msg=\"hello from my bash module\"'"
	@echo "    $ ansible localhost -m custom_module_python"
	@echo "    $ ansible localhost -m custom_module_args_python -a 'msg='\"hello from my python module\"'"
	@echo

# deploment:		## Dynamic Inventory
# 	@echo "	
# 			$ ansible-playbook tasks/vagrant_management/vagrant.yml -v \\
#   -e vagrantfile=./ \\
#   -e @tasks/vagrant_management/deployment.json \\
#   -e application_war=$(pwd)/sample.war
# "