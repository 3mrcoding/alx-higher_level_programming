#!/usr/bin/python3
"""Return value of X-Request-Id variable in the response"""
from urllib import request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    with request.urlopen(url) as response:
        response = response.getheaders()
        for tuples in response:
            if tuples[0] == "X-Request-Id":
                print(tuples[1])
