import json
from news_filter import get_news, get_news_from_api 

def test_one():
    news_json = json.load(open('gb-news.json'))
    news = get_news(news_json)
    assert len(news) >= 1
    
def test_two():
    news_json = json.load(open('gb-news.json'))
    news = get_news(news_json)
    assert news[0]['title'] != None

def test_four():
    response = get_news_from_api(json.load(open('config.json'))['news_api_key'])
    assert response.status_code == 200
