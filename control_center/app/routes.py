from flask import Flask, render_template, jsonify
import requests
import os
import datetime
from dotenv import load_dotenv  # Import the load_dotenv function

# Load environment variables from the .env file
load_dotenv()

app = Flask(__name__)

BASE_URL = 'https://api.open-meteo.com/v1/forecast'

@app.route("/")
def index():
    # Load latitude and longitude from environment variables
    latitude = os.getenv("HOME_LATITUDE")
    longitude = os.getenv("HOME_LONGITUDE")

    params = {
        'latitude': latitude,  # Use the loaded latitude
        'longitude': longitude,  # Use the loaded longitude
        'hourly': 'temperature_2m,apparent_temperature,precipitation,windspeed_10m',
        'temperature_unit': 'fahrenheit',
        'windspeed_unit': 'mph',
        'timezone': 'auto',
        'forecast_days': 1
    }

    response = requests.get(BASE_URL, params=params)

    data = response.json()

    # Check if 'hourly' key exists in the data
    if 'hourly' not in data:
        return render_template('error.html', message="Unexpected data format from the weather API.")

    # Create a dictionary that matches the expected format in the template
    desired_hours = [8, 12, 16, 20]
    simple_time_mapping = {
        8: "8AM",
        12: "12PM",
        16: "4PM",
        20: "8PM"
    }

    weather_data = {
        'time': [simple_time_mapping[hour] for hour in desired_hours],
        'temperature_2m': [data['hourly']['temperature_2m'][hour] for hour in desired_hours],
        'precipitation': [data['hourly'].get('precipitation', [0]*24)[hour] for hour in desired_hours],
        'windspeed_10m': [data['hourly']['windspeed_10m'][hour] for hour in desired_hours]
    }

    # Get the current date and format it
    current_date = datetime.datetime.now().strftime("%A, %B %d, %Y")

    return render_template('dashboard.html', weather=weather_data, date=current_date)

if __name__ == '__main__':
    app.run(debug=True)
