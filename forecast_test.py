#!/usr/bin/env python3.7

import os
import json
import requests
from urllib.parse import urljoin

zip_code = {'zip': '20171'}
api_key = {'appid': os.environ['api_key']}
base_url = 'https://api.openweathermap.org/data/2.5/weather'

payload = {**zip_code, **api_key}

response = requests.get(base_url, params=payload)
print(response.json())

