import json
import requests
import os
import sys
import argparse

# Parse the input arguments
parser = argparse.ArgumentParser(
                    prog='WeatherForecaster',
                    description='Provides the weather in any given city')

parser.add_argument('-c', '--city')
parser.add_argument('-s', '--state')
parser.add_argument('-n', '--country')

args = parser.parse_args()
print(args)


# def get_weather(lat, lon):

# def get_coordinates(city, state, country_code):

#     # return lat, lon

# def get_api_key():




    


