from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
import os
from dotenv import load_dotenv


class WeatherDataTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        load_dotenv()

    def test_get_weather_data(self):
        url = reverse('weather-list')
        response = self.client.get(url, {'lat': 33.441792, 'lon': -94.037689, 'data_type': 'current'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
