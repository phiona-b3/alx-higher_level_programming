#!/usr/bin/python3
"""
a Python script that takes in a URL and an email, sends a POST
request to the passed URL with the email as a parameter
"""
import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    value = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(value)
    data = data.encode("ascii")
    request = urllib.request.Request(sys.argv[1], data)

    with urllib.request.urlopen(request) as response:
        print(response.read().decode('utf-8'))
