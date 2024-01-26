#!/usr/bin/python3
"""sends a POST request to the passed URL with the email as a parameter, and
displays the body of the response"""
from urllib import request
import urllib
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')
    """this transfers the email from string to bytes format as http only deals
    with bytes"""
    req = urllib.request.Request(url, data=data, method='POST')
    with urllib.request.urlopen(req) as response:
        body = response.read().decode('utf-8')
        print(body)
