#!/usr/bin/python3
# script that fetches https://intranet.hbtn.io/status using requests

import requests

req = requests.get('https://intranet.hbtn.io/status')
print("Body response:")
print("    - type: {}".format(type(req.text)))
print("    - content: {}".format(req.text))
