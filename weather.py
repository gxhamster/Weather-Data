from urllib.request import urlopen
import json

WEATHER_DATA_SAMPLE = 'http://samples.openweathermap.org/data/2.5/weather?lat=35&lon=139&appid=b6907d289e10d714a6e88b30761fae22'

API_KEY = 'c96942b84298788e25e726d0532f4ad1'
COORDINATES = 'http://ipinfo.io/'
WEATHER_DATA = 'http://samples.openweathermap.org/data/2.5/weather?'

def parse_json(url):
    try:
        json_data = {}
        request = urlopen(url)
        data = request.read().decode('utf-8')
        json_data = json.loads(data)

        return json_data
    except Exception as ex:
        print('Could not fetch data due to ', ex)

# Get latitide and longitude
def getCoordinates(url):
    data = parse_json(url)
    latitude, longitude = data['loc'].split(',')

    return [latitude, longitude]

def getWeatherData(url, coordinates, key):
    latitude, longitude = coordinates
    weatherData = {}
    url = url + 'lat={}&lon={}&appid={}'.format(latitude, longitude, key)
    data = parse_json(url)
    weather = data['weather'][0]
    dataNums = data['main']
    weatherData.setdefault('weather', weather)
    weatherData.setdefault('main', dataNums)

    return weatherData

def printWeatherData(url, coordinates, key):
    weatherData = getWeatherData(url, coordinates, key)
    # Print data in nice way
    print('WEATHER DATA'.center(20 + 15, '-'))
    for k, v in weatherData['main'].items():
        print(k.ljust(20, ' ') + str(v).rjust(15))



# print(getCoordinates(COORDINATES))
# print(getWeatherData(WEATHER_DATA, getCoordinates(COORDINATES), API_KEY))
printWeatherData(WEATHER_DATA, getCoordinates(COORDINATES), API_KEY)
