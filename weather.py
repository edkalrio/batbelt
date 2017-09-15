#!/bin/env python3

import requests
import json

def wu(KEY, feature, LOCATION):
	wu_url = "http://api.wunderground.com/api/{}/{}/q/{}.json".format(KEY, feature, LOCATION)
	wu_response = requests.get(wu_url)
	wu_json = json.loads(wu_response.text)
	return wu_json

forecast_json = wu("", "forecast", "es/Palencia")
astronomy_json = wu("", "astronomy", "es/Palencia")
conditions_json = wu("", "conditions", "es/Palencia")

low = forecast_json['forecast']['simpleforecast']['forecastday'][0]['low']['celsius']
high = forecast_json['forecast']['simpleforecast']['forecastday'][0]['high']['celsius']
moon = astronomy_json['moon_phase']['phaseofMoon']
temp_c = conditions_json['current_observation']['temp_c']
icon = conditions_json['current_observation']['icon']

def moon_phase(moon):
	if moon == "New":
		moon_icon = "🌑 new"
	elif moon == "Waxing Crescent":
		moon_icon = "🌒 waxing crescent"
	elif moon == "First Quarter":
		moon_icon = "🌓 first quarter"
	elif moon == "Waxing Gibbous":
		moon_icon = "🌔 waxing gibbous"
	elif moon == "Full":
		moon_icon = "🌕 full"	
	elif moon == "Waning Gibbous":
		moon_icon = "🌖 waning gibbous"
	elif moon == "Last Quarter":
		moon_icon = "🌗 last quarter"
	elif moon == "Waning Crescent":
		moon_icon = "🌘 waning crescent"
	else:
		moon_icon = moon
	return moon_icon	

luna = moon_phase(moon)

def weather(icon):
	if icon == "partlycloudy":
		weather_icon = "⛅ Partly Cloudy"
	# elif icon == "":
	# 	weather_icon =	""	
	else:
		weather_icon = icon
	return weather_icon

sol = weather(icon)

print("{} {} {}-{}-{}".format(sol, luna, low, temp_c, high))
