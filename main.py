from flask import Flask, render_template, url_for, request
from cities import cities_list
from random import sample
from dotenv import load_dotenv
import requests
import os


load_dotenv()
app = Flask(__name__)
API_KEY = os.getenv('API_KEY')
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'


@app.post('/')
def query_weather_info_for_city():
    context = {}
    query = request.form.get('q')

    city = 'Nairobi'
    if request.method == 'POST':
        city = query
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

            context = [{
                'city': city, 
                'weather': str(weather).capitalize(), 
                'temperature': temp, 
                'country': country,
                'long': round(longitude, 4), 
                'lat': round(latitude, 4), 
                'humidity': humidity, 
                'wind_speed': wind_speed, 
                'icon': icon,
                'weather_condition': condition,
            }]
    
    return render_template('index.html', weather_info=context)


@app.get('/')
def select_random_cities():
    sampled_cities = []

    for c in sample(cities_list, k=3):
        request_url = f'{BASE_URL}?appid={API_KEY}&q={c}&units=metric'
        response = requests.get(request_url)
        json_data = response.json()
        sampled_cities.append(json_data)
        print(sampled_cities)
    
    return render_template('index.html', cities=sampled_cities)

