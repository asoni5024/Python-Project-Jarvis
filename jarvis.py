import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir!")
    
    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir!")
    else:
        speak("Good Evening Sir!")
    speak("I am jarvis Sir.Please tell me how may I help you")

def takeCommand():
    # it takes microphone input from the user and return string output
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....!")
        r.pause_threshold = 1.0
        audio = r.listen(source)
    
    try:
        print("Recognizing....!")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    
    except Exception as e:
        print(e)
        print("Say that again please....!")
        return "None"
    return query

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com')
    server.ehlo()
    server.starttls()
    server.login('asoni1814@gmail.com', 'angelgupta')
    server.sendmail('asoni1814@gmail.com', to, content)
    server.close()



if __name__ == "__main__":
    wishMe()
    
    while True:
        query = takeCommand().lower()
       # logic for executing task 
        if 'wikipedia' in query:
            speak('Searching Wikipedia....!')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=4)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak("Ok Sir")
            webbrowser.open("www.youtube.com")

        elif 'open google' in query:
            speak("Ok Sir")
            webbrowser.open("www.google.com")

        elif 'open gmail' in query:
            speak("Ok Sir")
            webbrowser.open("www.gmail.com")

        elif 'open stackoverflow' in query:
            speak("Ok Sir")
            webbrowser.open("stackoverflow.com")  

        elif 'play music' in query:
            speak("Ok Sir")
            music_dir = 'F:\\New folder'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            speak("Ok Sir")
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir,the time is {strTime}")

        elif 'open visual studio' in query:
            speak("Ok Sir")
            visualcode = "C:\\Project\\Microsoft VS Code\\Code.exe"
            os.startfile(visualcode)

        elif 'email to aman' in query:
            try:
                speak("Ok Sir")
                speak("What should I say?")
                content = takeCommand()
                to = "asoni1814@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend aman.I am not able to send this email")

        elif 'exit' in query:
            speak("Bye Sir! Have a good day")
            exit()