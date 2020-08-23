#!/usr/bin/env python3.7

from response import Response

lambda_response = {"coord": {"lon": -73.94, "lat": 42.81}, "weather": [{"id": 802, "main": "Clouds", "description": "scattered clouds", "icon": "03d"}], "base": "stations", "main": {"temp": 275.62, "feels_like": 272.89, "temp_min": 274.26, "temp_max": 277.15, "pressure": 1012, "humidity": 80}, "visibility": 16093, "wind": {"speed": 0.93, "deg": 162}, "clouds": {"all": 40}, "dt": 1589191163, "sys": {"type": 1, "id": 3273, "country": "US", "sunrise": 1589189812, "sunset": 1589242048}, "timezone": -14400, "id": 0, "name": "Schenectady", "cod": 200}

#lambda_response = {"cod": "404", "message": "city not found"}

response = Response(lambda_response)

print(response.create_response())

