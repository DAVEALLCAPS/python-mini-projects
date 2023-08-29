# Denver Weather Data Fetcher

Weather Data Fetcher is a simple Python script that fetches and displays the current weather data for Denver, Colorado using the OpenWeatherMap API.

## Description

This application fetches current weather data for Denver, Colorado. It displays information such as the weather description, temperature, humidity, and atmospheric pressure.

## Libraries Used

- `os`: For accessing environment variables.
- `requests`: To make HTTP requests to the OpenWeatherMap API.
- `dotenv`: To load environment variables from an `.env` file.

## Features

- Fetches real-time weather data using OpenWeatherMap API.
- Displays weather description, temperature, humidity, and pressure.
- Uses environment variables for sensitive data (like API key) ensuring security.

## Installation & Setup

1. Install the required libraries:
    ```
    pip install requests python-dotenv
    ```
2. Create a `.env` file in the root directory and add your OpenWeatherMap API key:
    ```env
    OPENWEATHER_API_KEY=your_api_key_here
    ```
## Usage
After setup, simply run the script using:
    ```
    python denverweather.py
    ```
