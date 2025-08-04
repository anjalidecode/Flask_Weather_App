import os

def get_weather_url(city: str):

    API_KEY = os.getenv("API_KEY")  

    return f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    
   