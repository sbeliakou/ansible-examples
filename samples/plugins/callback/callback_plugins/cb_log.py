from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.plugins.callback import CallbackBase
from datetime import datetime

class CallbackModule(CallbackBase):
    
    CALLBACK_VERSION = 2.0
    CALLBACK_TYPE = 'log'
    CALLBACK_NAME = 'cb_log'
    CALLBACK_NEEDS_WHITELIST = True

    def __init__(self, *args, **kwargs):
        super(CallbackModule, self).__init__(*args, **kwargs)
        self.start_time = datetime.now()

    def v2_on_any(self, *args, **kwargs):
        with open('log.txt', 'a+') as log:
            log.write("\nArgs: %s Kwargs: %s\n" % (args, kwargs))

    def days_hours_minutes_seconds(self, runtime):
        minutes = (runtime.seconds // 60) % 60
        r_seconds = runtime.seconds - (minutes * 60)
        return runtime.days, runtime.seconds // 3600, minutes, r_seconds

    def show(self, result):
        if result.is_failed():
            colour = 'magenta'
        elif result.is_skipped():
            colour = 'blue'
        else:
            colour = 'yellow'
        with open('log.txt', 'a+') as log:
            log.write("\n%s | HOST: %s | failed: %s | skipped: %s | unreachable: %s | changed: %s\n"
        % (result._task, result._host, result.is_failed(), result.is_skipped(), result.is_unreachable(), result.is_changed()))
            log.write("Output: %s\n" % result._task_fields['args'].values())

    def v2_runner_on_failed(self, result, ignore_errors=False):
        self.show(result)

    def v2_runner_on_ok(self, result):
        self.show(result)

    def v2_runner_on_skipped(self, result):
        self.show(result)

    def v2_runner_on_unreachable(self, result):
        self.show(result)

    def v2_playbook_on_stats(self, stats):
        end_time = datetime.now()
        runtime = end_time - self.start_time
        with open('log.txt', 'a+') as log:
            log.write("\nPlaybook run took %s days, %s hours, %s minutes, %s seconds\n" % (self.days_hours_minutes_seconds(runtime)))
