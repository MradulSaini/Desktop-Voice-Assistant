# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 17:08:45 2019

@author: Mradul
"""

import pyttsx3 
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser as wb
import os,random
import smtplib

chrome_path='C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takeCommand():
    r = sr.Recognizer()
    r.pause_threshold=1
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source,duration=2)
       
        print("SPEAK")
        speak("Listening...")
        audio=r.listen(source)
    try:
        speak("Recognizing... Please Wait....")    
        query=r.recognize_google(audio,language='en-in')
        print(f"Task :{query}\n")
        
    except Exception as e:
        print(e)
        speak("Sorry Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('your mail id', 'your-password')
    server.sendmail('your mail id', to, content)
    server.close()
    
if __name__ == "__main__":
    speak("Hello  How may i help you")
    while True:        
        query=takeCommand().lower()
        
        if 'stop' in query or 'close' in query or 'bye' in query:
            speak("GOOD BYE")
            break
        
        elif 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query=query.replace("wikipedia","")
            wb.get(chrome_path).open('https://en.wikipedia.org/wiki/'+query)
            speak(wikipedia.summary(query, sentences=3))
            break

        elif 'open youtube' in query:
            wb.get(chrome_path).open("youtube.com")
            break

        elif 'open google' in query:
            query=query.replace('google','')
            query=query.replace('open','')
            wb.get(chrome_path).open('google.com')
            break

        elif 'play music' in query or 'music'  in query:
            mdir='D:/Movies/youtube'
            songs=os.listdir(mdir)
            os.startfile(os.path.join(mdir,songs[random.randint(0,5)]))
            break

        elif "what's the time" in query or 'time' in query:
            strTime=datetime.datetime.now().strftime("%I%M%p")    
            speak(f"Time is {strTime}")

        elif 'email'  in query or 'mail' in query or 'send mail' in query:
            try:
                speak("What's the message")
                content=takeCommand()
                speak("To whom do you you want to mail")
                to=takeCommand()    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                speak("Unable to send message")
                print(e)
       
        elif 'open notedpad' in query or 'notepad' in query:
            wb.open('Notepad.exe')
            break
        
        elif 'open paint' in query:
            wb.open('mspaint.exe')
            break
        
        elif 'search' in query:
            query=query.replace('search','')
            speak("Searching the web")
            wb.get(chrome_path).open('https://www.google.com/search?q='+query)
            break
        
        elif 'open camera' in query or 'webcam' in query or 'camera' in query or 'cam' in query:            
            wb.open('microsoft.windows.camera:')
            break
        
        elif 'calculator' in query:
           import subprocess
           subprocess.Popen('C:\\Windows\\System32\\calc.exe')
           break
        elif 'restart' in query:
            speak("GOOD BYE")            
            speak("Restarting your PC.")
            os.system("shutdown /r /t 1");
            break
        elif 'shut down' in query:
            speak("GOOD BYE")            
            speak("Shudting Down your PC.")
            os.system("shutdown /s /t 1");
            break
        elif 'on screen keyboard' in query or 'keyboard' in query:
            os.system("osk")
            break
        elif 'whatsapp' in query or 'whatsapp web' in query:
            wb.get(chrome_path).open('https://web.whatsapp.com/')
            break
        elif 'today date' in query or 'date' in query:
            speak("Today's Date is ")
            d=datetime.date.today()
            speak(str(d))
            
            
            
            
        
        
        
            
       
                   
