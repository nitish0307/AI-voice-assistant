import imp
from itertools import takewhile
from ssl import _PasswordType
import webbrowser
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import os
import smtplib




engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[0].id)



    


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good Morning!")

    elif hour>=12 and hour<18:
        speak("good Afternoon!") 

    else:
        speak("Good Evening!")

    speak("I m Jarvis. Please tell me how may I help you")    

def takeCommand():
    # it takes microphone input and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("say that again please.....")
        return "None"
    return query
# def sendEmail(to, content):

if __name__ == "__main__":
    wishMe()
    while True:
    #  if 1:
      query = takeCommand().lower()

      if 'wikipedia' in query:
        speak('searching Wikipedia....')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia")
        print(results)
        speak(results)

      elif 'open youtube' in query:
            webbrowser.open("youtube.com")

      elif 'open google' in query:
            webbrowser.open("google.com")

      elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   

      elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
      
      elif 'open vs code' in query:
            codePath = "C:\\Users\HP\\AppData\Local\\Programs\\Microsoft VS Code\,\Code.exe"
            os.startfile(codePath)
    #   elif 'email to Nitish' in query:
    #         try:
    #             speak("What should I say?")
    #             content = takeCommand()
    #             to = "NitishyourEmail@gmail.com"    
    #             sendEmail(to, content)
    #             speak("Email has been sent!")
    #         except Exception as e:
    #             print(e)
    #             speak("Sorry sir. I am not able to send this email")
      elif 'open' in query:
            a = query.split()
            b = a[1]

            webbrowser.open(b + '.com')
      
      elif 'introduce yourself' in query:
        speak("my name is jarvis, i am a voice assistant and i can help you in some of your tasks. would you like to ask anything")

      elif 'i love you' in query:
        speak("i love you too. but as a friend, we can just be friends but nothing more than that")

        