from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.plugins.callback import CallbackBase
import smtplib
from email.mime.text import MIMEText

class CallbackModule(CallbackBase):
    
    CALLBACK_VERSION = 2.0
    CALLBACK_TYPE = 'notify'
    CALLBACK_NAME = 'cb_notify'
    CALLBACK_NEEDS_WHITELIST = True

    def __init__(self, *args, **kwargs):
        super(CallbackModule, self).__init__(*args, **kwargs)
        self.play = None

    def v2_playbook_on_play_start(self, play):
        self.play = play

    def v2_playbook_on_stats(self, stats):
        msg = MIMEText("Playbook execution finished: ok - %s changed - %s skipped - %s failures - %s" % (stats.ok, stats.changed, stats.skipped, stats.failures))
        msg['Subject'] = 'Test playbook finished'
        msg['From'] = 'test@gmail.com'
        msg['To'] = '%s' % self.play.vars['email']
        if self.play.vars['email']:
            send = smtplib.SMTP('localhost')
            send.sendmail(msg['From'], [msg['To']], msg.as_string())
            send.quit()
