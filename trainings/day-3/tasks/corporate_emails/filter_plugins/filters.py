from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from functools import partial
import types

from ansible import errors


def email(arg, suffix="epam.com"):
    import re

    result = []
    for item in arg:
        result.append("{}_{}@{}".format(item['name'], item['surname'], suffix))

    return result


class FilterModule(object):
    def filters(self):
        return {
            'email': email
        }