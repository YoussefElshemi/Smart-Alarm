'''
This module is used to get the weather for a specific region/city
'''

# pylint: disable=line-too-long

import json
import requests

def get_weather_from_api(api_key: str, city: str = 'exeter') -> dict:
    '''
    This function calls the openweathermap api to get the weather
    '''

    base_url = 'http://api.openweathermap.org/data/2.5/weather?'
    complete_url = base_url + 'appid=' + api_key + '&q=' + city
    response = requests.get(complete_url) # call the api
    return response # return the response


def get_weather(weather_data: dict) -> dict:
    '''
    This function parses the data from the api call
    '''

    main = weather_data['main'] # extract the main data
    current_temperature = main['temp'] # extract the current temperature
    current_humidity = main['humidity'] # extract the humidity
    weather = weather_data['weather'] # extract the weather
    weather_description = weather[0]['description'] # extract the description

    return { # return the results as a dictionary
        'temperature': round(current_temperature - 273.15), # convert from kelvin to celcius and round the value
        'humidity': round(current_humidity), # round the value
        'description': weather_description
    }

if __name__ == '__main__':
    print(get_weather(get_weather_from_api(json.load(open('config.json'))['weather_api_key'], 'london').json()))
