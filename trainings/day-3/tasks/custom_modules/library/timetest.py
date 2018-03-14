#!/usr/bin/env python

import datetime
import json

date = str(datetime.datetime.now())
print json.dumps({
  "time": date
})


