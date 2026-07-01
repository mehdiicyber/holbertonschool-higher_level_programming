#!/usr/bin/python3
"""
Takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter 'q'. Handles JSON responses.
"""
import sys
import requests


if __name__ == "__main__":
    if len(sys.argv) < 2:
        q = ""
    else:
        q = sys.argv[1]

    url = "http://0.0.0.0:5000/search_user"
    payload = {'q': q}

    try:
        response = requests.post(url, data=payload)
        json_data = response.json()

        if not json_data:
            print("No result")
        else:
            print(f"[{json_data.get('id')}] {json_data.get('name')}")

    except ValueError:
        print("Not a valid JSON")
