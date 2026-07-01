#!/usr/bin/python3
"""
Takes in a URL and an email, sends a POST request to the passed URL
with the email as a parameter, and displays the body of the response.
"""
import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    data = {'email': email}

    utf8_data = urllib.parse.urlencode(data).encode('utf-8')

    with urllib.request.urlopen(url, data=utf8_data) as response:
        html = response.read()

    print(html.decode('utf-8'))
