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
    data = json.loads(response.text)

    if response.status_code == 200:
        weather_data = {
            "Temperature": data["main"]["temp"],
            "Humidity": data["main"]["humidity"],
            "Description": data["weather"][0]["description"],
            "Wind Speed": data["wind"]["speed"]
        }
        return weather_data
    else:
        print("Error occurred:", data["message"])
        return None

# Replace "YOUR_API_KEY" with your actual API key from OpenWeatherMap
api_key = "YOUR_API_KEY"
city_name = input("Enter city name: ")
weather_info = get_weather(api_key, city_name)

if weather_info:
    print("Weather Information for", city_name)
    for key, value in weather_info.items():
        print(key + ":", value)
