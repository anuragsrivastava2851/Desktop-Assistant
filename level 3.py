import speech_recognition as sr
import win32com.client
import webbrowser
import datetime
import os

mic = sr.Microphone(device_index=1)
speaker = win32com.client.Dispatch("SAPI.SpVoice")
notes_file = "notes.txt"  # File to store notes

def say(text):
    speaker.Speak(text)

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)

        try:
            print("recognizing....")
            query = r.recognize_google(audio, language="en-in")
            print(f"You said: {query}")
            return query
        except Exception as e:
            return "Sorry, I could not understand the audio."

def add_note(note):
    with open(notes_file, "a") as file:
        file.write(note + "\n")
    say("Note added successfully.")

def view_notes():
    if os.path.exists(notes_file):
        with open(notes_file, "r") as file:
            notes = file.readlines()
            if notes:
                say("Here are your notes.")
                for note in notes:
                    print(note.strip())
                    say(note.strip())
            else:
                say("You have no notes.")
    else:
        say("You have no notes.")

def delete_note():
    if os.path.exists(notes_file):
        with open(notes_file, "r") as file:
            notes = file.readlines()

        if notes:
           
           
            say("Here are your notes:")
            for index, note in enumerate(notes, start=1):
                print(f"{index}: {note.strip()}")
                say(f"{index}: {note.strip()}")

            say("Which note would you like to delete? Please say the note number.")
            note_number = takeCommand()
            try:
                note_index = int(note_number) - 1
                if 0 <= note_index < len(notes):
                    deleted_note = notes[note_index].strip()
                    del notes[note_index]
                    with open(notes_file, "w") as file:
                        file.writelines(notes)
                    say(f"Deleted note: {deleted_note}")
                else:
                    say("Invalid note number.")
            except ValueError:
                say("Please say a valid number.")
        else:
            say("You have no notes to delete.")
    else:
        say("You have no notes to delete.")

if __name__ == '__main__':
    say("Hello, I am Jarvis, your personal desktop assistant.")

    while True:
        print("listening.......")
        query = takeCommand()  
        sites = [["youtube", "https://www.youtube.com"], ["wikipedia", "https://www.wikipedia"],
                 ["google", "https://www.google.com"], ["instagram", "https://www.instagram.com"]]

        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]} sir...")
                webbrowser.open(site[1])

        if "the time" in query:
            strfTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"Sir, the time is: {strfTime}")
            say(f"Sir, the time is {strfTime}")

        if "add " in query or "please write" in query or "write" in query:
            say("What would you like to note down?")
            note = takeCommand()
            add_note(note)

        if "view notes" in query or "show me" in query or "open" in query or "i want to see" in query:
            view_notes()

        if "delete a note" in query or "i want to delete" in query:
            delete_note()
