import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voices', voices[1].id)




def speak(audio):
    engine.say(audio)
    engine.runAndWait()
 
    
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning")
        
    elif hour>=12 and hour<18:
         speak("good afternoon")
         
    else:
          speak("good evening")
          
    speak("i am jarvis sir. please tell me how may help you")
    
    
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)
        
    try:
        print("recognizing....")
        query = r.recognize_google(audio, Language='en-in')
        print(f"user said:{query}\n")   
        
    except Exception as e:
        # print(e)
        
        print("say that again please....")
        return "None"
    return query



if __name__=="__main__":
   wishMe()
   
   while True:
        query=takecommand().lower()
        
        
        if 'wikipedia' in query:
            speak('searching wikipedia..')
            query = query.replace("wikipedia","")
            result=wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            speak(result)
            
        elif 'youtube' in query:
            webbrowser.open("youtube.com")
        
