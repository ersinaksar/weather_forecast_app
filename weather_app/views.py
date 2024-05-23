import plotly.express as px
from django.shortcuts import render
from django.utils import timezone
from rest_framework import viewsets
from rest_framework.response import Response
from .models import WeatherData
from .serializers import WeatherDataSerializer
from .utils import fetch_weather_data
from datetime import timedelta
from django.conf import settings
import plotly.graph_objs as go
from plotly.offline import plot
import pandas as pd


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


def weather_chart(request):
    lat = request.GET.get('lat')
    lon = request.GET.get('lon')
    data_type = request.GET.get('data_type')

    if not all([lat, lon, data_type]):
        return render(request, 'weather_chart.html', {'error': 'Missing required parameters'})

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

    data = weather_data.data

    if data_type == 'hourly':
        df = pd.DataFrame(data)
        df['dt'] = pd.to_datetime(df['dt'], unit='s')
        fig = px.line(df, x='dt', y='temp', title='Hourly Temperature')
    elif data_type == 'daily':
        df = pd.DataFrame(data)
        df['dt'] = pd.to_datetime(df['dt'], unit='s')
        df['day_temp'] = df['temp'].apply(lambda x: x['day'])
        fig = px.line(df, x='dt', y='day_temp', title='Daily Temperature')
    else:
        return render(request, 'weather_chart.html', {'error': 'Unsupported data type for chart'})

    graph_html = fig.to_html(full_html=False)

    return render(request, 'weather_chart.html', {'graph_html': graph_html})