import requests
from datetime import datetime, timedelta

def test_one():
    date = datetime.now() + timedelta(minutes=5)
    formatted_date = date.strftime('%Y-%m-%dT%H:%M')
    response = requests.get('http://127.0.0.1:5000/index?alarm={0}&two=test'.format(formatted_date))
    assert response.status_code == 200

def test_two():
    response = requests.get('http://127.0.0.1:5000/index?alarm_item=test')
    assert response.status_code == 200