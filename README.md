# COVID-19 Smart Alarm Clock

## Introduction
This program is a smart alarm clock with smart features built into it. The smart features include automated weather updates, news updates, and also coronavirus stats which appear as notifications. All three smart features can be announced using a text-to-speech module when an alarm goes off.


## Dependencies 
All of these dependencies are required to be installed to run the program:

`pip install sched`  
`pip install threading`  
`pip install logging`  
`pip install pyttsx3`  
`pip install flask`  
`pip install pylint`  
`pip install uk_covid19`  
`pip install requests`  
`pip install pytest`  

## Configuration	

Create a file in the main folder with the name config.json, paste and fill this in:  
`{ `  
`  "news_api_key": "",  `  
`  "weather_api_key": "",  `  
`"title": "Alarm Clock",  `  
`"city": "exeter",  `  
`"news_keywords": ["covid", "corona"],  `  
`"news_sources": ["bbc news"],  `  
`"covid_infected_threshold": 1000, `   
`"covid_death_threshold": 500,  `  
`"port": 5000  `  
`}`  

"news_api_key": You can register for a key [here](https://newsapi.org/)  
"weather_api_key": You can register for a key [here](https://openweathermap.org/api)  
"title": The title that is displayed on the alarm page  
"city": The city you live in to pull weather  
"news_keywords": A list of words to filter news with  
"news_sources": A list of news sources to filter alongside the keyword  
"covid_infected_threshold": The minumum number of infected in a day to display a notification  
"covid_death_threshold": The minimum number of deaths in a day to display a notification  
"port": The port for the website to run on  

## Usage

Start off by downloading all of the dependencies, to start the program, run `python main.py` in the main directory. Based on the port of you choose in the config (default is 5000), head over to your prefered web browser, and go to http://127.0.0.1:5000/index, if you have changed the port, replace 5000 with the port you chose. You can set an alarm, with the ability to choose the title, time it goes off, and whether or not the weather and news is announced. You can also cancel alarms, and also remove notifications. 

## Testing

To test the program, run `python -m pytest` in the console, please ensure that the program is also running simultaneously or there will be errors in the test_alarms category as this tests the program itself. This test will also check the APIs, so please ensure that your keys are valid. 

To test the syntax/linting, please run `python ./tests/linter.py`, this will check all of the files to ensure they the pep8 style and also correct syntax.

## Author
Name: Youssef Elshemi
Licence: [MIT](https://github.com/YoussefExeter/Smart-Alarm/blob/main/licence.md)
Github: [here](https://github.com/YoussefExeter/Smart-Alarm)
