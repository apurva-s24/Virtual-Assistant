import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import sys
# import speechRecognition as sr
import speech_recognition as sr


emails = {'name': 'youremailaddress'}
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning")
    elif hour >= 12 and hour <18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    
    speak("I am zira, Please tell me how I help you")


def takeCommand():
    # It takes microphone input from the users and return string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query2 = r.recognize_google(audio, language='en-in')
        print(f"User said: {query2}")
       

    except Exception as e:
        print(e)
        print("Say that again please...")
        speak("Say that again please...")
        return "None"
    return query2


def sendEmail(to, content):
    # Use SMTP protocol - search=less secure apps in gmail
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremailaddress', 'your-password')
    server.sendmail('youremailaddress', to, content)
    server.close()



if __name__ == '__main__':
    wishMe()
    while True:
        query = takeCommand().lower()

        # logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak('okay')
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak('okay')
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            speak('okay')
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            speak('okay')
            music_dir = 'E:\\music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")

        elif 'open code' in query:
            speak('okay')
            codePath = "D:\\myVSCode\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)   

        elif 'send email' in query:
            speak('okay')
            try:
                speak("What should I say")
                content = takeCommand()
                to = "youremailaddress"
                sendEmail(to, content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("Sorry friend, I am not able to send this email")

        elif 'exit' in query:
            sys.exit()
