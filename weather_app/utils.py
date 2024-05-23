import os
import requests
import logging
from dotenv import load_dotenv

logger = logging.getLogger(__name__)

# load .env file
load_dotenv()


def fetch_weather_data(lat, lon, data_type):
    api_key = os.getenv('OPENWEATHER_API_KEY')  # get the API key from.env file
    url = f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude=hourly,daily&appid={api_key}"

    logger.info(f"Fetching weather data from URL: {url}")
    response = requests.get(url)
    logger.info(f"Response status code: {response.status_code}")
    logger.info(f"Response content: {response.content}")

    if response.status_code != 200:
        raise Exception('Error fetching data from OpenWeatherMap')

    data = response.json()

    if data_type == 'current':
        return data['current']
    elif data_type == 'minutely':
        return data['minutely']
    elif data_type == 'hourly':
        return data['hourly']
    elif data_type == 'daily':
        return data['daily']
    else:
        raise ValueError('Invalid data type')
