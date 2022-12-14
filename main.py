import pandas as pd
import requests
from bs4 import BeautifulSoup

page = requests.get(
    'https://forecast.weather.gov/MapClick.php?lat=36.3741&lon=-119.2702#.YWCMzdpByMo')
soup = BeautifulSoup(page.content, 'html.parser')
week = soup.find(id='seven-day-forecast-body')

items = week.find_all(class_='tombstone-container')

# print(items[0].find(class_='period-name').get_text())
# print(items[0].find(class_='short-desc').get_text())
# print(items[0].find(class_='temp').get_text())

period_names = [item.find(class_='period-name').get_text() for item in items]
short_desc = [item.find(class_='short-desc').get_text() for item in items]
temp = [item.find(class_='temp').get_text() for item in items]
# print(period_names)
# print(short_desc)
# print(temp)

weather_stuff = pd.DataFrame(
    {
        'Period': period_names,
        'Short_Desc': short_desc,
        'Temp': temp,
    }
)

print(weather_stuff)
# weather_stuff.to_csv('weather.csv')
