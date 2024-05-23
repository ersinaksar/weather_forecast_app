from django.shortcuts import render
from django.utils import timezone
from rest_framework import viewsets
from rest_framework.response import Response
from .models import WeatherData
from .serializers import WeatherDataSerializer
from .utils import fetch_weather_data
from datetime import timedelta
from django.conf import settings


class WeatherDataViewSet(viewsets.ViewSet):
    def list(self, request):
        lat = request.query_params.get('lat')
        lon = request.query_params.get('lon')
        data_type = request.query_params.get('data_type')

        if not all([lat, lon, data_type]):
            return Response({'error': 'Missing required parameters'}, status=400)

        try:
            weather_data = WeatherData.objects.get(latitude=lat, longitude=lon, data_type=data_type)
            if timezone.now() - weather_data.timestamp > timedelta(minutes=settings.WEATHER_DATA_TIMEOUT):
                raise WeatherData.DoesNotExist
        except WeatherData.DoesNotExist:
            weather_data = fetch_weather_data(lat, lon, data_type)
            WeatherData.objects.update_or_create(
                latitude=lat, longitude=lon, data_type=data_type,
                defaults={'data': weather_data, 'timestamp': timezone.now()}
            )
            weather_data = WeatherData.objects.get(latitude=lat, longitude=lon, data_type=data_type)

        serializer = WeatherDataSerializer(weather_data)
        return Response(serializer.data)

def index(request):
    google_maps_api_key = settings.GOOGLE_MAPS_API_KEY
    return render(request, 'index.html', {'google_maps_api_key': google_maps_api_key})
