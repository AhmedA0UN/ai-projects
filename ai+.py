import pyttsx3
import time
import webbrowser
import speech_recognition as sr
import datetime
import os
import subprocess

# Initialisation du moteur TTS
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def take_commands():
    recognizer = sr.Recognizer()
    with sr.Microphone() as mic:
        print('Listening...')
        recognizer.pause_threshold = 1
        audio = recognizer.listen(mic)
        
        try:
            print('Recognizing...')
            query = recognizer.recognize_google(audio, language='en')
            print(f"You said: {query}")
        except Exception as e:
            print("Error:", e)
            return None
        return query.lower()

speak("Hello sir Ahmed, how can I help you?")

while True:
    query = take_commands()
    
    if not query:
        continue
        
    # ===== ANCIENNES COMMANDES (GARDÉES INTACTES) =====
    if 'hello' in query:
        speak('Hello Mohamed')
    elif 'how are you' in query:
        speak('I am fine sir, and you?')
    elif 'open google' in query:
        speak('Opening Google')
        webbrowser.open("https://google.com")
    elif 'exit' in query or 'quit' in query:
        speak("Goodbye sir!")
        break
    
    # ===== NOUVELLES COMMANDES (AJOUTÉES SANS MODIFIER L'ANCIEN CODE) =====
    
    # 📅 Date & Time
    elif 'time' in query:
        current_time = datetime.datetime.now().strftime("%H:%M")
        speak(f"The current time is {current_time}")
    elif 'date' in query:
        current_date = datetime.datetime.now().strftime("%d/%m/%Y")
        speak(f"Today's date is {current_date}")
    
    # 🌐 Navigation Web
    elif 'open youtube' in query:
        speak("Opening YouTube")
        webbrowser.open("https://youtube.com")
    elif 'open facebook' in query:
        speak("Opening Facebook")
        webbrowser.open("https://facebook.com")
    elif 'search' in query:
        search_query = query.replace("search", "").strip()
        if search_query:
            speak(f"Searching for {search_query}")
            webbrowser.open(f"https://google.com/search?q={search_query}")
    
    # 🎵 Musique & Divertissement
    elif 'play music' in query:
        speak("Playing music")
        webbrowser.open("https://music.youtube.com")
    elif 'open spotify' in query:
        speak("Opening Spotify")
        webbrowser.open("https://open.spotify.com")
    
    # 📝 Productivité
    elif 'open vs code' in query:
        speak("Opening Visual Studio Code")
        try:
            subprocess.Popen(["code"])  # Windows / Linux (si dans PATH)
        except:
            speak("Failed to open VS Code. Is it installed?")
    
    elif 'open terminal' in query:
        speak("Opening Terminal")
        try:
            if os.name == 'nt':  # Windows
                os.system("start cmd")
            else:  # Linux / Mac
                os.system("gnome-terminal")
        except:
            speak("Could not open Terminal.")
    
    elif 'open file explorer' in query:
        speak("Opening File Explorer")
        if os.name == 'nt':
            os.system("explorer")
        else:
            os.system("nautilus")
    
    # 📰 Actualités & Météo
    elif 'news' in query:
        speak("Opening news")
        webbrowser.open("https://news.google.com")
    elif 'weather' in query:
        speak("Which city?")
        city = take_commands()
        if city:
            webbrowser.open(f"https://weather.com/en-IN/weather/today/l/{city}")
    
    # 🛠️ Autres Utilitaires
    elif 'calculator' in query:
        speak("Opening calculator")
        webbrowser.open("https://www.google.com/search?q=calculator")
    elif 'translate' in query:
        speak("What should I translate?")
        text = take_commands()
        if text:
            webbrowser.open(f"https://translate.google.com/?text={text}")
    
    # ❌ Fermeture d'applications
    elif 'close chrome' in query:
        speak("Closing Chrome")
        if os.name == 'nt':
            os.system("taskkill /f / Microsoft Edge.exe")
        else:
            os.system("pkill Microsoft Edge")
    
    # 🤖 Commandes amusantes
    elif 'tell a joke' in query:
        speak("Why don't scientists trust atoms? Because they make up everything! hahahaha!")
    elif 'who made you' in query:
        speak("I was created by a brilliant developer using Python!")
    
    # ===== FIN DES NOUVELLES COMMANDES =====