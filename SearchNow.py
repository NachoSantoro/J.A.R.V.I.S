import speech_recognition
from speech_recognition import Microphone, Recognizer, AudioFile, UnknownValueError, RequestError
from playsound import playsound
import pyttsx3
import pywhatkit
import wikipedia
import webbrowser


def takeCommand(recognizer, source):

    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,4)
    try:
        print("Understanding..")
        reconocer = recognizer.recognize_google(source, language='us-US')
        texto = str(reconocer).lower()
        print("I've heard:", texto)
    except RequestError as exc:
        print("Error al escuchar: ", exc)
    except UnknownValueError:
        playsound('./DataBase/Voices/Brian/dontUnderstandBrian.mp3')
    return

#query = takeCommand().lower()  # type: ignore

engine = pyttsx3.init('sapi5')

def Speak(audio):
    print("     ")
    print(f": {audio}")
    print("     ")
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[7].id)
    engine.setProperty('rate', 170)
    engine.say(audio)
    engine.runAndWait()

def searchGoogle(texto: str):
    if (texto.__contains__("google")):
        import wikipedia as googleScrap
        texto = texto.replace("jarvis","")
        texto = texto.replace("google search","")
        texto = texto.replace("google","")
        Speak("This is what I found on google")

        try:
            pywhatkit.search(texto)
            result = googleScrap.summary(texto,1)
            Speak(result)

        except:
            Speak("No speakable output available")

def searchYoutube(texto: str):
    if (texto.__contains__("youtube")):
        Speak("This is what I found for your search!") 
        texto = texto.replace("youtube search","")
        texto = texto.replace("youtube","")
        texto = texto.replace("jarvis","")
        web  = "https://www.youtube.com/results?search_query=" + texto
        webbrowser.open(web)
        pywhatkit.playonyt(texto)
        Speak("Done, Sir")

def searchWikipedia(texto: str):
    if (texto.__contains__("wikipedia")):
        Speak("Searching from wikipedia....")
        texto = texto.replace("wikipedia","")
        texto = texto.replace("search wikipedia","")
        texto = texto.replace("jarvis","")
        results = wikipedia.summary(texto,sentences = 2)
        Speak("According to wikipedia..")
        print(results)
        Speak(results)