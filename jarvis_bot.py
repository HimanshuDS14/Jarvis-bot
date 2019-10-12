import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib



engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")

#print(voices[1].id)
engine.setProperty("voice" , voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if (hour>=0 and hour<12):
        speak("good morning sir")
    elif(hour>=12 and hour<18):
        speak("good afternoon sir")
    else:
        speak("good evening sir")


    speak("I am jarvis sir. please tell me how may i help you.")

def takeCommand():
    #it takes input from the user and return string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listining...")
        r.pause_threshold = 2
        r.energy_threshold = 800
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio , language="en-in")
        print(f"user said {query}\n")

    except Exception as e:
        #print(e)
        print("Say that again please")
        return "None"

    return query


if __name__ == '__main__':
    wishme()
    #speak("welcome to chatbot")
    while True:
        query = takeCommand().lower()

        #logic for executing task

        if "wikipedia" in query:
            speak("search content")
            content = takeCommand()
            speak(f"searching {content} on wikipedia")

            result = wikipedia.summary(content , sentences=2)
            print(result)
            speak(f"According to wikipedia {result}")


        elif "open youtube" in query:
            speak("opening youtube")
            webbrowser.open("youtube.com")

        elif "open google" in query:
            webbrowser.open("google.com")

        elif "open stackoverflow" in query:
            webbrowser.open("stackoverflow.com")

        elif "good bye" in query:
            speak("take care and good bye sir")
            break

        elif "music time" in query:
            music_dir = r"E:\song"
            songs  = os.listdir(music_dir)
            speak("Enjoy your music")
            os.startfile(os.path.join(music_dir , songs[0]))

        elif "the time" in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir the time is {strtime}")

        elif "open chrome" in query:
            path = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
            speak("opening chrome")
            os.startfile(path)

        elif "open code" in query:
            path = r"C:\Program Files\JetBrains\PyCharm Community Edition 2018.3.5\bin\pycharm64.exe"
            speak("opening pycharm")
            os.startfile(path)

        elif "open paint" in query:
            path = r"%windir%\system32\mspaint.exe"
            speak("opening paint")
            os.startfile(path)

        elif "search in google" in query:
            speak("search content")
            content = takeCommand()
            speak(f"searching {content}")
            webbrowser.open("https://www.google.com/search?q=" + content)

        elif "search on youtube" in query:
            speak("search content")
            content = takeCommand()
            speak(f"searching {content}")
            webbrowser.open("https://www.youtube.com/results?search_query="+content)

        elif "atmosphere broadcast" in query:
            webbrowser.open("https://www.google.com/search?q=wheather+broadcast")

        elif "play indian music" in query:
            speak("music name")
            content = takeCommand()
            speak(f"searching{content}")
            speak("enjoy your music")
            webbrowser.open("https://wynk.in/music/detailsearch/"+content+"?q="+content)


        elif "tell me something about yourself" in query:
            speak("I am JARVIS 1.0 creator by Himanshu verma.")



