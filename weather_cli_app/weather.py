from configparser import ConfigParser
import argparse
import sys
import json
from pprint import pp
from urllib import parse, request, error

BASE_WEATHER_API_URL = "http://api.openweathermap.org/data/2.5/weather"

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

def build_weather_query(city_input, imperial = False):

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

if __name__ == "__main__":
    user_args = read_user_cli_args()
    query_url = build_weather_query(user_args.city, user_args.imperial)
    weather_data = get_weather_data(query_url)
    print(
        f"{weather_data['name']}: \n"
        f"{weather_data['weather'][0]['description']}\n"
        f"{weather_data['main']['temp']}\n"
    )