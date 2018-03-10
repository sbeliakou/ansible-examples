from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.plugins.action import ActionBase
import socket

class ActionModule(ActionBase):

    def run(self, tmp=None, task_vars=None):

        if task_vars is None:
            task_vars = dict()

        result = super(ActionModule, self).run(tmp, task_vars)

        secret = self._task.args.get('secret', None)
	test_variable = self._task.args.get('test_variable', None)

	result['_ansible_verbose_always'] = True
	
	hostname = socket.gethostname()

	with open(secret, "r") as file:
	    secret_text = file.read().replace('\n', '')

	pass_vars = dict()
	pass_vars.update(
	    ansible_version=task_vars['ansible_version'],
	    secret=secret_text
	)

	result['action_msg'] = ["Hello, I am another action plugin!"]
	result['action_msg'].append("I run on %s." % hostname)
	result['action_msg'].append("Since I have a corresponding empty module file I can be called the same way as modules.")
	result['action_msg'].append("I call module echo_module and pass some playbook and global ansibe variables to it along with my test_variable = %s" % test_variable)
	result['action_msg'].append("Also I read a secret from a file located on ansible host machine in %s and pass it to the module." % secret)

	new_module_args = dict()
	new_module_args.update(
            dict(
                test_argument=test_variable,
		task_var=pass_vars,
            ),
        )

	result.update(
            self._execute_module(
                module_name='echo_module',
                module_args=new_module_args,
            )
        )

        return result
	
