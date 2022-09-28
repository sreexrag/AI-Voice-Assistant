import os
import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import wikipedia
import random
import pywhatkit
import pyjokes

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour<12:
        speak("Good Morning")
    elif hour >=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")

    speak("I am Jacqueline..Your personal assistant")


def takeCommand():
    #Microphone input from User

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.adjust_for_ambient_noise(source,duration=0.5)
        r.pause_threshold = 1
        audio =r.listen(source)

    try:
        print("Recognizing..")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)

        print("Say that again")
        return "None"
    return query
if __name__ == '__main__':
    wishMe()
    if 1:
        query=takeCommand().lower()

        if 'who is'in query:
            person=query.replace('wikipedia','')
            results=wikipedia.summary(person,sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'what is'in query:
            person=query.replace('wikipedia','')
            results=wikipedia.summary(person,sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
            
        elif 'where is'in query:
            person=query.replace('wikipedia','')
            results=wikipedia.summary(person,sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
            
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is{strTime}")

        elif 'open code' in query:
            codepath= "C:\\Users\\harik\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)

        elif 'open spotify' in query:
            spotify_path= "C:\\Users\\harik\\AppData\\Roaming\\Spotify\\Spotify.exe"
            os.startfile(spotify_path)

        elif 'play' in query:
            b='Opening Youtube'
            engine.say(b)
            engine.runAndWait()
            pywhatkit.playonyt(query)

        elif 'joke' in query:
            speak(pyjokes.get_joke())

        elif 'how are you' in query:
            speak('I am fine thanks..Hope you are doing well too')

        elif 'bored' in query:
            speak('Of course you are...because you dont have anyone to text or talk.Get a life dude..')

        elif 'alexa' in query:
            speak('Dont talk to me about her...I hate that bitch')

        elif 'sorry' in query:
            speak('Oh its OK...Dont repeat it')

        elif 'love' in query:
            speak('I love you too...but as a brother')

        elif 'you are funny' in query:
            speak('Ya its good that atleast one of us is funny..')

        elif 'Are you single' in query:
            speak('No I am not...I am in deeply love with cloud')

        elif 'hi' in query:
            speak('Hello there mate..How is your day going')

        elif 'hai' in query:
            speak('Hello dude.Hope your day is going fine')

        elif 'who made you' in query:
            speak('A geek named Sreerag made me')
            

        else:
            speak('Say that correctly...You fool')





            

            

    
