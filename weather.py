#!/bin/env python3

import requests
import json

KEY = ""
LOCATION = "303119"

def aw(feature):
	aw_url = "https://dataservice.accuweather.com/{}/{}?apikey={}&language=es-es&details=true&metric=true".format(feature, LOCATION, KEY) #http?
	aw_response = requests.get(aw_url)
	aw_json = json.loads(aw_response.text)
	return aw_json

def weather(icon):
	if icon == 1: #"sunny" or icon == "clear":
		weather_icon = "\N{black sun with rays}"
	elif icon in (2,3,33,34): #"mostlysunny" or icon in "partlysunny":
		weather_icon = "\N{white sun with small cloud}"
	elif icon in (4,5,6,35,36): #"mostlycloudy" or icon in "partlycloudy":
		weather_icon = "\N{sun behind cloud}"
	elif icon in (7,8,37,38): #"cloudy":
		weather_icon = "\N{cloud}"
	elif icon in (12,13,14,18,39,40): #"rain" or icon in "chancerain":
		weather_icon = "\N{cloud with rain}"
	elif icon in (24,25,26,29): #"sleet" or icon in "chancesleet":
		weather_icon = "\N{cloud with snow}"
	elif icon in (19,20,21,22,23,43,44): #"snow" or icon in "chancesnow" or icon in "flurries" or icon in "chanceflurries":
		weather_icon = "\N{snowflake}"
	elif icon in (15,16,17,41,42): #"tstorms" or icon in "chancetstorms":
		weather_icon = "\N{cloud with lightning}"
	elif icon in 11:
		weather_icon = "\N{fog}"
	else:
		weather_icon = icon
	return weather_icon

def lunar_phase(moon):
	if moon == "NewMoon":
		moon_icon = "\N{new moon symbol}"
	elif moon == "WaxingCrescent":
		moon_icon = "\N{waxing crescent moon symbol}"
	elif moon == "FirstQuarter":
		moon_icon = "\N{first quarter moon symbol}"
	elif moon == "WaxingGibbous":
		moon_icon = "\N{waxing gibbous moon symbol}"
	elif moon == "Full":
		moon_icon = "\N{full moon symbol}"    
	elif moon == "WaningGibbous":
		moon_icon = "\N{waning gibbous moon symbol}"
	elif moon == "LastQuarter":
		moon_icon = "\N{last quarter moon symbol}"
	elif moon == "WaningCrescent":
		moon_icon = "\N{waning crescent moon symbol}"
	else:
		moon_icon = moon
	return moon_icon

forecast_json = aw("forecasts/v1/daily/1day")
conditions_json = wu("currentconditions/v1")

low = str(forecast_json['DailyForecasts'][0]['Temperature']['Minimum']['Value'])
high = str(forecast_json['DailyForecasts'][0]['Temperature']['Maximum']['Value'])
moon = forecast_json['DailyForecasts'][0]['Moon']['Phase']
temp_c = conditions_json[0]['Temperature']['Metric']['Value']
icon = conditions_json[0]['WeatherIcon']

sup = str.maketrans(".-0123456789", "ᐧ⁻⁰¹²³⁴⁵⁶⁷⁸⁹")
sub = str.maketrans(".-0123456789", ".₋₀₁₂₃₄₅₆₇₈₉")

print("{} {}{}/{} {}".format(weather_icon, temp_c, high.translate(sup), low.translate(sub), moon_icon))
