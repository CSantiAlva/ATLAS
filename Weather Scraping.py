#!/usr/bin/env python
# coding: utf-8

# In[3]:


import requests
from bs4 import BeautifulSoup

# Specify the URL of the weather forecast page for your location
url = 'https://forecast.weather.gov/MapClick.php?lat=41.308010000000024&lon=-72.92431999999997#.ZDOyaezMI6E'

# Send a GET request to the URL and parse the HTML content
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Send a GET request to the forecast URL and parse the HTML content
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Find the HTML element that contains the forecast data
forecast_element = soup.find('div', {'id': 'seven-day-forecast'})

# Extract the daily forecast item
daily_forecast_item = forecast_element.find_all(class_='tombstone-container')[0]

# Extract the name of the period (e.g. 'Today', 'Tonight', etc.)
period_name = daily_forecast_item.find(class_='period-name').get_text()

# Extract the short description of the forecast (e.g. 'Mostly Sunny')
short_desc = daily_forecast_item.find(class_='short-desc').get_text()

# Extract the temperature range for the period (e.g. 'High: 70 °F')
temp = daily_forecast_item.find(class_='temp').get_text()

# Extract the temperature value as a float
temp_value = float(temp.split()[1])

# Print the forecast information
print(period_name)
print(short_desc)
print(temp)

# `Make a recommendation if the temperature is below 50 degrees Fahrenheit
if temp_value < 50:
    print("It's going to be cold today, you might want to wear a sweater!")
# Make a recommendation if the temperature is below 50 degrees Fahrenheit
if temp_value == 35:
    print("chill out don't be so dramatic woman")
    
# Make a recommendation if the temperature is below 50 degrees Fahrenheit
if temp_value > 50:
    print("Hot as balls, suns out buns out")

