import json
from weather_update import get_weather, get_weather_from_api

weather_json = {
    'coord':{
        'lon':-3.53,
        'lat':50.72
    },
    'weather':[{
        'id':500,
        'main':'Rain',
        'description':'light rain',
        'icon':'10n'
    }],
    'base':'stations',
    'main':{
        'temp':286.32,
        'feels_like':284.96,
        'temp_min':285.93,
        'temp_max':286.48,
        'pressure':1016,
        'humidity':95
    },
    'visibility':10000,
    'wind':{
        'speed':3,
        'deg':121
    },
    'rain':{
        '1h':0.81
    },
    'clouds':{
        'all':18
    },
    'dt':1604877233,
    'sys':{
        'type':3,
        'id':2005600,
        'country':'GB',
        'sunrise':1604819889,
        'sunset':1604853461
    },
    'timezone':0,
    'id':2649808,
    'name':'Exeter',
    'cod':200
}

def test_one():
    weather = get_weather(weather_json)
    assert weather['description'] == 'light rain'
    
def test_two():
    weather = get_weather(weather_json)
    assert weather['temperature'] == 13

def test_three():
    weather = get_weather(weather_json)
    assert weather['humidity'] == 95

def test_four():
    response = get_weather_from_api(json.load(open('config.json'))['weather_api_key'], 'exeter')
    assert response.status_code == 200
