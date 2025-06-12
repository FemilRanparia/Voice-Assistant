from main import voice_assistant
import keyboard
import pyttsx3
from datetime import datetime
# import threading


def speak(text):    
    engine = pyttsx3.init()
    engine.setProperty('rate', 170)
    engine.say(text)
    engine.runAndWait()

def greet(hour):
    if hour>12 and hour<16:
        speak("Good Afternoon Femil Please Press 's' to Activate Jarvis")
    elif hour>16 and hour<24:
        speak("Good Evening Femil Please Press 's' to Activate Jarvis")
    else:
        speak("Good Morning Femil Please Press 's' to Activate Jarvis")

now = datetime.now()

curr_hour = int(now.strftime("%H"))

greet(curr_hour)


# def trigger_jarvis():
#     t = threading.Thread(target=voice_assistant)
#     t.daemon = False
#     t.start()

keyboard.add_hotkey('s', voice_assistant)

keyboard.wait('esc')