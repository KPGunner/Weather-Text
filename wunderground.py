import requests
import json
import urllib

w = urllib.request.urlopen('http://api.wunderground.com/api/73215ad820eff503/forecast/q/CA/New_Bern.json')

string = w.read()
parsed = json.loads(string)

## Morning ##
cond_morn = parsed['forecast']['simpleforecast']['forecastday'][0]['conditions']
cond_morn_ht = parsed['forecast']['simpleforecast']['forecastday'][0]['high']['fahrenheit']
cond_morn_lt = parsed['forecast']['simpleforecast']['forecastday'][0]['low']['fahrenheit']

## Afternoon ##
cond_aft = parsed['forecast']['simpleforecast']['forecastday'][1]['conditions']
cond_aft_ht = parsed['forecast']['simpleforecast']['forecastday'][1]['high']['fahrenheit']
cond_aft_lt = parsed['forecast']['simpleforecast']['forecastday'][1]['low']['fahrenheit']



x = (f'This morning there is {cond_morn}, the high is {cond_morn_ht} and the low is {cond_morn_lt}. ')
y = (f'This afternoon there is {cond_aft}, the high is {cond_aft_ht} and the low is {cond_aft_lt}.')

message = (x + y)

print(message)

# w = requests.get('http://api.wunderground.com/api/73215ad820eff503/forecast/q/CA/New_Bern.json').json()
#
# string = w.read()
#
# parsed = json.loads(string)
#
# cond_morn = parsed['forecast']['simpleforecast']['forecastday'][0]['conditions']
#
# print(cond_morn)


# print(weather)


# def weather_parse():
#     for (k, v) in weather.items():
#         print('Key: ' + k)
#         print('Value: ' + str(v))
#
#
# weather_parse()

# def message_body():
#     for (k, v) in weather.items():
#         print(k)
#         print(v['title']['fcttext'])
#
# message_body()


# def weather_parse():
#     for day in weather['forecast']['simpleforecast']['forecastday']:
#         print(day['date']['weekday'])
#         print("Conditions: ", day['conditions'])
#         print("High: ", day['high']['fahrenheit'] + "F", "Low: ", day['low']['fahrenheit'] + "F")
#
#
#
# weather_parse()



