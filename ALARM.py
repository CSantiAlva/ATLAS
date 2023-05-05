import time
import platform
from playsound import playsound
import datetime

def alarm(sound_file):
    playsound(file_path_alarm)
    ##in order to use playsound you will need to [pip install 'PyObjC'] 
    #this is what playsound needed to play playsound,
    #it just needs a more updated version  [include this part in the read-me file]
while True:
    alarm_time = input("Enter the alarm time in hh:mm AM/PM format: ")
    try:
        time_struct = time.strptime(alarm_time, '%I:%M %p')
        alarm_hour = time_struct.tm_hour
        alarm_minute = time_struct.tm_min
        break
    except ValueError:
        print("Enter a valid time in hh:mm AM/PM format.")

sound_file = "alarm_sound.mp3" #Replace with the path to your mp3 file

while True:
    current_time = datetime.datetime.now().time().strftime('%I:%M %p')
    if current_time == time.strftime('%I:%M %p', time_struct):
        print("Time's up!")
        alarm(sound_file)
        break
    time.sleep(1)

