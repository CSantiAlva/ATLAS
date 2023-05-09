# This is the upated version of the weather scraping code that will he used to 
#run the streamlit app, I have updated so much, there is just a couple of things
#used HTML, this was simple code, then I was able to look at the edits that
# could be done on streamlit  
from PIL import Image
import requests
from bs4 import BeautifulSoup
import streamlit as st
import os

class WeatherForecast:
    
    def __init__(self):
        pass
    
    def fetch_forecast(self, url):
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        forecast_element = soup.find('div', {'id': 'seven-day-forecast'})
        return forecast_element
    
    def daily_forecast(self, forecast_element):
        daily_forecast_item = forecast_element.find_all(class_='tombstone-container')[0]
        period_name = daily_forecast_item.find(class_='period-name').get_text()
        short_desc = daily_forecast_item.find(class_='short-desc').get_text()
        temp = daily_forecast_item.find(class_='temp').get_text()
        temp_value = float(temp.split()[1])
        
        return period_name, short_desc, temp, temp_value
    
    def display_daily_weather(self, selected_city):
        if selected_city == "New Haven":
            url = 'https://forecast.weather.gov/MapClick.php?lat=41.308010000000024&lon=-72.92431999999997#.ZDOyaezMI6E'
            image_file = 'washington_dc.jpg'
        elif selected_city == "San Diego":
            url = 'https://forecast.weather.gov/MapClick.php?lat=32.7157&lon=-117.1617'
            image_file = 'washington_dc.jpg'
        elif selected_city == "New York":
            url = 'https://forecast.weather.gov/MapClick.php?lat=40.7145&lon=-74.0071'
            image_file = 'washington_dc.jpg'
        elif selected_city == "Chicago":
            url = 'https://forecast.weather.gov/MapClick.php?lat=41.8902&lon=-87.6979'
            image_file = 'washington_dc.jpg'
        elif selected_city == "Washington DC":
            url = 'https://forecast.weather.gov/MapClick.php?lat=38.8904&lon=-77.032'
            image_file = 'washington_dc.jpg'
        image_path = os.path.join('images', image_file)
        if os.path.exists(image_path):
            image = Image.open(image_path)
            st.image(image, use_column_width=True) 

        forecast_element = self.fetch_forecast(url)
        period_name, short_desc, temp, temp_value = self.daily_forecast(forecast_element)
        
        st.write(period_name)
        st.write(short_desc)
        st.write(temp)
        if temp_value < 50:
            st.write("It's going to be cold today, you might want to wear a sweater!")
        elif temp_value == 35:
            st.write("Chill out, don't be so dramatic!")
        elif temp_value > 50:
            st.write("It seems a bit warm, I reccommend a light sweater and bright colors for a pretty day")

    def run(self):
        st.title("Weather Forecast")
    
        selected2 = st.radio("Here is your Daily Forecast", ("Daily Weather",))
    
        if selected2 == "Daily Weather":
            st.title(f"Select a City from the Options Below to View Today's Forecast")
            selected_city = st.button("New Haven")
            if selected_city:
                self.display_daily_weather("New Haven")
            selected_city = st.button("San Diego")
            if selected_city:
                self.display_daily_weather("San Diego")
            selected_city = st.button("New York")
            if selected_city:
                self.display_daily_weather("New York")
            selected_city = st.button("Chicago")
            if selected_city:
                self.display_daily_weather("Chicago")
            selected_city = st.button("Washington DC")
            if selected_city:
                self.display_daily_weather("Washington DC")

if __name__ == "__main__":
    weather_forecast = WeatherForecast()
    weather_forecast.run()