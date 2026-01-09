import speech_recognition as sr
import win32com.client
import webbrowser
import openai
import datetime

mic = sr.Microphone(device_index=1)

speaker = win32com.client.Dispatch("SAPI.SpVoice")


def say(text):
    speaker.Speak(text)


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # r.pause_threshold= 1
        audio = r.listen(source)

        try:
            print("recognizing....")
            query = r.recognize_google(audio, language="en-in")
            print(f"You said: {query}")
            return query
        except Exception as e:

            return "Sorry, I could not understand the audio."


if __name__ == '__main__':
    say("Hello, I am Nexus your personal chatbot.")

    while True:
        print("listening.......")
        query = takeCommand() 
        sites = [["youtube", "https://www.youtube.com"], ["wikipedia", "https://www.wikipedia"],
                 ["google", "https://www.google.com"], ["instagram", "https://www.instagram.com"]]

        for site in sites: 
            if f"Open {site[0]}".lower() in query.lower():  
                say(f"opening the {site[0]} sir...")
                webbrowser.open(site[1])  
        # say(query)     

        if "the time" in query:
            strfTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"Sir the time is : {strfTime}")
            say(f" Sir the time is{strfTime}")




