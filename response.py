#!/usr/bin/env python3.7

import json

class Response:
    
    def __init__(self, response):
        self.response = response
        
    def create_response(self):
        
        status_code = self.response['cod']
        response_object = {}
        
        if (int(status_code) == 200):
            response_object['statusCode'] = 200
            response_object['headers'] = {}
            response_object['headers']['Content-Type'] = 'application/json'
            response_object['headers']['Access-Control-Allow-Origin'] = '*'
            response_object['headers']['Access-Control-Allow-Methods'] = 'GET, OPTIONS'
            response_object['body'] = json.dumps(self.response)
        
        elif (int(status_code) == 404):
            response_object['statusCode'] = 200
            response_object['headers'] = {}
            response_object['headers']['Content-Type'] = 'application/json'
            response_object['headers']['Access-Control-Allow-Origin'] = '*'
            response_object['headers']['Access-Control-Allow-Methods'] = 'GET, OPTIONS'
            response_object['body'] = json.dumps(self.response)
        
        return response_object