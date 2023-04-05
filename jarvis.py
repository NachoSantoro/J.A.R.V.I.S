from selenium import webdriver
import time
from speech_recognition import Microphone, Recognizer, AudioFile, UnknownValueError, RequestError
from gtts import gTTS
from playsound import playsound 
import random
import datetime
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr
import os
from os import startfile
from pyautogui import click
#from keyboard import press
#from keyboard import press_and_release
#from keyboard import write

#VARIABLES GLOBALES
validaAuth =  False
browser = webdriver
engine = pyttsx3.init()

def speak(audio):
    print("     ")
    print(f": {audio}")
    print("     ")
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[7].id)
    engine.setProperty('rate', 170)
    engine.say(audio)
    engine.runAndWait()

def alarm(query):
    timehere = open("Alarmtext.txt","a")
    timehere.write(query)
    timehere.close()
    os.startfile("alarm.py")

def escuchar():
    
    print("Escuchando...")
    recognizer = Recognizer()
    microfono = Microphone()
    with microfono:
        recognizer.adjust_for_ambient_noise(microfono)
    recognizer.listen_in_background(microfono, callback)
    
def callback(recognizer, source):
    print("Recognizing...")
    
    try:
        hour = datetime.datetime.now().hour
        reconocer = recognizer.recognize_google(source, language='us-US')
        texto = str(reconocer).lower()
        print("I've heard:", texto)
        
        
        if(texto.__contains__("eva")):
            print("You've called Eva")
            texto = texto.replace("eva", "")    
            accion(texto)
                
        if(texto.__contains__("good morning") or texto.__contains__("good afternoon") or texto.__contains__("good evening") or texto.__contains__("hello")):
            
            if hour >= 5 and  hour < 13:
                playsound('./DataBase/Voices/Amy/goodMorningAmy.mp3')
            elif hour >= 13 and hour < 20:
                playsound('./DataBase/Voices/Amy/goodAfternoonAmy.mp3')
            else:
                playsound('./DataBase/Voices/Amy/goodEveningAmy.mp3')
            
            time.sleep(1)
            playsound('./DataBase/Voices/Amy/assistAmy.mp3')
            return
        
        if (texto.__contains__("thank you") or texto.__contains__("thanks")):
            playsound('./DataBase/Voices/Amy/myPleasureAmy.mp3')
        
            
        return
    except RequestError as exc:
        print("Error al escuchar: ", exc)
    except UnknownValueError:
        playsound('./DataBase/Voices/Amy/dontUnderstandAmy.mp3')

def accion(texto: str):
    
    if (texto.__contains__("you up")):
            playsound('./DataBase/Voices/Amy/alwaysAmy.mp3')
    
    if(texto.__contains__("open whatsapp")):
        print("Opening Whatsapp")
        playsound('./DataBase/Voices/Amy/openingWhatsappAmy.mp3')
        time.sleep(1)
        startfile('C:\\Users\\IgnacioSantoro\\AppData\\Local\\WhatsApp\\Whatsapp.exe')
        
    if(texto.__contains__("do you know any joke") or texto.__contains__("tell me a joke")):
        chiste()
        return
    
    if (texto.__contains__("google") or texto.__contains__("Google")):
            from SearchNow import searchGoogle
            searchGoogle(texto)
            
    elif (texto.__contains__("youtube") or texto.__contains__("Youtube")):
        from SearchNow import searchYoutube
        searchYoutube(texto)
            
    elif (texto.__contains__("wikipedia") or texto.__contains__("Wikipedia")):
        from SearchNow import searchWikipedia
        searchWikipedia(texto)
        
    elif (texto.__contains__("the time") or texto.__contains__("what time")):
        strTime = datetime.datetime.now().strftime("%H:%M")    
        speak(f"Sir, the time is {strTime}")
        
    elif (texto.__contains__("go to sleep")):
        speak("Going to sleep, sir")
        exit()
            
    elif (texto.__contains__("open")):
        from Dictapp import openappweb
        openappweb(texto)
            
    elif (texto.__contains__("close")):
        from Dictapp import closeappweb
        closeappweb(texto)
            
    elif (texto.__contains__("set an alarm")):
        print("input time example:- 10 and 10 and 10")
        speak("Set the time")
        a = input("Please tell the time :- ")
        alarm(a)
        speak("Done,sir")
        
    elif (texto.__contains__("play a game")):
        from game import game_play
        game_play()
            
    if (texto.__contains__("close browser")):
        playsound('./DataBase/Voices/Amy/closingAmy.mp3')
        browser.close() # type: ignore
        return

def hablar(texto: str):
    print("Hablando...")
    audio = gTTS(text=texto, lang='en-US', slow=False) # type: ignore
    audio.save('./DataBase/Voices/Google/')
    time.sleep(1)
    playsound('./DataBase/Voices/Google/')
    return

def chiste():
    playsound('./DataBase/Voices/Amy/Jokes/letMeThinkAmy.mp3')
    time.sleep(1.5)
    aleatorio = random.randrange(7)
    print("Contando chiste:", str(aleatorio))
    if(aleatorio == 1):
        playsound('./DataBase/Voices/Amy/Jokes/joke1Amy.mp3')
    elif(aleatorio == 2):
        playsound('./DataBase/Voices/Amy/Jokes/joke2Amy.mp3')
    elif(aleatorio == 3):
        playsound('./DataBase/Voices/Amy/Jokes/joke3Amy.mp3')
    elif(aleatorio == 4):
        playsound('./DataBase/Voices/Amy/Jokes/joke4Amy.mp3')
    elif(aleatorio == 5):
        playsound('./DataBase/Voices/Amy/Jokes/joke5Amy.mp3')
    elif(aleatorio == 6):
        playsound('./DataBase/Voices/Amy/Jokes/joke6Amy.mp3')  
    else:
        playsound('./DataBase/Voices/Amy/iDontKnowAmy.mp3')
    
    time.sleep(1)
    return

def activarAsistente():
    escuchar()
    while True:
        time.sleep(1)      

#wishme()
activarAsistente()
#hablar("")
#speak("Hello world!")