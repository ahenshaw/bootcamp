'''Use web service to retrieve data'''
import webbrowser
# third-party libraries
import requests


URL = 'https://xkcd.com/info.0.json' # latest xkcd comic

response = requests.get(URL)
data = response.json()

print(data['img'])
webbrowser.open(data['img'])

print(data['alt'])
