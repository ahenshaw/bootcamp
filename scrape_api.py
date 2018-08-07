'''Use web service to retrieve data'''
# standard library
import time

# third-party libraries
import requests


URL = 'https://maps.googleapis.com/maps/api/geocode/json'

locations = ['Kennesaw State University', 
             'Washington Monument']

for location in locations:
    print(location)
    parameters = {'address': location}
    response = requests.get(URL, params=parameters)
    print(response.url)

    data = response.json()
    # print(data)

    try:
        location = data['results'][0]['geometry']['location']
    except IndexError:
        print(response.content)
    else:    
        print('{0[lat]},{0[lng]}'.format(location))
        
    print(flush=True)
    time.sleep(0.5)


