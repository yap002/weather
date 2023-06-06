import requests
import json

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    if data["cod"] == "404":
        print("City not found.")
        return

    weather = {
        "temperature": data["main"]["temp"],
        "description": data["weather"][0]["description"],
        "humidity": data["main"]["humidity"],
        "wind_speed": data["wind"]["speed"],
    }

    return weather

# Set your OpenWeatherMap API key
API_KEY = "YOUR_API_KEY"

# Enter the city name for which you want to check the weather
city_name = input("Enter city name: ")

# Get the weather data
weather_data = get_weather(API_KEY, city_name)

# Print the weather information
if weather_data:
    print(f"\nWeather in {city_name}:")
    print(f"Temperature: {weather_data['temperature']}°C")
    print(f"Description: {weather_data['description']}")
    print(f"Humidity: {weather_data['humidity']}%")
    print(f"Wind Speed: {weather_data['wind_speed']} m/s")
