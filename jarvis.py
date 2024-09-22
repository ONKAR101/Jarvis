import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import pyautogui

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voices[1].id)

engine.setProperty('voice',voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak ("good morning!")
        
    elif hour>=12 and hour<=18:
        speak("good Afternoon!")
        
    else :
        speak("good morning!")        
        speak("I am jarvis .please tell me how may i help you")
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
    wishme()
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
 

def listen_for_scroll_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("bolne ke liye tayar hai...")
        audio = recognizer.listen(source)
        try:
            command=recognizer.reconize_google(audio)
            print(f"Apne kaha:{command}")
            return command
        except sr.UnknownValueError:
            print("samajh nahi aaya.")
            return None
        while true:
            command = listen_for_scroll_command()
            if command and "scroll"in command.lower():
                pyautogui.scroll(-100)#scroll down
                print("scrolling")            

