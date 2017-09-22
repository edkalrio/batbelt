#!/bin/env python3

import requests
import json

KEY = ""
LOCATION = "es/Palencia"

def wu(feature, KEY, LOCATION):
    wu_url = "http://api.wunderground.com/api/{}/{}/q/{}.json".format(KEY, feature, LOCATION)
    wu_response = requests.get(wu_url)
    wu_json = json.loads(wu_response.text)
    return wu_json

def weather(icon):
    if icon == "sunny" or "clear":
        weather_icon = "🌣 Sunny"
    elif icon == "mostlysunny" or "partlysunny":
        weather_icon =  "🌤 Partly Sunny"    
    elif icon == "mostlycloudy" or "partlycloudy":
        weather_icon =  "⛅ Partly Cloudy"
    elif icon == "cloudy":
        weather_icon =  "☁ Cloudy"
    elif icon == "rain" or "chancerain":
        weather_icon =  "🌧 Rain"
    elif icon == "sleet" or "chancesleet":
        weather_icon =  "🌨 Sleet"
    elif icon == "snow" or "chancesnow" or "flurries" or "chanceflurries":
        weather_icon =  "❄ Snow"
    elif icon == "tstorms"  or "chancetstorms":
        weather_icon =  "🌩 Storm"
    elif icon == "fog" or "hazy":
        weather_icon =  "🌁 Fog"
    elif icon == "unknown":
        weather_icon =  "Unknown"
    else:
        weather_icon = icon
    return weather_icon

def lunar_phase(moon):
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

forecast_json = wu("forecast", KEY, LOCATION)
astronomy_json = wu("astronomy", KEY, LOCATION)
conditions_json = wu("conditions", KEY, LOCATION)

low = forecast_json['forecast']['simpleforecast']['forecastday'][0]['low']['celsius']
high = forecast_json['forecast']['simpleforecast']['forecastday'][0]['high']['celsius']
moon = astronomy_json['moon_phase']['phaseofMoon']
temp_c = conditions_json['current_observation']['temp_c']
icon = conditions_json['current_observation']['icon']

sup = str.maketrans("-0123456789", "⁻⁰¹²³⁴⁵⁶⁷⁸⁹")
sub = str.maketrans("-0123456789", "₋₀₁₂₃₄₅₆₇₈₉")

weather_icon = weather(icon)
moon_icon = lunar_phase(moon)

print("{} {}{}/{} {}".format(weather_icon, temp_c, high.translate(sup), low.translate(sub), moon_icon))
