#This is the initial list of packages and imports that will be used for this WebApp.
import streamlit as st 
import time
import threading
import platform
from playsound import playsound
import datetime
from datetime import datetime, timedelta
import time
from streamlit_option_menu import option_menu
from PIL import Image, ImageDraw, ImageFont
import os
import multiprocessing
from bs4 import BeautifulSoup
from datetime import datetime
from pydub import AudioSegment
from pydub.playback import play
from PIL import Image
import requests
from datetime import datetime
from WeatherScrapingFinal import WeatherForecast

# While it may seem like this .py file may be out of order, for the sake of the streamlit app
# keeping this .py in a particular order will directly change the layout of the website.

# Zodiac Dates: Preliminarily setting up date definitions for one of our features of the app.
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
# Zodiac Links: Using the .get, linking the zodiacs to their specific website was easier to code
# rather than coding a program that would read a navigate the sites.
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
#Oracle_Message: This is the attached message that will appear before the Zodiac cards, while this is not 
# ideal placement for pretty code, again, streamlit is restrictive and sensitive when it comes to arranging and creative permissions.
oracle_message = """ 
		Greetings, seekers of knowledge and enlightenment! I, the Oracle of the morning, 
    	offer thee free horoscopes for the day. 
    	Behold, and click on thy zodiac sign below to unlock the secrets of the universe. The movements of the stars and planets have an omnipotent influence on our daily lives, shaping our destinies and illuminating our paths. 
    	By delving into the mystical realm of the cosmos, we gain insights into the grand design of the universe and discover our true purpose.
		As you embark on your journey today, let the wisdom of the stars guide you. 
		Unravel the cosmic mysteries that lie before you and unlock the power of the universe. 
		For within these horoscopes lies the key to your destiny, and the knowledge to unlock your full potential.
		So heed the call of the cosmos, and let your zodiac sign lead you to the truth. For in the mystical realm of the stars, all things are possible, and the power of the universe is at your fingertips.
		"""

#This is where we begin the creating of our horoscope function. This is an iteration of the original definition from the notebooks.
def get_daily_horoscope(sign):
    response = requests.get(zodiac_links[sign])
    soup = BeautifulSoup(response.text, "html.parser") #html.parser is making it easier to read the website and pull apart the pieces you need.
    message = soup.find('p', {'class': 'css-18vfmjb et3p2gv0'}) # after that, this is where we can draw from the divisions it found.
    # employed the use of elif as a short cut to else if, picking up every new trick to code, lets see how this makes coding run.
    if message is not None:
        current_hour = datetime.now().hour
        if current_hour < 12:
            greeting = "Good mythical morning"
        elif current_hour < 18:
            greeting = "Goooood pretty afternoon"
        else:
            greeting = "Good mistyy evening"
        return f"{greeting} {sign}, here is your daily horoscope:\n\n{message.get_text().strip()}" #this is where I try merging text with a text strip
    else:
        return "Sorry, the oracle does not speak today."

#crazy html style syntax that will allow me to edit streamlit as much as possible
zodiac_title = '<center><span style="font-family:MedievalSharp; font-size:25px; font-weight:bold;">Choose Your Zodiac Sign</span></center>'

def daily_zodiac():
    st.header("Daily Zodiac") #integration of streamlit as we begin with the 'st.' commands, this is what translates into streamlit
    st.write(oracle_message)
    st.markdown(zodiac_title, unsafe_allow_html= True) 

    zodiac_signs = list(zodiac_links.keys())
    buttons = [st.columns(3) for _ in range(4)]

    clicked_sign = None

    for i, sign in enumerate(zodiac_signs):
        with buttons[i // 3][i % 3]:
            image = Image.open(f"zodiac_images/{sign}.jpg")
            st.image(image, use_column_width=True)
            if st.button(sign):
                clicked_sign = sign

    if clicked_sign:
        horoscope = get_daily_horoscope(clicked_sign)
        st.markdown(
            f"""
            <style>
                .horoscope-textbox {{
                    font-family: 'Roboto', sans-serif;
                    font-size: 16px;
                    color: #333;
                    padding: 20px;
                    border: 1px solid #ccc;
                    border-radius: 10px;
                    background-color: #f9f9f9;
                    box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.1);
                }}
            </style>
            <div class='horoscope-textbox'>
                {horoscope}
            </div>
            """,
            unsafe_allow_html=True
        ) #this was a standard code that would help with the editing fo fonts and size, so this is the same one pasted all over the app.

#failed attempt at creating a 'post it wall' using streamlit. It has trouble with loops and having more that 1 button function per page.
def notes_app():
    st.title("Notes/Reminders App")
    tasks = {}
    for i in range(1, 6):
            note_input = st.text_input(f"Power Task {i}:")
            if note_input:
                tasks[f"Power Task {i}"] = note_input
    if tasks:
            st.write("Your reminders for today:")
            for task, note in tasks.items():
                st.write(f"{task}: {note}")



# MARKING BEGINING OF ALARM CODE :
# The dictionary that will be used to call the audio files.
audio_files = {
    'sound_1': {'file': 'alarm_sounds/sound_1.mp3', 'duration': 5},
    'sound_2': {'file': 'alarm_sounds/sound_2.mp3', 'duration': 5},
    'sound_3': {'file': 'alarm_sounds/sound_3.mp3', 'duration': 5},
    'sound_4': {'file': 'alarm_sounds/sound_4.mp3', 'duration': 5}
}

def play_alarm(sound_file):
    playsound(sound_file)
def alarm_app():
    # set default values
    default_audio = 'sound_1'
    alarm_time = st.time_input('Set a timer (set in 15 minute intervals)', value=(datetime.now().time()))

    audio_selection = st.selectbox('Select alarm sound:', list(audio_files.keys()), index=0)

    if st.button('Preview'):
        play_alarm(audio_files[audio_selection]['file'])

    # Alarm logic
    alarm_set = st.button('Set Alarm')
    snooze_button = st.empty()
    alarm_message = st.empty()
    time_remaining = st.empty()
    
    if alarm_set:
        alarm_datetime = datetime.combine(datetime.today(), alarm_time)
        p = None  # We will use this to store our process
        while True:
            now = datetime.now()
            if now >= alarm_datetime:
                if p:  # If a sound is already playing, this will stop it before starting a new one
                    p.terminate()
                    p.join()
                p = multiprocessing.Process(target=play_alarm, args=(audio_files[audio_selection]['file'],))
                p.start()
                alarm_message.text("Time's up!")
                snooze = snooze_button.button('Snooze')
                if snooze:
                    p.terminate()  # Stop the sound
                    p.join()
                    alarm_message.text("Snoozing for 5 minutes.")
                    alarm_datetime = now + timedelta(minutes=5)
                    break  # Exit the loop after snoozing
                else:
                    break  # Exit the loop if snooze is not clicked
            else:
                time_remaining.text(f"Time remaining: {(alarm_datetime - now).seconds // 60} minutes")
            time.sleep(1)

# using 'st.sidebar' is what allows you to create multiple pages on streamlit
with st.sidebar:
    selected = option_menu("Welcome to A-T-L-A-S", ["Homepage", 'A-T-L-A-S' ,'Settings', 'FAQ'], 
        icons=['house', 'gear'], menu_icon="cast", default_index=1,
        styles={
        "nav-link": {"font-size": "25px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "purple"},
    }
)
    selected
if selected == "Homepage":
	st.title (" The A-T-L-A-S Alarm System")
	st.markdown(
    """
    <style>
        .textbox {
            font-family: 'Roboto', sans-serif;
            font-size: 16px;
            color: #333;
            padding: 20px;
            border: 1px solid #ccc;
            border-radius: 10px;
            background-color: #f9f9f9;
            box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.1);
        }
    </style>
     <div class='textbox'>
        <p> The ATLAS cre welcomes you onboard, we are delighted to hear you have decided to
        wake up with ATLAS now! </p>
        <p>Welcome to A-T-L-A-S, your ultimate personal assistant! 
        We are thrilled to introduce you to our cutting-edge project and your first look at Python code through Streamlit. 
        Our app functions as an alarm, providing you with timely wake-up calls. But that's just the beginning! 
        A-T-L-A-S can also keep you updated on your daily horoscope, provide you with the latest weather updates, and help you stay on top of your daily tasks with customizable reminders. 
        We are excited for you to experience the power of A-T-L-A-S and simplify your life like never before. </p>
    </div>

    """,
    unsafe_allow_html=True
)
# Because we already used sidebar, streamlit did not allow the same command twice, so our way around this
# was creating more sub-pages! Along with the 'if', this is what would make them buttons, and attach commands to the buttons as well.
if selected == 'A-T-L-A-S' :
	st.title(f" The {selected} Alarm System")
	selected2 = option_menu("Look into the Hands of ATLAS", ["Alarms", "Daily Reminders", 'Daily Zodiac', 'Daily Weather'], 
	    icons=['house', 'list-task', "circle", 'cirlce', 'cirlce', 'circle', 'circle', 'circle'], 
	    menu_icon="cast", default_index=0, orientation="horizontal",
        styles={
	        "nav-link": {"font-size": "25px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
	        "nav-link-selected": {"background-color": "purple"},
    	}
	)
	if selected2 == "Alarms" :
		st.title (f"A -- T -- L -- A -- S")
		if __name__ == "__main__":
		    alarm_app()
	if selected2 == 'Daily Zodiac':
		    daily_zodiac()
	if selected2 == "Daily Weather":
		def main():
		    weather_forecast = WeatherForecast()
		    weather_forecast.run()
		if __name__ == "__main__":
				main()

#need to make sure the indentation is correct, there is a indent difference that will make 
#changes to the sidebar or horizontal menu if not indented correctly.

if selected == 'Settings':
	st.title (" Setttings")
	st.markdown(
    """
    <style>
        .textbox {
            font-family: 'Roboto', sans-serif;
            font-size: 16px;
            color: #333;
            padding: 20px;
            border: 1px solid #ccc;
            border-radius: 10px;
            background-color: #f9f9f9;
            box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.1);
        }
    </style>
     <div class='textbox'>
        <p>Welcome to the settings page!</p>
        <p>If you're looking for information on how to download, use, or debug our A-T-L-A-S Streamlit app, look no further! 
        We've got you covered in our README file, which you can find on our Github page @CSantiAlva. 
        Head on over there and get all the details you need to make the most out of our app. 
        Don't hesitate to reach out to us with any questions or feedback you might have! </p>
    </div>
    """,
    unsafe_allow_html=True
)

if selected == 'FAQ':
	st.title (" Frequently Asked Questions")
	# Define the FAQ questions and answers
	faqs = {
	    "What Were You Looking to Accomplish with ATLAS?": "I was looking for new creative ways to improve my mornings.",
	    "How Do You See ATLAS Changing in the Future?": "I see it including more midless bits, this will welcome a stimulating and healthy morning routine",
	    "What do I do if my Zodiac will not show up? ": "submit a comment on github, or feedback! All needed documentation can be found there.",
	    "How can I reccomend a change or provide code feedback? ": "GitHub!",
	    "How would you aim to further develop this App?": "I would produce an entirely new website, away from restrictive measures, and give myself more creative freedom.",
	    "What was one of the biggest challenges?": "Working with streamlit and figuring out what makes it angry and what does not",
	    "What would you advise someone who is looking at creating thir own webapp? ": "Using mediums like streamlit are useful when it comes to learning how to implement code and having it run, so if you are looking to improve your coding skills, use streamlit. If you are confident and are ready for more freedom and boundless work, I'd suggest creating a website from scratch. Yet, Streamlit is nice as it provides a template to webapp creations.",
	}

	# Add a dropdown menu to the app with the FAQ questions as options
	selected_faq = st.selectbox("Look At Previously Asked Questions from Past Users", list(faqs.keys()))

	# Display the answer to the selected FAQ question
	st.write(faqs[selected_faq])

	st.markdown(
    """
    <style>
        .textbox {
            font-family: 'Roboto', sans-serif;
            font-size: 16px;
            color: #333;
            padding: 20px;
            border: 1px solid #ccc;
            border-radius: 10px;
            background-color: #f9f9f9;
            box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.1);
        }
    </style>
     <div class='textbox'>
        <p> Welcome! I am glad you made it this far with my first Streamlit webapp.</p>
        <p> This section of the app deals with the frequently asked questions!</p>
        <p> These questions range from work done to the app, or questions dealing with things on a larger scope. 
        This being my first webapp has exposed to lots more new code and possibilities when it comes to creating new fun projects. 
        This was definitely a learning experience with such a steep learning curve, thankfully, the results are satisfactory.</p>

    </div>

    """,
    unsafe_allow_html=True
)	