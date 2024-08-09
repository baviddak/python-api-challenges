import requests
import os
import argparse

def kel_to_cel(kel):
    return kel - 273.15

def get_weather(api_key, lat, lon):
    """
    Given the latitude and longitude, return the current weather.
    """
    excludes = "alerts,daily,hourly,minutely"
    api_url = f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude={excludes}&appid={api_key}"
    response = requests.get(api_url)

    weather_info = response.json()["current"]
    current_temp = kel_to_cel(weather_info["temp"])
    print(f"The current temperature is {current_temp}")

def get_coordinates(api_key, city, state, country_code):
    """
    Given the city, state/region, and country code, find the coordinates.
    """
    api_url = f"http://api.openweathermap.org/geo/1.0/direct?q={city},{state},{country_code}&appid={api_key}"
    response = requests.get(api_url)
    city_obj = response.json()[0]

    return city_obj["lat"], city_obj["lon"]

def get_api_key():
    """
    Check the environment for the API key.
    """
    return os.getenv("WEATHER_API_KEY", default=None)

def main():
    # Parse the input arguments
    parser = argparse.ArgumentParser(
                    prog='weather_forecast.py',
                    description='Provides the weather in any given city')

    parser.add_argument('-c', '--city')
    parser.add_argument('-s', '--state')
    parser.add_argument('-n', '--country')

    args = parser.parse_args()
    location = vars(args)
    api_key = get_api_key()

    if api_key == None:
        print("The WEATHER_API_KEY is not set.")
    else:
        lat, lon = get_coordinates(api_key, location["city"], location["state"], location["country"])
        get_weather(api_key, lat, lon)

main()