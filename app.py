from flask import Flask, request, jsonify, render_template
import requests
from utils import get_weather_url
from dotenv import load_dotenv
from db import init_db, get_cached_weather, save_weather

load_dotenv()
init_db()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# Searched City Weather
@app.route('/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city')
    if not city:
        return jsonify({'error': 'City parameter is missing'}), 400

    cached_data = get_cached_weather(city, table="searched_cities")
    if cached_data:
        return jsonify({
            'city': cached_data['city'].title(),
            'temperature': cached_data['temperature'],
            'description': cached_data['description'],
            'icon': cached_data['icon']
        })

    url = get_weather_url(city)
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        weather_info = {
            'city': data['name'],
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description'],
            'icon': data['weather'][0]['icon']
        }

        save_weather(
            weather_info['city'],
            weather_info['temperature'],
            weather_info['description'],
            weather_info['icon'],
            table="searched_cities"
        )

        return jsonify(weather_info)
    else:
        return jsonify({'error': 'City not found'}), 404

# Added City Weather
@app.route('/add-weather', methods=['GET'])
def add_weather():
    city = request.args.get('city')
    if not city:
        return jsonify({'error': 'City parameter is missing'}), 400

    cached_data = get_cached_weather(city, table="added_cities")
    if cached_data:
        return jsonify({
            'city': cached_data['city'].title(),
            'temperature': cached_data['temperature'],
            'description': cached_data['description'],
            'icon': cached_data['icon']
        })

    url = get_weather_url(city)
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        weather_info = {
            'city': data['name'],
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description'],
            'icon': data['weather'][0]['icon']
        }

        save_weather(
            weather_info['city'],
            weather_info['temperature'],
            weather_info['description'],
            weather_info['icon'],
            table="added_cities"
        )

        return jsonify(weather_info)
    else:
        return jsonify({'error': 'City not found'}), 404

if __name__ == '__main__':
    app.run(debug=True, port=3000)
