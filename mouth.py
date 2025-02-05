import speech_recognition as sr
import pyttsx3
import os
import threading
import time
import pyttsx3
import random
from colorama import Fore,Style,init
from mtranslate import translate

WAKE_WORD = "friday"
init(autoreset=True) #function which auto reset style where we call it

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('rate', 150)
engine.setProperty('volume', 1.0)
engine.setProperty('voice', voices[1].id)

def translateHindi(txt):
    englishLnag = translate(txt,to_language="en")
    return englishLnag

def speak(text):
    print(f"Friday: {text}")
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    recognizer.dynamic_energy_threshold = False #do not fluctuate the sound listining
    recognizer.energy_threshold = 3500 #listen sound only louder then 3500
    recognizer.dynamic_energy_adjustment_damping = 0.03 #less react on sudden arise
    recognizer.dynamic_energy_ratio = 1.9 #This line adjusts how much louder speech needs to be compared to background noise before it's recognized as speech.
    recognizer.operation_timeout = None
    recognizer.pause_threshold = 0.2
    recognizer.non_speaking_duration = 0.1

    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print(Fore.GREEN+ "Listening...", end="", flush=True)
        try:
            audio = recognizer.listen(source,timeout=None)
            time.sleep(0.2)
            print("\r"+Fore.LIGHTYELLOW_EX + "Got it! Recognizing...", end="", flush=True)

            query  = recognizer.recognize_google(audio)
            translQuery = translateHindi(query)
            print("\r",Fore.BLUE+"Mr Aadi: " + translQuery)
            return translQuery.lower()
        except sr.UnknownValueError:
            translQuery = ""
            speak(random.choice(["sorry,I didn't catch that.", "Can you repeat?","I couldn't understand you."]))
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
            return ""
