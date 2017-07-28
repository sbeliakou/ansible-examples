from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.plugins.action import ActionBase
import socket

class ActionModule(ActionBase):

    def run(self, tmp=None, task_vars=None):

        if task_vars is None:
            task_vars = dict()

        result = super(ActionModule, self).run(tmp, task_vars)

	hostname = socket.gethostname()

        result['msg'] = ["Hello, I am a simple action plugin!"]
	result['msg'].append("I run on %s." % hostname)
	result['msg'].append("I don't have a corresponding module, so I can only be run with action.")
	result['msg'].append("I can see and use playbook variables like test_variable = %s." % task_vars['test_variable'])
	result['msg'].append("I can also access global ansible variables like ansible_version = %s." % task_vars['ansible_version'])
	result['_ansible_verbose_always'] = True

        return result
