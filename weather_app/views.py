from django.shortcuts import render, redirect
import requests


def index_view(request):
    context = {}
    if request.method == 'GET':
        API_KEY = ''
        BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'

        city = request.GET.get('city')

        request_url = f'{BASE_URL}?appid={API_KEY}&q={city}&units=metric'
        response = requests.get(request_url)

        if response.status_code == 200:
            data = response.json()
            
            longitude = data['coord']['lon']
            latitude = data['coord']['lat']
            country = data['sys']['country']
            condition = data['weather'][0]['main']
            weather = data['weather'][0]['description']
            temp = data['main']['temp']
            wind_speed = data['wind']['speed']
            humidity = data['main']['humidity']
            icon = data['weather'][0]['icon']

            context = {'city':city, 'weather': str(weather).capitalize(), 'temperature': temp, 'country': country,
                'long': round(longitude, 2), 'lat': round(latitude, 2), 'humidity': humidity, 'wind_speed': wind_speed, 'icon': icon,
                'weather_condition': condition,
            }
        
    return render(request, 'weather-app/index.html', context)

