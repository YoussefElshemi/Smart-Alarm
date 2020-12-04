from covid_update import get_covid

def test_one():
    covid_data = get_covid()
    assert covid_data['cumCasesByPublishDate'] != None

def test_two():
    covid_data = get_covid()
    assert covid_data['cumDeaths28DaysByPublishDate'] >= 51187
