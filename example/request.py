#!/usr/bin/env python

import requests

url = "http://google.com"
r = requests.get(url)
if r.status_code == requests.codes.ok:
    print(f"SUCCESS GET'ing {url}")
else:
    print(f"Unexpected HTTP status code {r.status_code} GET'ing {url}")
