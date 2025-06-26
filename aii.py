import pyttsx3
import time
import webbrowser
import speech_recognition as sr
import pyaudio
import datetime  # Nouveau module pour l'heure

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
        
    # Anciennes commandes (non modifiées)
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
    
    # ===== NOUVELLES COMMANDES (AJOUTÉES SANS TOUCHER L'ANCIEN CODE) =====
    elif 'time' in query:
        current_time = datetime.datetime.now().strftime("%H:%M")
        speak(f"The current time is {current_time}")
    elif 'open youtube' in query:
        speak("Opening YouTube")
        webbrowser.open("https://youtube.com")
    elif 'thank you' in query:
        speak("You're welcome, sir!")
    elif 'what is your name' in query:
        speak("I am your voice assistant, sir!")
    elif 'search' in query:
        search_query = query.replace("search", "").strip()
        if search_query:
            speak(f"Searching for {search_query}")
            webbrowser.open(f"https://google.com/search?q={search_query}")
        else:
            speak("What should I search for?")
    elif 'play music' in query:
        speak("Playing music")
        webbrowser.open("https://music.youtube.com")
    elif 'tell a joke' in query:
        speak("Why did the computer go to the doctor? Because it had a virus!")
    elif 'set a reminder' in query:
        speak("What should I remind you about?")
        reminder = take_commands()
        if reminder:
            speak(f"Reminder set for: {reminder}")
        else:
            speak("I didn't catch that, please repeat.")
    elif 'weather' in query:
        speak("Please tell me the city for the weather update.")
        city = take_commands()
        if city:
            speak(f"Fetching weather information for {city}")
            webbrowser.open(f"https://weather.com/en-IN/weather/today/l/{city}")
        else:
            speak("I didn't catch that, please repeat the city name.")
    elif 'news' in query:
        speak("Opening the latest news")
        webbrowser.open("https://news.google.com")
    elif 'calculator' in query:
        speak("Opening the calculator")
        webbrowser.open("https://www.google.com/search?q=calculator")
    elif 'translate' in query:
        speak("Please tell me the text you want to translate.")
        text_to_translate = take_commands()
        if text_to_translate:
            speak(f"Translating {text_to_translate}")
            webbrowser.open(f"https://translate.google.com/?sl=auto&tl=en&text={text_to_translate}")
        else:
            speak("I didn't catch that, please repeat the text to translate.")
    elif 'open notepad' in query:
        speak("Opening Notepad")
        webbrowser.open("https://notepad-plus-plus.org/downloads/")
    elif 'open calculator' in query:
        speak("Opening Calculator")
        webbrowser.open("https://www.google.com/search?q=calculator")
    elif 'open calendar' in query:
        speak("Opening Calendar")
        webbrowser.open("https://calendar.google.com")
    elif 'open maps' in query:
        speak("Opening Maps")
        webbrowser.open("https://maps.google.com")
    elif 'open gmail' in query:
        speak("Opening Gmail")
        webbrowser.open("https://mail.google.com")
    elif 'open facebook' in query:
        speak("Opening Facebook")
        webbrowser.open("https://www.facebook.com")
    # open vs code editor local in my computer without using web browser
    elif 'open vs code ' in query:
        speak("Opening Visual Studio Code Editor")
        try:
            import os
            os.system("code")  # Assurez-vous que 'code' est dans votre PATH
        except Exception as e:
            speak("I couldn't open Visual Studio Code. Please check if it's installed.")
    elif 'open terminal' in query:
        speak("Opening Terminal")
        try:
            import os
            os.system("gnome-terminal")  # Pour Linux, utilisez 'cmd' pour Windows
        except Exception as e:
            speak("I couldn't open the terminal. Please check if it's installed.")
    elif 'open file explorer' in query:
        speak("Opening File Explorer")
        try:
            import os
            os.system("explorer")  # Pour Windows, utilisez 'nautilus' pour Linux
        except Exception as e:
            speak("I couldn't open the file explorer. Please check if it's installed.")
    elif 'open settings' in query:
        speak("Opening Settings")
        try:
            import os
            os.system("start ms-settings:")  # Pour Windows, utilisez 'gnome-control-center' pour Linux
        except Exception as e:
            speak("I couldn't open the settings. Please check if it's installed.")
    elif 'open spotify' in query:
        speak("Opening Spotify")
        webbrowser.open("https://open.spotify.com")
    # open block note
    elif 'open bloc note' in query:
        speak("Opening Block Note")
        try:
            import os
            os.system("bloc-notes")  # Pour Windows, utilisez 'gedit' pour Linux
        except Exception as e:
            speak("I couldn't open the Block Note. Please check if it's installed.")
    elif 'open discord' in query:
        speak("Opening Discord")
        webbrowser.open("https://discord.com")
    elif 'open whatsapp' in query:
        speak("Opening WhatsApp Web")
        webbrowser.open("https://web.whatsapp.com")
    elif 'open twitter' in query:
        speak("Opening Twitter")
        webbrowser.open("https://twitter.com")
    elif 'open instagram' in query:
        speak("Opening Instagram")
        webbrowser.open("https://instagram.com")
    # ===== FIN DES NOUVELLES COMMANDES =====