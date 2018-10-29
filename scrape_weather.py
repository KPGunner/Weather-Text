import bs4 as bs
import pandas as pd
import urllib.request

page = urllib.request.urlopen('https://forecast.weather.gov/MapClick.php?lat=35.03126400000005&lon=-77.03440099999996')
soup = bs.BeautifulSoup(page.read(), 'html.parser')

temp = soup.find(class_='myforecast-current-lrg')
forecast = soup.find(class_='col-sm-10 forecast-text')

#print(temp.text)
#print(site.text)


message = f'The temperature right now is {temp.text}. Today it will be: {forecast.text}'

#print(message)



