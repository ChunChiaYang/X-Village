import json
import requests
import json
api_key = 'location/2306179'
url = 'https://www.metaweather.com/api/' + api_key
r = requests.get(url)
r.encoding = 'utf-8' 
weather=json.loads(r.text)
print(r.text)
print('='*60)
print(weather['consolidated_weather'][0]['weather_state_name'])

