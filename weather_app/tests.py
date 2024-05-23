from django.test import TestCase, override_settings
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
import os
from dotenv import load_dotenv

load_dotenv()

class WeatherDataTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    @override_settings(OPENWEATHER_API_KEY=os.getenv('OPENWEATHER_API_KEY'))
    def test_get_weather_data(self):
        url = reverse('weather-list')
        response = self.client.get(url, {'lat': 33.441792, 'lon': -94.037689, 'data_type': 'current'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
