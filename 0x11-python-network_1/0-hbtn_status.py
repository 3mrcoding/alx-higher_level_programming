#!/usr/bin/python3
"""Write a Python script that fetches https://alx-intranet.hbtn.io/status"""

import urllib
from urllib.request import urlopen

url = "https://alx-intranet.hbtn.io/status"
with urlopen(url) as response:
    body = response.read()

print(
    f"Body response: \n\t - type: {type(body)}\n\t - content: {body}\n\t"
    f" - utf8 content: {body.decode('UTF-8')}")
