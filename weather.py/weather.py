import requests
from datetime import date
from typing import Optional
from dataclasses import dataclass


BASE = "http://api.weatherapi.com"
WEATHER_API = 'YOUR-WEATHER-API-KEY'
# Get key from https://www.weatherapi.com/


@dataclass
class Weather:
    loc: str
    desc: str
    icon: str
    curr: str
    wind: str
    pressure: str
    feels: str


@dataclass
class Astro:
    sunrise: str
    sunset: str
    moonrise: str
    moonset: str


def current_weather(city: str) -> Optional[Weather]:
    ''' Get the current weather of any city

    Example:

    >>> current_weather('New york') 
    Weather(loc='New York, New York', 
            desc='Overcast', 
            icon='https://cdn.weatherapi.com/weather/64x64/day/122.png', 
            curr='6.7°C', 
            wind='0.0 kmph', 
            pressure='1009.0 mbar', 
            feels='3.6°C'
           )
    '''
    weather_url = BASE + f"/v1/current.json?key={WEATHER_API}&q={city}"
    response = requests.get(weather_url)
    data = response.json()

    if "error" in data:
        return None

    location = data['location']
    condition = data['current']['condition']
    degree = u"\N{DEGREE SIGN}"
    temp = data['current']

    return Weather(
        loc=f"{location['name']}, {location['region']}",
        desc=condition['text'],
        icon=f"https:{condition['icon']}",
        curr=f"{temp['temp_c']}{degree}C",
        wind=f"{temp['wind_kph']} kmph",
        pressure=f"{temp['pressure_mb']} mbar",
        feels=f"{temp['feelslike_c']}{degree}C"
    )


def astronomy(city: str) -> Optional[Astro]:
    ''' Get the astro details of any city

    Example:

    >>> astronomy('New york')
    Astro(sunrise='06:14 AM', 
          sunset='07:38 PM',
          moonrise='09:27 AM', 
          moonset='12:11 AM'
         )
    '''
    today = date.today()
    url = BASE + f"/v1/astronomy.json?key={WEATHER_API}&q={city}&dt={today}"
    response = requests.get(url)
    data = response.json()

    if "error" in data:
        return None

    astro = data['astronomy']['astro']

    return Astro(
        sunrise=astro['sunrise'],
        sunset=astro['sunset'],
        moonrise=astro['moonrise'],
        moonset=astro['moonset']
    )


def apod() -> Optional[str]:
    '''Returns a url of the astronomy picture of the day

    Example:

    >>> apod()
    'https://apod.nasa.gov/apod/image/2104/FlamenebulaIR1024.jpg'
    '''
    NASA_API = 'YOUR-NASA-API-KEY'
    # Get key from https://api.nasa.gov/
    url = f"https://api.nasa.gov/planetary/apod?api_key={NASA_API}"
    response = requests.get(url)
    return response.json()['url'] if response.ok else None
