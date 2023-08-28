import os
import requests
from dotenv import load_dotenv

load_dotenv()  # This loads the environment variables from the .env file

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather_data(lat, lon, api_key):
    """
    Fetches weather data for the provided latitude and longitude.
    """
    params = {
        'lat': lat,
        'lon': lon,
        'appid': api_key,
        'units': 'imperial'
    }
    
    response = requests.get(BASE_URL, params=params)
    
    if response.status_code != 200:
        print("Failed to retrieve data.")
        return None

    return response.json()

def main():
    API_KEY = os.environ.get('OPENWEATHER_API_KEY')

    lat = 39.73
    lon = -104.99

    weather_data = get_weather_data(lat, lon, API_KEY)

    if weather_data:
        main_info = weather_data['main']
        weather_info = weather_data['weather'][0]
        
        print(f"Weather: {weather_info['description'].capitalize()}")
        print(f"Temperature: {main_info['temp']}°F")
        print(f"Humidity: {main_info['humidity']}%")
        print(f"Pressure: {main_info['pressure']} hPa")

if __name__ == "__main__":
    main()
