## Training Agenda:

### Module 1:
  - Briefly about Configuration Management
  - What is Ansible?
  - YAML Syntax
  - How Ansible Works
  - Requirements and Installation
  - “Hello world!” Playbook
  - How to start the Project
  - Under the bonnet:
    - Architecture
    - Connecting to Managed Nodes
    - Hosts Inventory
    - Playbook Structure
    - Tasks and Modules
    - Ad-hoc Commands
    - Variables

  [Examples](day-1/)

### Module 2:
  - Handlers
  - Inventory
    - environment specification
    - host_vars/group_vars
    - groups
    - patterns
    - inventory related variables
    - behavioral parameters
  - Ansible Roles
  - Ansible Variables:
    - Precedence
    - Command Line (extra vars)
    - Registered Variables
  - Discovered Data
    - Gathering Modes
    - System Facts
    - Custom Facts
    - Getting Environment Variables
  - Play Structure Skeleton
  - Project Structure (Directory Layout)

  [Examples](day-2/)

### Module 3:
  - Loops in Ansible
    - Standard Loops
    - Standard Loops with Index
    - Nested Loops
    - Files
    - Command Results
    - Parallel Sets
    - Random Choice
    - Do-Until
    - Register with Loops
    - Loop Control:
      - label
      - pause
      - index_var
      - loop_var
    - Squash Actions
  - Jinja2 Filters:
    - Default
    - Default(omit)
    - Mandatory
    - Math Filters
    - to/from_yaml/json
    - Json_query
    - Combine
    - Comment + Ansible_managed
    - Regex
    - Urlsplit
  - Conditionals
  - Jinja2 Tests
    - Defined/Undefined
    - Match/search
    - Any/all
    - File/Path tests
    - Tasks Result
    - Conditions+Tests vs Handlers
  - Developing Custom Filters
  - Developing Custom Modules
    - Testing Custom Modules
    - Modules on Bash with/without Arguments
    - Modules on Python with/without Arguments
  - Dynamic inventories
  - Inventory Modules

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

