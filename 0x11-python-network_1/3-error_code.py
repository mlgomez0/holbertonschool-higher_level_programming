#!/usr/bin/python3
# takes and url sends a request: displays body and handles error.

import urllib.request
import sys

url = sys.argv[1]
req = urllib.request.Request(url)
try:
    with urllib.request.urlopen(req) as resp:
        print(resp.read().decode('utf-8'))
except urllib.error.HTTPError as e:
    print("Error code: {}".format(e.code))
