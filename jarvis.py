import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
engine= pyttsx3.init('sapi5')
voices= engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def wishMe():
    hour= int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
        
    speak("I am Jarvis sir. please tell me how may i help you")
 
def takeCommand():
    r= sr.Recognizer() 
    with sr.Microphone() as source:
     print("Listening...")
     r.pause_threshold= 1
     audio= r.listen(source)
     
    try:
        print("Recognizing...")
        query=r.recognize_google(audio, language='en-in')
        print(f"user said:{query}\n")
        
    except Exception as e:
        print("Say that again please...")
        return "none"
    return query

    
if __name__ == "__main__":
   wishMe()
   while True:
     query=takeCommand().lower()
     if query == "none":
       continue

     
     if 'wikipedia' in query:
         speak('searching wikipedia...')
         query=query.replace("wikipedia","")
         results= wikipedia.summary(query, sentences=2)
         speak("According to wikipedia")
         print(results)
         speak(results)
         
     elif 'open Youtube' in query:
         webbrowser.open("youtube.com")
     elif 'open google' in query:
         webbrowser.open("https://www.google.com")
     elif 'open amazon' in query:
         webbrowser.open("amazon.com")
     elif 'open cricbuzz' in query:
         webbrowser.open("https://www.cricbuzz.com")
     elif 'open flipkart' in query:
         webbrowser.open("https://www.flipkart.com/")
     elif 'open hotstar' in query:
         webbrowser.open("www.hotstar.com")
     elif 'the time' in query:
         strTime= datetime.datetime.now().strftime("%H:%M:%S")
         speak(f"sir, the time is {strTime}")
         
     elif 'open code' in query:
        codepath="C:\\Users\\rishi\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(codepath)
     elif 'quit' in query or 'exit' in query or 'stop' in query:
            speak("Goodbye sir! Have a nice day.")
            break
         
         
         
     
         
         
         
   
        
     