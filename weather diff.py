import requests

def get_weather(city):
    api_key = 'YOUR_API_KEY'  # Replace with your OpenWeatherMap API key
    base_url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        weather_data = response.json()
        temperature = weather_data['main']['temp']
        weather_desc = weather_data['weather'][0]['description']
        return temperature, weather_desc
    except requests.exceptions.RequestException as e:
        print('Error:', e)
        return None

# Current city
current_city = 'Your City'

print(f"Weather for {current_city}:")
current_temp, current_desc = get_weather(current_city)
if current_temp and current_desc:
    print(f'Temperature: {current_temp}°C')
    print(f'Description: {current_desc}')
else:
    print('Failed to fetch weather data for the current city.')

# Hong Kong
hongkong_city = 'Hong Kong'

print(f"\nWeather for {hongkong_city}:")
hongkong_temp, hongkong_desc = get_weather(hongkong_city)
if hongkong_temp and hongkong_desc:
    print(f'Temperature: {hongkong_temp}°C')
    print(f'Description: {hongkong_desc}')
else:
    print('Failed to fetch weather data for Hong Kong.')

# Calculate temperature difference
if current_temp and hongkong_temp:
    temp_diff = current_temp - hongkong_temp
    print(f"\nTemperature difference between {current_city} and {hongkong_city}: {temp_diff}°C")
