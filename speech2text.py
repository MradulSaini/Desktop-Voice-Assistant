# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 08:24:40 2019

@author: Mradul
"""
import speech_recognition as sr
File_object=open('TEXTAUDIO.txt','a')
r=sr.Recognizer()
r.pause_threshold=1

with sr.Microphone() as source :
    r.adjust_for_ambient_noise(source,duration=2)
    print('say something')
    audio=r.listen(source)
    text=r.recognize_google(audio)
    File_object.write(text)
    File_object.close()

try:
    print('You said :' + text)
except:
    print('Too MUCH NOISE ')

