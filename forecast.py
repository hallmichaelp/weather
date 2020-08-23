#!/usr/bin/env python3.7

import os
import json
import requests

class Forecast:
    #Setting two class variables that are pertinent to all instances of the class.
    #Ultimately we will need to move api_key to AWS key management and reference it instead of hard coding it.
    api_key = {'appid': os.environ['api_key']}
    base_url = 'https://api.openweathermap.org/data/2.5/weather'
    
    def __init__(self, zip):
        self.zip = zip
        
    def get_forecast(self):
        zip_code = {'zip': self.zip}
        payload = {**zip_code, **Forecast.api_key}
        response = requests.get(Forecast.base_url, params=payload)
        data = response.json()
        return data