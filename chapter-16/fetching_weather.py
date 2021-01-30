import json
import requests
import sys
import config

# Reads the requested location from the command line
# 2. Downloads JSON weather data from OpenWeatherMap.org
# 3. Converts the string of JSON data to a Python data structure
# 4. Prints the weather for today and the next two days
# So the code will need to do the following:
# 1. Join strings in sys.argv to get the location.
# 2. Call requests.get() to download the weather data.
# 3. Call json.loads() to convert the JSON data to a Python data structure.
# 4. Print the weather forecast.

APPID = config.APP_ID

# the sys.argv reads the command line parameters, the first one is the script name itself
# if we don't receive more than one parameter, then just exit the program
if(len(sys.argv) < 2):
    print('Usage: getOpenWeather.py city_name, 2-letter_country_code')
    sys.exit()

# we are going to join the parameters into a single string variable slicing from the first argument
location = ' '.join(sys.argv[1:])
print(location)

url = f'https://api.openweathermap.org/data/2.5/forecast/daily?q={location}&appid={APPID}'
print(f'Request URL: [{url}]')

try:
    response = requests.get(url)

    # returns an HTTPError object if an error has occurred during the process.
    # It is used for debugging the requests module and is an integral part of Python requests.
    response.raise_for_status()
    print(response.text)
except requests.exceptions.RequestException as e:
    print(f'Request Exception while trying to retrieve data -> {e}')
