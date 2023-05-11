import googlemaps # pip install googlemaps
import json
import requests

# save the key in a variable
API_KEY = 'AIzaSyDOorAGDAn6noddz7AjQzwx3xFrgeHtcV0'

# create a client
map_client = googlemaps.Client(key=API_KEY)

# create an empty list to store the station addresses
station_addresses = []

# get the station information
station_information = requests.get('https://gbfs.capitalbikeshare.com/gbfs/en/station_information.json').json()

# loop through the list of stations and append the address to the list
for station in station_information['data']['stations']:
    station_addresses.append(station['address'])

# get the latitude and longitude of the first station
response = map_client.geocode(station_addresses[0])
print(response)
print(response[0]['geometry']['location']['lat'])
print(response[0]['geometry']['location']['lng'])

# get the latitude and longitude of the last station
response = map_client.geocode(station_addresses[-1])
print(response)
print(response[0]['geometry']['location']['lat'])
print(response[0]['geometry']['location']['lng'])

# get the directions from the first station to the last station
response = map_client.directions(station_addresses[0], station_addresses[-1])

# print the directions
print(json.dumps(response, indent=4, sort_keys=True))
