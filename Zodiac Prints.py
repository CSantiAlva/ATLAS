#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Define a mapping of zodiac signs to the ranges of dates that correspond to them
zodiac_dates = {
    "Aries":    ("03-21", "04-19"),
    "Taurus":   ("04-20", "05-20"),
    "Gemini":   ("05-21", "06-20"),
    "Cancer":   ("06-21", "07-22"),
    "Leo":      ("07-23", "08-22"),
    "Virgo":    ("08-23", "09-22"),
    "Libra":    ("09-23", "10-22"),
    "Scorpio":  ("10-23", "11-21"),
    "Sagittarius": ("11-22", "12-21"),
    "Capricorn": ("12-22", "01-19"),
    "Aquarius": ("01-20", "02-18"),
    "Pisces":   ("02-19", "03-20")
}


# In[3]:


import requests
from bs4 import BeautifulSoup
from datetime import datetime

# Define a mapping of zodiac signs to the daily horoscope URLs
zodiac_links = {
    "Aries":    "https://www.elle.com/horoscopes/daily/a60/aries-daily-horoscope/",
    "Taurus":   "https://www.elle.com/horoscopes/daily/a98/taurus-daily-horoscope/",
    "Gemini":   "https://www.elle.com/horoscopes/daily/a99/gemini-daily-horoscope/",
    "Cancer":   "https://www.elle.com/horoscopes/daily/a100/cancer-daily-horoscope/",
    "Leo":      "https://www.elle.com/horoscopes/daily/a101/leo-daily-horoscope/",
    "Virgo":    "https://www.elle.com/horoscopes/daily/a102/virgo-daily-horoscope/",
    "Libra":    "https://www.elle.com/horoscopes/daily/a103/libra-daily-horoscope/",
    "Scorpio":  "https://www.elle.com/horoscopes/daily/a104/scorpio-daily-horoscope/",
    "Sagittarius": "https://www.elle.com/horoscopes/daily/a105/sagittarius-daily-horoscope/",
    "Capricorn": "https://www.elle.com/horoscopes/daily/a106/capricorn-daily-horoscope/",
    "Aquarius": "https://www.elle.com/horoscopes/daily/a107/aquarius-daily-horoscope/",
    "Pisces":   "https://www.elle.com/horoscopes/daily/a108/pisces-daily-horoscope/"
}

# Define a function to find the zodiac sign for a given date
def get_zodiac_sign(birthday):
    month, day = birthday.split("-")
    date_str = f"{month}-{day}"
    for sign, (start, end) in zodiac_dates.items():
        if start <= date_str <= end:
            return sign
    raise ValueError("Invalid date")

# Ask the user for their birthday
birthday = input("Enter your birthday (MM-DD): ")
try:
    sign = get_zodiac_sign(birthday)
except ValueError:
    print("Invalid date")
else:
    # Get the URL for the daily horoscope page for the user's sign and parse the HTML
    url = zodiac_links[sign]
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
   
    # Find the <p> tag that contains the horoscope message and print it (if it exists)
    message = soup.find('p', {'class': 'css-18vfmjb et3p2gv0'})
    if message is not None:
        current_hour = datetime.now().hour
        if current_hour < 12:
            greeting = "Good mythical morning"
        elif current_hour < 18:
            greeting = "Goooood pretty afternoon"
        else:
            greeting = "Good mistyy evening"
        print(f"{greeting} {sign}, here is your daily horoscope:")
        print(message.get_text().strip())
    else:
        print("Sorry, the oracle does not speak today.")

