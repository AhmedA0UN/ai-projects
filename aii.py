import pyttsx3
import time
import webbrowser
import speech_recognition as sr  # Fixed the import name (was 'rs')
import pyaudio

# Initialize the text-to-speech engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # Fixed property name (was 'voices')

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def take_commands():  # Changed to lowercase for Python naming convention
    recognizer = sr.Recognizer()
    with sr.Microphone() as mic:
        print('Listening for commands...')
        recognizer.phrase_threshold = 1
        recognizer.pause_threshold = 1  # Added for better recognition
        audio = recognizer.listen(mic)
        
        try:
            print('Recognizing...') 
            query = recognizer.recognize_google(audio, language='en')
            print(f'You said: {query}')
        except Exception as error:
            print(f"Error: {error}")
            return None
        return query.lower()

speak('Hello sir Ahmed, say your commands please')

while True:
    query = take_commands()
    
    if query is None:
        continue
        
    if 'hello' in query:
        speak('Hello Mohamed')
    elif 'how are you' in query:  # Fixed typo ('haw' -> 'how')
        speak('I am fine sir, and you?')
    elif 'open google' in query:
        speak('Opening Google sir')
        time.sleep(3)
        webbrowser.open('https://www.google.com')
    elif 'exit' in query or 'quit' in query:  # Added exit condition
        speak('Goodbye sir')
        break