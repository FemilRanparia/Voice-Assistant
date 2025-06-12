import speech_recognition as sr
# Now we dont need to write whole speechrecog... we replace it to sr
import webbrowser
# its a built in module no need to install
import pyttsx3

import musicLibrary

# To implement key based start up


def voice_assistant():
    # recognizer = sr.Recognizer()

    def speak(text):
        engine = pyttsx3.init()
        engine.setProperty('rate', 170)
        engine.say(text)
        engine.runAndWait()
    # This function is use to convert text to speech

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
            speak("Goodbye Pardon!")
            return
        else:
            speak("Please Speak Again")

    # speak("Initializing Jarvis...")
    r = sr.Recognizer()
    # speak("Jarvis Activated")
    # speak("Jarvis Initialized")
    # while True:
    # Listen for the wake word jarvis
    # obtain audio from microphone
    print("recognizing...")
    try:
        # with sr.Microphone() as source:
            # r.adjust_for_ambient_noise(source, duration=1)
            # print("Listening...")
            # audio = r.listen(source, timeout=5, phrase_time_limit=4)
            # above code is for listining from microphone
            # timeout is time it will listen. after 2 secs it will do timeout
            # phasetimeout is time after how much sec u take to continue
        # word = r.recognize_google(audio)
        # print(word)
        # if "jarvis" in word.lower():
            # speak("I am listening")
            # Listen for the further command
        with sr.Microphone() as source:
            speak("Jarvis Activated")
            audio = r.listen(source, timeout=5, phrase_time_limit=5)
            command = r.recognize_google(audio)
            processCommand(command)

    except Exception as e:
        print("Error ; {0}".format(e))

if __name__ == "__main__":
    voice_assistant()   