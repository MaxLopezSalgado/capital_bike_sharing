from pprint import pprint # pip install pprintpp
import googlemaps # pip install googlemaps
import json 
import requests

# save the key in a variable
API_KEY = 'AIzaSyDOorAGDAn6noddz7AjQzwx3xFrgeHtcV0'

# create a client
map_client = googlemaps.Client(key=API_KEY)

# get the station information
station_information = requests.get('https://gbfs.capitalbikeshare.com/gbfs/en/station_information.json').json()

# get the station coordinates from the station information and save them in a list of strings
station_coordinates = [str(station['name']) + ',' + str(station['lat']) + ',' + str(station['lon']) for station in station_information['data']['stations']]
# print(station_coordinates)

# get the unique values from the list of strings
unique_station_coordinates = list(set(station_coordinates))
# print(unique_station_coordinates)

# eliminate the duplicates from the list of strings
unique_station_coordinates = list(dict.fromkeys(station_coordinates))
print(unique_station_coordinates)