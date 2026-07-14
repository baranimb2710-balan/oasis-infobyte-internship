import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import smtplib
import threading
import requests
import json

# Optional: NLP with transformers
from transformers import pipeline

# Initialize recognizer, TTS, and NLP
recognizer = sr.Recognizer()
engine = pyttsx3.init()
nlp = pipeline("text-classification", model="distilbert-base-uncased-finetuned-sst-2-english")

# --- Utility Functions ---

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that. Please repeat.")
            return None

# --- Feature Functions ---

def tell_time():
    now = datetime.datetime.now().strftime("%H:%M")
    speak(f"The current time is {now}")

def tell_date():
    today = datetime.date.today().strftime("%B %d, %Y")
    speak(f"Today's date is {today}")

def search_web(query):
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)
    speak(f"Searching for {query}")

def send_email(recipient, subject, body):
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login("your_dummy_email@gmail.com", "your_password")
        message = f"Subject: {subject}\n\n{body}"
        server.sendmail("your_dummy_email@gmail.com", recipient, message)
        server.quit()
        speak("Email sent successfully.")
    except Exception as e:
        speak("Sorry, I couldn't send the email.")
        print(e)

def set_reminder(seconds, message):
    def reminder():
        speak(f"Reminder: {message}")
    timer = threading.Timer(seconds, reminder)
    timer.start()
    speak(f"Reminder set for {seconds} seconds from now.")

def get_weather(city):
    api_key = "YOUR_OPENWEATHERMAP_API_KEY"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url).json()
    if response.get("main"):
        temp = response["main"]["temp"]
        desc = response["weather"][0]["description"]
        speak(f"The temperature in {city} is {temp}°C with {desc}.")
    else:
        speak("Sorry, I couldn't fetch the weather.")

def answer_question(question):
    # Placeholder for QA API integration
    speak("This is where I'd answer general knowledge questions.")
    # Example: integrate WolframAlpha or HuggingFace QA models

def load_custom_commands():
    try:
        with open("commands.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

# --- Main Loop ---

def main():
    custom_commands = load_custom_commands()
    while True:
        command = listen()
        if command:
            if "hello" in command:
                speak("Hello! How can I help you today?")
            elif "time" in command:
                tell_time()
            elif "date" in command:
                tell_date()
            elif "search" in command:
                topic = command.replace("search", "").strip()
                search_web(topic)
            elif "email" in command:
                send_email("recipient@example.com", "Test Subject", "This is a test email.")
            elif "remind me" in command:
                set_reminder(10, "Check the oven")  # Example: 10 seconds
            elif "weather" in command:
                get_weather("Madurai")
            elif "question" in command:
                answer_question(command)
            elif command in custom_commands:
                speak(custom_commands[command])
            elif "exit" in command:
                speak("Goodbye!")
                break

if __name__ == "__main__":
    main()
