from django.shortcuts import render
from django.contrib import messages
import requests
import json

def index_view(request):
    context = {}
    if request.method == 'GET':
        API_KEY = '5832d3fb7821368ed47f17f2b4cbfb18'
        BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'

        city = request.POST.get('search-form')

        request_url = f'{BASE_URL}?appid={API_KEY}&q={city}&units=metric'
        response = requests.get(request_url)

        if response.status_code == 200:
            data = response.json()
            print(data)
            longitude = data['coord']['lon']
            latitude = data['coord']['lat']
            country = data['sys']['country']
            weather = data['weather'][0]['description']
            temp = data['main']['temp']
            wind_speed = data['wind']['speed']
            humidity = data['main']['humidity']
            pressure = data['main']['pressure']
            icon = data['weather'][0]['icon']

            context = {'city':str(city).title(), 'weather': str(weather).title(), 'temperature': temp, 'country': country,
             'long': round(longitude, 2), 'lat': round(latitude, 2), 'humidity':humidity, 'wind_speed': wind_speed, 'icon': icon}
        

    return render(request, 'weather-app/index.html', context)

