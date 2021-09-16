'''weather.py uses openweathermap to download json and read weather forecast from it'''
import json, requests, sys

def getWeather(location):
    url = 'http://api.openweathermap.org/data/2.5/weather?q=%s&appid=924a2fc55307d32ebdcbc06c7d9ff415' % location
    response = requests.get(url)
    response.raise_for_status()

    w = json.loads(response.text)
    description = w['weather'][0]['description']
    temp = round(w['main']['temp'] - 273.15)
    windSpeed = w['wind']['speed']

    print('Current weather in %s: %s.\nTemperature: %s °C. \nWind speed: %s' % (location, description, temp, windSpeed))

print(getWeather('Gdynia'))