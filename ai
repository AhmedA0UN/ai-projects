from distutils.cmd import Command
from tkinter import COMMAND
import pyttsx3
import time
import webbrowser
import speech_recognition as rs
import pyaudio

wel = pyttsx3.init()
voices = wel.getProperty('voices')
wel.setProperty('voices', voices[0].id)

def speak(audio):
    wel.say(audio)
    wel.runAndWait()
def TakeCommands ():
    Command = sr.Recognizer()
    with rs.Microphone() as mic :
        print('say commands sie ....')
        Command.phrase_threshold =1
        audio = Command.listen(mic)
        try:
            print('rocording...') 
            query = Command.recognize_google(audio , language='en')
            print(f'you said : {query}')
        except Exception as Error:
            return None
        return query.lower()
    

speak('hello sir ahmed, say your commands please')

while True:
    query = TakeCommands ()
    if 'hello' in query:
        speak('hello bohmid')
    if 'haw are you' in query:
        speak('am fine sir , and you')
    if 'open google' in query:
              speak('ok sir')
              time.sleep(3)
              webbrowser.open('https://www.google.com')
