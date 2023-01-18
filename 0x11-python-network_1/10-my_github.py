#!/usr/bin/python3
"""Uses the Github API to display a Github ID based on given credentials.
Usge: ./10-my_githut.py <Github username> <Github password>
    - Uses Basic Authentication to access the ID.
"""
import sys
import requests
from requets.auth import HTTPBasicAuth


if __name__ == "__main__":
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    r = requests.get("https://api.github.com/user", auth=auth)
    print(r.json().get("id"))
