import speech_recognition as sr
import webbrowser
# its a built in module no need to install
import pyttsx3
import musicLibrary
from gpt4all import GPT4All
# gpt model
import time
import os  
import sys

def voice_assistant():

    def speak(text):
        engine = pyttsx3.init()
        engine.setProperty('rate', 170)
        engine.say(text)
        engine.runAndWait()
    # This function is use to convert text to speech

    def resource_path(relative_path):
        try:
            return os.path.join(sys._MEIPASS, relative_path)
        except:
            return os.path.abspath(relative_path)

    model_path = resource_path("mistral-7b-instruct-v0.1.Q4_0.gguf")
    model = GPT4All(model_path, allow_download=False)
    # GPT4All model, download dependencies automatically

    def gpt_response(prompt):
        response = model.generate(prompt, max_tokens=128)
        return response

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
            link = musicLibrary.songs[song]
            if link:
                webbrowser.open(link)
            else:
                speak("Song Not Found")

        elif "stop" in c.lower() or "exit" in c.lower():
            speak("Goodbye Femil!")
            return
        
        elif len(c)==0:
            speak("Please Speak Again")
        
        else:
            speak("Preparing your answer please wait")
            model_response = gpt_response(c)
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
    
