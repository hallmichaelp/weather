#!/usr/bin/env python3.7

from forecast import Forecast
from response import Response
import json

def main_handler(event, context):
    #Store the zip code from the query string parameter 'zipcode' in the event object.
    zip_code = event['queryStringParameters']['zipcode']
    
    #Instantiate a new forecast object and pass in the zip code from the event object.
    forecast = Forecast(zip_code).get_forecast()
    
    #Instantiate a new response object and pass in the json response from the get_forecast method.
    response_object = Response(forecast).create_response()
    
    #Return the HTTP response.
    return response_object