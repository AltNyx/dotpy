import json
import requests
import os
from datetime import datetime


def forecast(data):
    if 'message' in data:
        print(data['message'])
        return

    KELVIN = 273.15
    DEGREE = "\u00B0"
    weather = data['weather'][0]['description']
    temp = data['main']['temp'] - KELVIN
    feels_like = data['main']['feels_like'] - KELVIN
    sunrise = datetime.fromtimestamp(data['sys']['sunrise']).time()
    sunset = datetime.fromtimestamp(data['sys']['sunset']).time()

    print()
    print(f'Weather: {weather}')
    print(f'Temp: {temp:.2f}{DEGREE}C')
    print(f'Feels Like: {feels_like:.2f}{DEGREE}C')
    print(f'Sunrise: {sunrise}')
    print(f'Sunset: {sunset}')


def main():
    # Enter your api key
    API_KEY = os.getenv("WEATHER")

    city = input("Enter city: ")
    url = f'http://api.openweathermap.org/data/2.5/weather?appid={API_KEY}&q={city}'

    response = requests.get(url)
    data = response.json()
    forecast(data)


if __name__ == "__main__":
    main()
