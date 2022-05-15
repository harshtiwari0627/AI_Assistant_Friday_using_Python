import pyttsx3
import datetime
from os import system,name
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb
import pyautogui
import psutil

from wikipedia.wikipedia import search

engine = pyttsx3.init()
voice = engine.getProperty('voices')
engine.setProperty('voice', voice[1].id)
newVoiceRate = 150
engine.setProperty('rate', newVoiceRate)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%H:%M:%S")
    speak(Time)

def date():
    newVoiceRate = 190
    engine.setProperty('rate', newVoiceRate)
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    day = datetime.datetime.now().day
    speak("the current date is")

    speak(day)
    speak(month)
    speak(year)
    
def wishme():
    hour = datetime.datetime.now().hour
    newVoiceRate = 150
    engine.setProperty('rate', newVoiceRate)
    
    if hour >= 6 and hour < 12:
        speak("Good Morning")
    elif hour >= 12 and hour < 16:
        speak("Good Afternoon ")
    elif hour >= 16 and hour <= 17:
        speak("Good Evening ")
    else:
        speak("Good night")
    speak("Friday at your service.")
    speak("Sir, what's the task for me")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening... .... ..")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recongnizing.....")
        query = r.recognize_google(audio)
        print(query)

    except Exception as e:
        print(e)
        speak("Sir Can You Say that again.....")

        return "None"
    return query

def clear():
    if name == 'nt':
        _ = system('cls')

def sendmail(to,content):
    server = smtplib.SMTP_SSL("smtp.gmail.com",465)
    server.login('harshfree0586@gmail.com','harsh87269')
    server.sendmail('harshfree0586@gmail.com',to ,content)
    server.close()

def screenshot():
    img = pyautogui.screenshot()
    img.save("D:\ss.png")

def cpu():
    cpu_usage = str(psutil.cpu_percent())
    speak("Cpu is at "+cpu_usage)

if __name__ =="__main__":
    wishme()
    while True:
        query = takeCommand().lower()

        if "time" in query:
            time()
        
        elif "date"in query:
            date()

        elif "wikipedia"in query or "search on wikipedia about"in query:
            speak("Searching.....")
            if "wikipedia"in query:
              query = query.replace("wikipedia","")
            elif "search on wikipedia about"in query:
              query = query.replace("search on wikipedia about","")
            result = wikipedia.summary(query,sentences=2)
            print(result)
            speak(result)
        
        elif"send mail" in query:
            try:
                speak("What should i send sir ?")
                print("what should i send sir ?")
                content = takeCommand()
                speak("To whom should i send mail can you tell his email address without using dot and @gmail.com")
                to = takeCommand()
                to = to.strip(" ")
                to = to.lower()
                to = to.replace(" ","")
                to = to+"@gmail.com"
                sendmail(to,content)
                speak(" Email sent successfully !!")
            except Exception as e:
                speak(e)
                print(e)
                speak("Unable to send Message")
        
        elif "go to sleep" in query:
            speak("have a nice day sir, friday going offline")
            quit()
        
        elif "search about" in query:
            speak(" Searching about your query ")
            chromepath = "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
            search =query.replace("search about",'').lower()
            wb.get(chromepath).open.__new__(search)
        
        elif "logout my system" in query:
            system("shutdown -l")
        
        elif "shutdown my system" in query:
            system("shutdown /s /t 1")

        elif "restart my system" in query:
            system("shutdown /r /t 1")

        #elif "play music" in query:
         #   songs_dir = ""
          #  songs = listdir(songs_dir)

        elif "remember that" in query:
            data = query.replace("remember that",'')
            speak("You said me to remember that"+data)
            remember = open("data.txt","w")
            remember.write(data)
            remember.close()
        
        elif "do you know anything" in query:
            remember = open("data.txt","r")
            speak("You told me to remember that"+remember.read())
            remember.close()
        
        elif "clear your memory"in query:
            remember = open("data.txt","w")
            remember.write("")
            remember.close()
        
        elif "screenshot" in query:
            screenshot()
            speak("done")
        
        elif "efficiency" in query:
            cpu()