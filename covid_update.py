'''
This module is used to get covid data for a specific region
'''

from uk_covid19 import Cov19API


def get_covid() -> dict:
    '''
    This function calls the covid api, and parses the data
    '''

    england_only = ['areaType=nation', 'areaName=England']

    cases_and_deaths = {
        'date': 'date',
        'areaName': 'areaName',
        'areaCode': 'areaCode',
        'newCasesByPublishDate': 'newCasesByPublishDate',
        'cumCasesByPublishDate': 'cumCasesByPublishDate',
        'newDeaths28DaysByPublishDate': 'newDeaths28DaysByPublishDate',
        'cumDeaths28DaysByPublishDate': 'cumDeaths28DaysByPublishDate',
        }

    api = Cov19API(filters=england_only, structure=cases_and_deaths) # initialise the api
    data = api.get_json()['data'][0] # extract the data

    return data # return the data


if __name__ == '__main__':
    print(get_covid())
