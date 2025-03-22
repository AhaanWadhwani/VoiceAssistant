import speech_recognition as sr
import pyttsx3 as tts
import datetime as dt
import wikipedia
import webbrowser
import os
import random
import pyjokes

engine=pyttsx3.init()

voices=engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
#
# speak("Apple")

def wishme():
    hour=datetime.datetime.now().hour
    #6-12 - morning
    #12-16 - afternoon
    #16-6 - evening
    if hour>=6 and hour<12:
        speak("Good morning! I am your personal voice assistant.")
    elif hour>=12 and hour<16:
        speak("Good afternoon! I am your personal voice assistant.")
    else:
        speak("Good evening! I am your personal voice assistant.")

def command():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1.5
        audio=r.listen(source)
        try:
            print("Recognizing...")
            query=r.recognize_google(audio,language="en-in")
            print(f"User said: {query}")
        except Exception as e:
            speak("Sorry, I can't understand. Please try again.")
            return "none"
        return query

if __name__ == '__main__':
    wishme()
    On=True
    while On==True:
        query=command().lower()
        if "how are you" in query:
            speak("I am fine.")
        if "time" in query:
            print(f"It's {datetime.datetime.now().hour} hour and {datetime.datetime.now().minute} minutes and {datetime.datetime.now().second} seconds.")
            speak(f"It's {datetime.datetime.now().hour} hour and {datetime.datetime.now().minute} minutes and {datetime.datetime.now().second} seconds.")
        if "wikipedia" in query:
            speak("Searching Wikipedia...")
            query=query.replace("wikipedia", "")
            result=wikipedia.summary(query, sentences=2)
            print("According to Wikipedia,", result)
            speak("According to Wikipedia,")
            speak(result)
        if "name" in query:
            speak("My name is Olivia.")
        if "age" in query:
            speak("I have no age, I am a robot.")
        if "can you hear me" in query:
            speak("Yes, I can hear you.")
        if "gender" in query:
            speak("I have no gender, I am a robot.")
        websites=[["google"], ["instagram"], ["facebook"], ["youtube"], ["amazon"], ["github"], ["bing"], ["yahoo"]]
        for i in websites:
            if f"open {i[0]}" in query:
                webbrowser.open(f"https://{i[0]}.com")
        if "play music" in query:
            music="C:\\Users\\hp\\Downloads\\music_python"
            songs=os.listdir(music)
            print(songs)
            os.startfile(os.path.join(music, songs[random.randint(0,1)]))
        if "play video" in query:
            videos="C:\\Users\\hp\\Downloads\\videos_python"
            visual=os.listdir(videos)
            print(visual)
            os.startfile(os.path.join(videos, visual[random.randint(0,1)]))
        if "open power" in query:
            powerpoint="C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE"
            os.startfile(powerpoint)
        if "open word" in query:
            word="C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
            os.startfile(word)
        if "open excel" in query:
            excel="C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE"
            os.startfile(excel)
        if "joke" in query:
            joke=pyjokes.get_joke("en")
            print(joke)
            speak(joke)
            laugh="C:\\Users\\hp\\Downloads\\music_python"
        if "quit" in query:
            speak("Okay, goodbye. It was nice talking to you.")
            On=False