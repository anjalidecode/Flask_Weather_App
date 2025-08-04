from flask import Flask, request, jsonify, render_template
import requests
from utils import get_weather_url
from dotenv import load_dotenv

load_dotenv() 

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city')
    if not city:
        return jsonify({'error': 'City parameter is missing'}), 400
         
    url = get_weather_url(city)
    print(url)    
    
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        weather_info = {
            'city': data['name'],
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description'],
            'icon': data['weather'][0]['icon']
        }
        return jsonify(weather_info)
    else:
        return jsonify({'error': 'City not found'}), 404

if __name__ == '__main__':
    app.run(debug=True, port=3000)