'''
This module is used to pull news from BBC or anything covid related
'''

# pylint: disable=line-too-long


import json
import requests
from flask import Markup

def get_news_from_api(api_key: str) -> dict:
    '''
    This function does the api call to newsapi to pull all top headlines
    '''

    base_url = 'https://newsapi.org/v2/top-headlines?'
    complete_url = base_url + 'country=gb' + '&apiKey=' + api_key
    response = requests.get(complete_url) # call the api
    return response # return the response dictionary


def get_news(news_dict: dict) -> list:
    '''
    This function parses the results from get_news_from_api()
    '''
    filtered_articles = [] # create an empty array for the filtered articles
    config_file = json.load(open('config.json')) # open the config file and load it into a dictionar
    covid = config_file['news_keywords'] # exrtract the news keywords
    news = config_file['news_sources'] # extract the news sources
    articles = news_dict['articles'] # load the articles from the api response
    for article in articles: # for each article in the list of articles
        if (any(x in article['title'].lower() for x in covid) or # if the title matches the keywords
            (any(x in article['source']['name'].lower() for x in news)) or # if the source matches the news sources
            (article['content'] and any(x in article['content'].lower() for x in covid))): # if the content matches the keywords
            description = article['description'] # extract the description
            content = Markup('<a href={0}>{1}</a>'.format(article['url'], description)) # markup the description with href
            filtered_articles.append({ 'title': article['title'], 'content': content }) # add the article to the list of filtered articles

    return filtered_articles # return the filtered articles

if __name__ == '__main__':
    print(get_news(get_news_from_api(json.load(open('config.json'))['news_api_key']).json()))
