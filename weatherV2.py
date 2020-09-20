import requests
from datetime import date
from secret import API_KEY
import sys


def current_weather(city):
    url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}"
    response = requests.get(url)
    data = response.json()

    if "error" in data:
        return None

    res = {}

    # Location details
    location = data['location']
    city, state, country = location['name'], location['region'], location['country']

    res['Location'] = {'City': city, 'State': state, 'Country': country}

    # Weather
    condition = data['current']['condition']
    desc, icon = condition['text'], "https:" + condition['icon']

    res['Weather'] = {'Description': desc, 'Icon': icon}

    # Numbers
    degree = u"\N{DEGREE SIGN}"

    temp = data['current']
    current = f"{temp['temp_c']}{degree}C"
    wind = f"{temp['wind_kph']} kmph"
    pressure = f"{temp['pressure_mb']} mbar"
    feels_like = f"{temp['feelslike_c']}{degree}C"

    res['Numbers'] = {'Current': current,
                      'Feels Like': feels_like, 'Wind Speed': wind, 'Pressure': pressure}

    return res


def astronomy(city):
    today = date.today()
    url = f"https://api.weatherapi.com/v1/astronomy.json?key={API_KEY}&q={city}&dt={today}"
    response = requests.get(url)
    data = response.json()

    if "error" in data:
        return None

    # Astronomy
    astro = data['astronomy']['astro']
    sunrise, sunset, moonrise, moonset = astro['sunrise'], astro['sunset'], astro['moonrise'], astro['moonset']
    res = {'Sunrise': sunrise, 'Sunset': sunset,
           'Moonrise': moonrise, 'Moonset': moonset}
    return res


city = input("Enter city: ")
weather = current_weather(city)
astro = astronomy(city)


if not weather or not astro:
    print("Invalid city!")
    sys.exit()

print("-"*70)
for head, sub in weather.items():
    if isinstance(sub, dict):
        print(f"{head}\n")
        for name, value in sub.items():
            print(f"{name}: {value}")
        print()
    else:
        print(f"{head}: {sub}")

print("-"*70)

for name, value in astro.items():
    print(f"{name}: {value}")

print("-"*70)
