from main import voice_assistant
import keyboard
import pyttsx3
from datetime import datetime
import random

def speak(text):    
    engine = pyttsx3.init()
    engine.setProperty('rate', 170)
    engine.say(text)
    engine.runAndWait()

def greet(hour):

    names = ['Femil', 'Operator', 'Chief', 'Captian']
    name = random.choice(names)

    if hour>=12 and hour<=16:
        speak(f"Good Afternoon {name} Please Press 's' to Activate Jarvis")
    elif hour>16 and hour<24:
        speak(f"Good Evening {name} Please Press 's' to Activate Jarvis")
    else:
        speak(f"Good Morning {name} Please Press 's' to Activate Jarvis")

now = datetime.now()

curr_hour = int(now.strftime("%H"))

greet(curr_hour)

keyboard.add_hotkey('s', voice_assistant)

key = keyboard.get_hotkey_name()

if key=='esc':
    speak("GoodBye")

keyboard.wait('esc')
