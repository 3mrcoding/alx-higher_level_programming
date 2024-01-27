#!/usr/bin/python3
"""sends a request to the URL and displays the body of the response."""

import requests
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    r = requests.get(url).status_code
    if r >= 400:
        print(f'Error code: {r}')
    else:
        print(requests.get(url).text)
