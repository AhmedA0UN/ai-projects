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
    # ===== FIN DES NOUVELLES COMMANDES =====