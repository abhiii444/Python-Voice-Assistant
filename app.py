import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random
import time
# --------------------------- SPEAK FUNCTION ---------------------------
def speak(audio):
    """Function to convert text to speech."""
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)  
    engine.setProperty('rate', 175)  # Set speaking speed
    engine.say(audio)
    engine.runAndWait()
    engine.stop()
    time.sleep(0.2)  # Small pause to avoid overlap between speech and mic

# --------------------------- WISH FUNCTION ---------------------------
def wishMe():
    """Function to greet user based on time."""
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 16:
        speak("Good Afternoon!")   
    else:
        speak("Good Evening!")
    speak("I am Pikachu sir. Please tell me how may I help you.")       

# --------------------------- LISTEN FUNCTION ---------------------------
def takeCommand(max_retries=3):
    """Function to take voice commands from user."""
    r = sr.Recognizer()
    for attempt in range(max_retries):
        with sr.Microphone() as source:
            print("Listening...")
            r.adjust_for_ambient_noise(source, duration=0.8)  # handle background noise
            r.pause_threshold = 1
            try:
                audio = r.listen(source, timeout=10, phrase_time_limit=10)
            except sr.WaitTimeoutError:
                print("Listening timed out.")
                speak("I didn't hear anything. Please try again.")
                continue
        try:
            print("Recognizing...")    
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
            return query
        except Exception as e:
            print("Say that again please...")  
    speak("Sorry, I couldn't understand. Let's try again later.")
    return "None"

# --------------------------- DATA ---------------------------
jokes = [
    "Why don't scientists trust atoms? Because they make up everything!",
    "Why did the computer go to the doctor? Because it had a virus!",
    "Why did the math book look sad? Because it had too many problems!",
    "Why was the broom late? It swept in!"
]

fun_facts = [
    "Honey never spoils. Archaeologists have found edible honey in ancient Egyptian tombs!",
    "Bananas are berries, but strawberries aren't.",
    "A group of flamingos is called a flamboyance.",
    "Octopuses have three hearts."
]

quotes = [
    "The best way to get started is to quit talking and begin doing. - Walt Disney",
    "Don't let yesterday take up too much of today. - Will Rogers",
    "It's not whether you get knocked down, it's whether you get up. - Vince Lombardi",
    "The harder you work for something, the greater you'll feel when you achieve it."
]

songs = [ 
    "https://www.youtube.com/watch?v=sUf2PtEZris&list=RDsUf2PtEZris&start_radio=1",
    "https://www.youtube.com/watch?v=k4yXQkG2s1E&list=RDk4yXQkG2s1E&start_radio=1",
    "https://www.youtube.com/watch?v=oAVhUAaVCVQ&list=RDoAVhUAaVCVQ&start_radio=1",
    "https://www.youtube.com/watch?v=JWMIlg42pHg&list=RDJWMIlg42pHg&start_radio=1",
    "https://www.youtube.com/watch?v=oGneAab3e88&list=RDoGneAab3e88&start_radio=1",
    "https://youtu.be/jADTdg-o8i0?si=QqJaUkhCbBrCjel9",
    "https://youtu.be/VAdGW7QDJiU?si=b1Q-_nS9rEcXOiDV"
]

# --------------------------- MAIN PROGRAM ---------------------------
if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if query == "none":
            continue

        # Wikipedia search
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "").strip()
            if not query:
                speak("Please tell me what you want to search on Wikipedia.")
                continue
            try:
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)
            except Exception as e:
                speak("Sorry, I couldn't find any results on Wikipedia.")
                print(f"Wikipedia error: {e}")

        elif query.startswith(("tell me about ", "who is ", "what is ")):
            topic = query.replace("tell me about ", "").replace("who is ", "").replace("what is ", "").strip()
            if topic:
                speak(f"Searching Wikipedia for {topic}...")
                try:
                    results = wikipedia.summary(topic, sentences=2)
                    speak("According to Wikipedia")
                    print(results)
                    speak(results)
                except Exception as e:
                    speak("Sorry, I couldn't find any results on Wikipedia.")
                    print(f"Wikipedia error: {e}")
            else:
                speak("Please specify what you want to know about.")

        # Open websites
        elif 'open youtube' in query:
            speak("Opening YouTube.")
            webbrowser.open("https://youtube.com")

        elif 'open google' in query:
            speak("Opening Google.")
            webbrowser.open("https://google.com")

        elif 'open stack overflow' in query:
            speak("Opening Stack Overflow.")
            webbrowser.open("https://stackoverflow.com")

        elif 'open github' in query:
            speak("Opening GitHub.")
            webbrowser.open("https://github.com")

        elif 'open whatsapp' in query:
            speak("Opening WhatsApp Web.")
            webbrowser.open("https://web.whatsapp.com")

        elif 'open facebook' in query:
            speak("Opening Facebook.")
            webbrowser.open("https://facebook.com")

        elif 'open instagram' in query:
            speak("Opening Instagram.")
            webbrowser.open("https://instagram.com")

        # Time
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Ma'am, the time is {strTime}")

        # Open VS Code
        elif 'open code' in query:
            codePath = "C:\\Users\\Administrator\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            speak("Opening Visual Studio Code.")
            os.startfile(codePath)

        # Jokes, facts, quotes, music
        elif 'joke' in query:
            joke = random.choice(jokes)
            speak(joke)
            print(joke)

        elif 'fun fact' in query:
            fact = random.choice(fun_facts)
            speak(fact)
            print(fact)

        elif any(word in query for word in ['motivate', 'motivation', 'quote']):
            quote = random.choice(quotes)
            speak(quote)
            print(quote)

        elif any(word in query for word in ['play a song', 'play music', 'play song']):
            song_url = random.choice(songs)
            speak("Playing a Bollywood hit song on YouTube!")
            webbrowser.open(song_url)

        # Fun actions
        elif 'flip a coin' in query:
            result = random.choice(['Heads', 'Tails'])
            speak(f"It's {result}!")
            print(f"Coin flip: {result}")

        elif 'roll a dice' in query or 'roll a die' in query:
            dice = random.randint(1, 6)
            speak(f"You rolled a {dice}!")
            print(f"Dice roll: {dice}")

        # Exit
        elif 'exit' in query or 'quit' in query or 'bye' in query or 'tata' in query:
            speak("Goodbye papa ji Have a nice day.")
            break