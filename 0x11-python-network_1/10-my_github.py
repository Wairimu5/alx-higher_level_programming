#!/usr/bin/python3
"""
Takes GitHub credentials (username and personal access token) and
uses the GitHub API to display the user's id using requests.
"""

import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]
    url = "https://api.github.com/user"
    auth = (username, token)
    response = requests.get(url, auth=auth)
    
    try:
        data = response.json()
        print(data.get('id', 'None'))
    except ValueError:
        print("None")
