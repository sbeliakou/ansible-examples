from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.plugins.callback import CallbackBase
from ansible import constants as C
from ansible.utils.color import colorize, hostcolor
import json
import os
import datetime


class CallbackModule(CallbackBase):

    '''
    This is the default callback interface, which simply prints messages
    to stdout when new callback events are received.
    '''

    CALLBACK_VERSION = 2.0
    CALLBACK_TYPE = 'stdout'
    CALLBACK_NAME = 'demo'
    CALLBACK_NEEDS_WHITELIST = True

    module_name = ""

    def show(self, task, host, result, color):
        if self.module_name != "setup":
            res = {}
            for key, value in result.iteritems():
                if key[0] != "_" and key not in ["invocation"]:
                    res.update({
                        key: value
                    })
            self._display.display("{} => {}".format(
                host, json.dumps(res, indent=4)
            ), color=color)
        else:
            self._display.display("{} => ok".format(host), color=color)

    def v2_playbook_on_start(self, playbook):
        print("[{}] | PLAYBOOK STARTED {}\nFILENAME: {}/{}\n".format(
            str(datetime.datetime.now()), ">"*31, os.getcwd(), playbook._file_name
        ))

    def v2_playbook_on_play_start(self, play):
        print("[{}] | PLAY: '{}'\n".format(str(datetime.datetime.now()), play.name))

    def v2_playbook_on_task_start(self, task, is_conditional):
        self.module_name = task._attributes.get("action", "")
        print("[{}] | TASK: '{}' | Module '{}'".format(
            str(datetime.datetime.now()), 
            task._attributes.get("name", "name"), 
            self.module_name
        ))
        
    def v2_runner_on_failed(self, result, ignore_errors=False):
        self.show(result._task, result._host.get_name(), result._result, C.COLOR_ERROR)
        if ignore_errors:
            self._display.display("...ignoring", color=C.COLOR_SKIP)
        print("")

    def v2_runner_on_ok(self, result):
        self.show(result._task, result._host.get_name(), result._result, C.COLOR_OK)
        print("")

    def v2_runner_on_skipped(self, result):
        self.show(result._task, result._host.get_name(), result._result, C.COLOR_SKIP)
        print("")

    def v2_runner_on_unreachable(self, result):
        self.show(result._task, result._host.get_name(), result._result, C.COLOR_ERROR)
        print("")

    def v2_playbook_on_stats(self, stats):
        print("[{}] | PLAYBOOK SUMMARY {}\n".format(str(datetime.datetime.now()), ">"*31))

        hosts = sorted(stats.processed.keys())
        for h in hosts:
            t = stats.summarize(h)

            self._display.display(u"%s : %s %s %s %s" % (
                hostcolor(h, t),
                colorize(u'ok', t['ok'], C.COLOR_OK),
                colorize(u'changed', t['changed'], C.COLOR_CHANGED),
                colorize(u'unreachable', t['unreachable'], C.COLOR_UNREACHABLE),
                colorize(u'failed', t['failures'], C.COLOR_ERROR)),
                screen_only=True
            )

            self._display.display(u"%s : %s %s %s %s" % (
                hostcolor(h, t, False),
                colorize(u'ok', t['ok'], None),
                colorize(u'changed', t['changed'], None),
                colorize(u'unreachable', t['unreachable'], None),
                colorize(u'failed', t['failures'], None)),
                log_only=True
            )

        self._display.display("", screen_only=True)