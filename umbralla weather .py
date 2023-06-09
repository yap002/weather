import requests
import smtplib

def check_weather(city):
    # Replace 'YOUR_API_KEY' with your actual API key from OpenWeatherMap
    api_key = 'YOUR_API_KEY'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    response = requests.get(url)
    weather_data = response.json()

    if response.status_code == 200:
        # Extract the weather condition
        weather_condition = weather_data['weather'][0]['main']
        return weather_condition
    else:
        print(f"Error: {response.status_code}")
        return None

def send_email(to_address, subject, body):
    # Replace the placeholder values with your email and SMTP server details
    from_address = 'your_email@example.com'
    smtp_server = 'smtp.example.com'
    smtp_port = 587
    username = 'your_username'
    password = 'your_password'

    message = f"Subject: {subject}\n\n{body}"

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(username, password)
        server.sendmail(from_address, to_address, message)
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error sending email: {e}")

def main():
    city = input("Enter the city name: ")
    weather_condition = check_weather(city)

    if weather_condition is not None:
        if weather_condition.lower() == 'rain':
            subject = 'Umbrella Reminder'
            body = f"Don't forget to bring an umbrella today in {city}!"
        else:
            subject = 'Weather Update'
            body = f"The weather in {city} today does not require an umbrella."

        to_address = input("Enter your email address: ")
        send_email(to_address, subject, body)

if __name__ == '__main__':
    main()
