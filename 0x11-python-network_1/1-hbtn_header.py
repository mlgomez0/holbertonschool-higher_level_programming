#!/usr/bin/python3
# takes and url sends a request and displays the value of the X-Request-Id.

import urllib.request
import sys

url = sys.argv[1]
with urllib.request.urlopen(url) as resp:
    print("{}".format(resp.getheader('X-Request-Id')))
