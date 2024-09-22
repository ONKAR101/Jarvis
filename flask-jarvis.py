import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser

from flask import Flask, render_template, request

app = Flask(__name__)

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voices[1].id)

@app.route('/')
def index():
    # varspeak = wishme()
    return render_template('index.html')

@app.route('/add', methods=['POST'])
def add():    
    while True:
        query = takecommand().lower()
        
        #logic for executing takes based on query
        if 'wikipedia' in query:
            speak('searching wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
            
        elif 'open youtube' in query:
            print("Opening youtube")
            webbrowser.open("youtube.com")
            
        elif 'open google' in query:
            print("Opening google")
            webbrowser.open("google.com")
            
        elif 'open photos' in query:
            print("Opening photos")
            webbrowser.open("photos.com")
        
        elif 'stop' in query:
            engine.stop()

engine.setProperty('voice',voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak ("good morning!")
        varspeak = "good morning"
        
    elif hour>=12 and hour<=18:
        speak("good Afternoon!")
        varspeak = "good Afternoon"
        
    else :
        speak("I am jarvis. please tell me how may i help you")
        varspeak = "I am jarvis. please tell me how may i help you"
     
    return varspeak   
    # return render_template('index.html', varspeak=varspeak)
   
def takecommand():
      # it takes microphone input from the user and returning string output 
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listing.....")
        r.pause_threshold = 1
        audio = r.listen(source)
        
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"user said:{query}\n")
            
        except Exception as e:
            #print(e)
            print("say that again please...")
            return "None"
        return query
            
if __name__  == "__main__":
    app.run(debug=True)
        
            
    
