import google.generativeai as genai
# from config import GEMINI_API_KEY

import speech_recognition as sr
import webbrowser
# its a built in module no need to install
import pyttsx3
import musicLibrary
# from gpt4all import GPT4All
# gpt model
import time
import os
import sys

GEMINI_API_KEY = "AIzaSyDPMKWkVsja7XrxUhFkLRo596GCaHj_0Xs"
genai.configure(api_key=GEMINI_API_KEY)


# mostly flash models are working properly pro models are not free

# Best working free model
# gemini-2.5-flash-lite-preview-09-2025

# slow and not working properly and not at all accurate
# gemini-2.0-flash-lite-preview-02-05

model = genai.GenerativeModel('gemini-2.5-flash-lite-preview-09-2025')
def voice_assistant():

    def speak(text):
        engine = pyttsx3.init()
        engine.setProperty('rate', 170)
        engine.say(text)
        engine.runAndWait()

    def gemini_response(prompt):
        try:
            response = model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"Error: {str(e)}"

    def processCommand(c):
        if "open google" in c.lower():
            webbrowser.open("https://google.com")
        elif "open facebook" in c.lower():
            webbrowser.open("https://facebook.com")
        elif "open linkedin" in c.lower():
            webbrowser.open("https://linkedin.com")
        elif "open youtube" in c.lower():
            webbrowser.open("https://youtube.com")
        elif c.lower().startswith("play"):
            song = c.lower().split(" ")[1]
            link = musicLibrary.songs.get(song)
            if link:
                webbrowser.open(link)
            else:
                speak("Song Not Found")

        elif "stop" in c.lower() or "exit" in c.lower():
            speak("Goodbye Femil!")
            return

        elif len(c) == 0:
            speak("Please Speak Again")

        else:
            speak("Preparing your answer please wait")
            model_response = gemini_response(c)
            speak("And Here it is")
            speak(model_response)
            time.sleep(1)
            speak("That was it")

        time.sleep(1)
        speak("To Continue Please press 's' again")

    r = sr.Recognizer()

    print("recognizing...")
    try:
        with sr.Microphone() as source:
            speak("Jarvis Activated")
            audio = r.listen(source, timeout=5, phrase_time_limit=5)
            command = r.recognize_google(audio)
            processCommand(command)

    except Exception as e:
        speak("Please press 's' and speak again")
        print(e)


if __name__ == "__main__":
    voice_assistant()