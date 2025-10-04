from main import voice_assistant
import keyboard
import pyttsx3
from datetime import datetime
import random
import threading

def speak(text):    
    engine = pyttsx3.init()
    engine.setProperty('rate', 170)
    engine.say(text)
    engine.runAndWait()

def greet(hour):
    names = ['Femil', 'Operator', 'Chief', 'Captain']
    name = random.choice(names)

    if hour >= 12 and hour <= 16:
        speak(f"Good Afternoon {name}, please press 's' to activate Jarvis.")
    elif hour > 16 and hour < 24:
        speak(f"Good Evening {name}, please press 's' to activate Jarvis.")
    else:
        speak(f"Good Morning {name}, please press 's' to activate Jarvis.")

def start_jarvis():
    threading.Thread(target=voice_assistant).start()

def exit_program():
    speak("Goodbye")
    exit(0)

# Greet on start
curr_hour = int(datetime.now().strftime("%H"))
greet(curr_hour)

# Assign hotkeys
keyboard.add_hotkey('s', start_jarvis)
keyboard.add_hotkey('esc', exit_program)

# Wait forever for any hotkey
keyboard.wait()
