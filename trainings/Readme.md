## Training Agenda:

### Module 1:
  - [103] Briefly about Configuration Management
  - [101] What is Ansible?
  - [102] YAML Syntax
  - [101] How Ansible Works
  - [101] Requirements and Installation
  - [101] “Hello world!” Playbook
  - [101] How to start the Project
  - [101] Under the bonnet:
    - [101] Architecture
    - [101] Connecting to Managed Nodes
    - [101] Hosts Inventory
    - [101] Playbook Structure
    - [101] Tasks and Modules
    - [101] Ad-hoc Commands
    - [101] Variables

  [Examples](day-1/)

### Module 2:
  - [101]/102 Handlers
  - Inventory
    - [101] environment specification
    - [101] host_vars/group_vars
    - [101] groups
    - [102] patterns
    - [102] inventory related variables
    - [101] behavioral parameters
  - [101] Ansible Roles
  - Ansible Variables:
    - [101] Precedence
    - [101] Command Line (extra vars)
    - [101] Registered Variables
  - Discovered Data
    - [102] Gathering Modes
    - [101] System Facts
    - [102] Custom Facts
    - [102] Getting Environment Variables
  - [101] Play Structure Skeleton
  - [101] Project Structure (Directory Layout)

  [Examples](day-2/)

### Module 3:
  - Loops in Ansible
    - [101] Standard Loops
    - [102] Standard Loops with Index
    - [102] Nested Loops
    - [102] Files
    - [102] Command Results
    - [102] Parallel Sets
    - [102] Random Choice
    - [102] Do-Until
    - [101] Register with Loops
    - Loop Control:
      - [102] label
      - [102] pause
      - [102] index_var
      - [102] loop_var
    - [102] Squash Actions
  - Jinja2 Filters:
    - [101] Default
    - [102] Default(omit)
    - [101] Mandatory
    - [101] Math Filters
    - [102] to/from_yaml/json
    - [102] Json_query
    - [102] Combine
    - [102] Comment + Ansible_managed
    - [102] Regex
    - [102] Urlsplit
  - [101] Conditionals
  - Jinja2 Tests
    - [101] Defined/Undefined
    - [102] Match/search
    - [102] Any/all
    - [101] File/Path tests
    - [101] Tasks Result
    - [101] Conditions+Tests vs Handlers
  - [103] Developing Custom Filters
  - [103] Developing Custom Modules
    - Testing Custom Modules
    - Modules on Bash with/without Arguments
    - Modules on Python with/without Arguments
  - [102] Dynamic inventories
  - [102] Inventory Modules

  [Examples](day-3/)

### Module 4:
  - Reusing Code with Includes
    - include_tasks / import_tasks
    - include_playbooks
    - include_roles / import_roles
    - include_vars
  - Ansible Tags
  - Jinja2 Templates
  - Ansible Configuration File (ansible.cfg)
  - Blocks, Rescue, Error Handling:
    - block
    - block/rescue/always
    - failed_when
    - changed_when
  - Ansible Strategies:
    - linear/free/debug
    - forks
    - serial
    - failure perception
  - Extending Ansible through Plugins:
    - callback plugins (stdout and others)
    - lookup plugins

  [Examples](day-4/)

### Module 5:
  - Secrets Management with Ansible Vault
    - Ansible Vault how to
    - Ansible vault vs Hashicorp Vault
  - Testing Ansible Playbooks
    - Syntax check mode
    - Dry run mode
    - Diff mode
    - Debug strategy
    - Start at task and Step
    - Debug / Yaml Callback Plugins
    - ANSIBLE_DEBUG Variable
  - Choice Push vs Pull
  - Ansible With:
    - Docker
    - Jenkins
    - AWS
    - Packer
      - DevOps Assembly Line
      - Building Images with Packer and Ansible
    - Terraform
    - Kubernetes
  - A little bit more about Ansible:
    - Lazy inventory
    - Limiting inventory
    - Script module
    - Wait_for module
    - Asynchronous actions and polling
    - Run_once
    - Hiding output
    - Logging ansible-playbook
    - Tasks delegating and local actions
  - Overall Questions

  [Examples](day-5/)

