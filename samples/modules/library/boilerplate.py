#!/usr/bin/python

# libraries you import here, must be present on the target node.

# You can defined other functions up here to make your code more modular.
# These functions will need to be called from main(), either directly or through N number of other functions
# that eventually lead back to main()

def main():

    module = AnsibleModule(
        argument_spec = dict(
           file = dict(default='file', choices=['file', 'directory']),
           owner = dict(required=True),
           mode = dict(required=True),
           recurse = dict(default=False, type='bool')
        ),
        supports_check_mode = True
    )

# Normalize params to make code cleaner
    file = module.params['file']
    owner = module.params['owner']
    mode = module.params['mode']
    recurse = module.params['recurse']

# Do logic here, can be calls to other functions above main()

    # if it is time to exit, successfully
    module.exit_json(changed=True, created=file, owner=owner, permossions=mode)

    # if it is time to exit, with an error
    module.fail_json(msg='Some error message')

    if module.check_mode:
    # Check if any changes would be made but don't actually make those changes
        module.exit_json(changed=check_if_system_state_would_be_changed())

# import module snippets (must stay here after your code)
from ansible.module_utils.basic import AnsibleModule
if __name__ == '__main__':
  main()
