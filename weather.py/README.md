# weather

Get weather asap.

## Usage

```python
from weather import current_weather
from weather import astronomy
from weather import apod


>>> current_weather('New york')
    Weather(loc='New York, New York',
            desc='Overcast',
            icon='https://cdn.weatherapi.com/weather/64x64/day/122.png',
            curr='6.7°C',
            wind='0.0 kmph',
            pressure='1009.0 mbar',
            feels='3.6°C'
           )


>>> astronomy('New york')
Astro(sunrise='06:14 AM',
      sunset='07:38 PM',
      moonrise='09:27 AM',
      moonset='12:11 AM'
    )


>>> apod()
'https://apod.nasa.gov/apod/image/2104/FlamenebulaIR1024.jpg'
```
