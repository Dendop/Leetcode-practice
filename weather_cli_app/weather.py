from configparser import ConfigParser
import argparse
import sys
import json
from pprint import pp
from urllib import parse, request, error

import style 

BASE_WEATHER_API_URL = "http://api.openweathermap.org/data/2.5/weather"
##PADDING = 20
##REVERSE = "\033[;7m"
##RESET = "\033[0m"
# Weather Condition Codes
# https://openweathermap.org/weather-conditions#Weather-Condition-Codes-2
THUNDERSTORM = range(200, 300)
DRIZZLE = range(300, 400)
RAIN = range(500, 600)
SNOW = range(600, 700)
ATMOSPHERE = range(700, 800)
CLEAR = range(800, 801)
CLOUDY = range(801, 900)

def get_weather_data(query_url):
    try:
        response = request.urlopen(query_url)
    except error.HTTPError as http_error:
        if http_error.code == 401: # 401 - Unauthorized
            sys.exit("Acces denied. Check your API key")
        elif http_error.code == 404: # 404 - Not found
            sys.exit("Can't find weather data for this city")
        else:
            sys.exit(f"Something went wrong... ({http_error.code})")
    data = response.read()
    try:
        return json.loads(data)
    except json.JSONDecodeError:
        sys.exit("Couldn't read the server response")

def build_weather_query(city_input, imperial = False):#imperial is set to false as default

    api_key = _get_api_key()
    city_name = " ".join(city_input)
    url_encoded_city_name = parse.quote_plus(city_name)
    units = "imperial" if imperial else "metric"
    url = (
        f"{BASE_WEATHER_API_URL}?q={url_encoded_city_name}"
        f"&units={units}&appid={api_key}"
    )
    return url

def _get_api_key():
    """
    fetch API key from config file "secrets.ini""
    """
    config = ConfigParser()
    config.read("secrets.ini")
    
    return config["openweather"]["api_key"]

def read_user_cli_args():
    parser = argparse.ArgumentParser(
        description = "gets weather and temperature"
    )
    parser.add_argument(
        "city", nargs="+", type=str, help="enter the city"
    )
    parser.add_argument(
        "-i",
        "--imperial",
        action = "store_true",
        help = "display the temperature in imperial units",
    )
    return parser.parse_args()

def _select_weather_display_params(weather_id):
    if weather_id in THUNDERSTORM:
        display_params = ("💥", style.RED)
    elif weather_id in DRIZZLE:
        display_params = ("💧", style.CYAN)
    elif weather_id in RAIN:
        display_params = ("💦", style.BLUE)
    elif weather_id in SNOW:
        display_params = ("⛄️", style.WHITE)
    elif weather_id in ATMOSPHERE:
        display_params = ("🌀", style.BLUE)
    elif weather_id in CLEAR:
        display_params = ("🔆", style.YELLOW)
    elif weather_id in CLOUDY:
        display_params = ("💨", style.WHITE)
    else:  # In case the API adds new weather codes
        display_params = ("🌈", style.RESET)
    return display_params



def display_weather_info(weather_data, imperial = False):
    """
    Prints formatted weather info about the city
    Args:
        weather_data (dict): API response from Openweather
        imperial (bool): optional for using imperial
    """
    city = weather_data['name']
    weather_description = weather_data['weather'][0]['description']
    temperature = weather_data['main']['temp']
    weather_id = weather_data['weather'][0]['id']

    style.change_color(style.REVERSE)
    print(f"{city:^{style.PADDING}}", end = "")
    style.change_color(style.RESET)
   
    #the function returns emoji and color based on id API is returning
    weather_symbol, color = _select_weather_display_params(weather_id)

    style.change_color(color)
    print(f"\t{weather_symbol}", end = " ")
    print(f"\t{weather_description.capitalize():^{style.PADDING}}", end = " ")
    style.change_color(style.RESET)#resets the color 

    print(f"({temperature}°{'F' if imperial else 'C'})")

if __name__ == "__main__":
    user_args = read_user_cli_args()
    query_url = build_weather_query(user_args.city, user_args.imperial)
    weather_data = get_weather_data(query_url)
    display_weather_info(weather_data, user_args.imperial)