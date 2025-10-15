import os
import pyttsx3
import speech_recognition as sr
import wikipedia 
import datetime 
import webbrowser
# import smtplib 


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    # hour = int(datetime.datetime.now().hour)
    # if hour>=0 and hour<12:
    #         speak("Good morning")
    # elif hour>=12 and hour<18:
    #         speak("Good Afternoon")
    # else: 
    #         speak("Good night")

    # speak("salam, sir , I am senti . How may i help you?")
    speak("SIR I AM EDIT . HOW MAY I HELP YOU ? ")

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"user said: {query}\n")  
    except Exception as e:
        print("say that again please...")
        return "None"
    return query
if __name__ =="_main_":
    wishme()
    while True:
    # if 1 :
     query = takecommand().lower()
     if 'wikipedia' in query:
        speak('searching wikipedia..')
        query = query.replace("wikipedia","")
        results = wikipedia.summary(query,sentences=2)
        speak("according to wikipedia")
        print(results)
        speak(results)

     elif 'youtube' in query:
         webbrowser.open("youtube.com")
     elif 'google' in query:
         webbrowser.open("google.com")
     elif 'read it' in query:
         speak('Enter your text sir')
         text = input("Enter your text = ")
         speak(text)
        
     elif 'time' in query:
         strTime = datetime.datetime.now().strftime("%H:%M:%S")
         speak(f"sir,the time is{strTime} ")
     elif 'vs code' in query:
        codePath="C:\\Users\\Adiiiii\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(codePath)
     elif 'telegram' in query:
        codePath = "C:\\Users\\Adiiiii\\AppData\\Roaming\\Telegram Desktop\\Telegram.exe"  
        os.startfile(codePath)
     elif 'whatsapp' in query:
        codePath = "C:\\Users\\Adiiiii\\AppData\\Local\\WhatsApp\\WhatsApp.exe" 
        os.startfile(codePath)
     elif 'microsoft word' in query:
        codePath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE" 
        os.startfile(codePath)
    # This is for app opening in voice command

    #  elif '' in query:
    #     codePath =   
    #     os.startfile(codePath)
    #  elif '' in query:
    #     codePath =   
    #     os.startfile(codePath)
    
     elif 'who are you' in query:
         speak("I am senti.. An A.I. is making by aditya")
     elif 'tumi k' in query:
         speak("I am senti.. An A.I. is making by aditya")
     elif 'thanks' in query:
         speak("You are most welcome sir")

     elif 'bye bye' in query:
         speak("ok sir have a good day")
         exit()
     elif 'tata' in query:
         speak("ok sir have a good day")
         exit()
     elif 'bye' in query:
         speak("ok sir have a good day")
         exit()
     elif 'good night' in query:
         speak("ok sir have a good day")
         exit()
    #  elif 'off' in query:
    #      speak("ok sir have a good day")
    #      exit()
    #  elif 'bondho' in query:
    #      speak("ok sir have a good day")
    #      exit()
    #  elif 'ghumai jaw' in query:
    #      speak("ok sir have a good day")