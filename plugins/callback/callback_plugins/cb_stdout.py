from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.plugins.callback import CallbackBase

class CallbackModule(CallbackBase):
    
    CALLBACK_VERSION = 2.0
    CALLBACK_TYPE = 'stdout'
    CALLBACK_NAME = 'cb_stdout'
    CALLBACK_NEEDS_WHITELIST = True

    def __init__(self, *args, **kwargs):
        super(CallbackModule, self).__init__(*args, **kwargs)

    def v2_playbook_on_vars_prompt(self, varname, private=True, prompt=None, encrypt=None,
                                  confirm=False, salt_size=None, salt=None, default=None):
        self._display.display("We can modify actions like variable prompts. Btw, do input your email address:", color='cyan')

    def show(self, result, colour):
        self._display.display("\n%s | HOST: %s | failed: %s | skipped: %s | unreachable: %s | changed: %s\n"
        % (result._task, result._host, result.is_failed(), result.is_skipped(), result.is_unreachable(), result.is_changed()))
        self._display.display("Output: %s\n" % result._task_fields['args'].values(), color=colour)

    def v2_runner_on_failed(self, result, ignore_errors=False):
        self.show(result, 'magenta')

    def v2_runner_on_ok(self, result):
        self.show(result, 'yellow')

    def v2_runner_on_skipped(self, result):
        self.show(result, 'blue')

    def v2_runner_on_unreachable(self, result):
        self.show(result, 'red')

