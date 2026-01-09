import speech_recognition as sr
import win32com.client
import webbrowser
import datetime
import os
import shutil
import ctypes
import subprocess

mic = sr.Microphone(device_index=1)
speaker = win32com.client.Dispatch("SAPI.SpVoice")
notes_file = "notes.txt"  # File to store notes

# Get the user's Desktop path
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

# User profiles dictionary
user_profiles = {
    "Anurag": {"name": "Anurag", "favorite_apps": ["notepad", "calculator"]},
    "bob": {"name": "Bob", "favorite_apps": ["paint", "word"]},
    # Add more users if needed
}

def say(text):
    speaker.Speak(text)

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"You said: {query}")
        return query.lower()
    except Exception as e:
        print("Error:", e)
        return ""

def identify_user():
    say("Please say your name.")
    name = takeCommand()
    for user_id, profile in user_profiles.items():
        if profile["name"].lower() in name:
            say(f"Welcome back, {profile['name']}!")
            return profile
    say("User not recognized.")
    return None

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

def open_file_or_folder(name):
    full_path = os.path.join(desktop_path, name)
    try:
        if os.path.exists(full_path):
            os.startfile(full_path)
            say(f"Opening {name}.")
        else:
            say("The specified file or folder does not exist on the Desktop.")
    except Exception:
        say("Sorry, I could not open the file or folder.")

def create_file_or_folder(name):
    full_path = os.path.join(desktop_path, name)
    try:
        if '.' in name:  # File
            with open(full_path, 'w') as f:
                pass
            say(f"File {name} created successfully on the Desktop.")
        else:  # Folder
            os.makedirs(full_path)
            say(f"Folder {name} created successfully on the Desktop.")
    except Exception:
        say("Sorry, I could not create the file or folder.")

def rename_file_or_folder(old_name, new_name):
    old_path = os.path.join(desktop_path, old_name)
    new_path = os.path.join(desktop_path, new_name)
    try:
        os.rename(old_path, new_path)
        say(f"Renamed {old_name} to {new_name} on the Desktop.")
    except Exception:
        say("Sorry, I could not rename the file or folder.")

def delete_file_or_folder(name):
    full_path = os.path.join(desktop_path, name)
    try:
        if os.path.isfile(full_path):
            os.remove(full_path)
            say(f"File {name} deleted successfully from the Desktop.")
        elif os.path.isdir(full_path):
            shutil.rmtree(full_path)
            say(f"Folder {name} deleted successfully from the Desktop.")
        else:
            say("The specified file or folder does not exist on the Desktop.")
    except Exception:
        say("Sorry, I could not delete the file or folder.")

def volume_up():
    for _ in range(5):
        ctypes.windll.user32.keybd_event(0xAF, 0, 0, 0)  # Volume Up
        ctypes.windll.user32.keybd_event(0xAF, 0, 2, 0)
    say("Increased the volume.")

def volume_down():
    for _ in range(5):
        ctypes.windll.user32.keybd_event(0xAE, 0, 0, 0)  # Volume Down
        ctypes.windll.user32.keybd_event(0xAE, 0, 2, 0)
    say("Decreased the volume.")

def shutdown_computer():
    say("Shutting down the computer.")
    os.system("shutdown /s /t 5")

def restart_computer():
    say("Restarting the computer.")
    os.system("shutdown /r /t 5")

def sleep_computer():
    say("Putting the computer to sleep.")
    ctypes.windll.PowrProf.SetSuspendState(0, 1, 0)

def open_application(app_name):
    apps = {
        "notepad": "notepad.exe",
        "calculator": "calc.exe",
        "paint": "mspaint.exe",
        "word": r"C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE",
        "excel": r"C:\Program Files\Microsoft Office\root\Office16\EXCEL.EXE",
    }
    app = apps.get(app_name.lower())
    if app:
        try:
            subprocess.Popen(app)
            say(f"Opening {app_name}.")
        except Exception:
            say(f"Sorry, I could not open {app_name}.")
    else:
        say(f"{app_name} is not in the applications list.")

if __name__ == '__main__':
    user = identify_user()
    if not user:
        say("Sorry, I cannot proceed without recognizing the user.")
    else:
        say(f"Hello, {user['name']}. I am Jarvis, your personal assistant.")

        while True:
            print("Listening...")
            query = takeCommand()

            if not query:
                continue

            # Website opener
            sites = {
                "youtube": "https://www.youtube.com",
                "wikipedia": "https://www.wikipedia.org",
                "google": "https://www.google.com",
                "instagram": "https://www.instagram.com"
            }
            for site_name, url in sites.items():
                if f"open {site_name}" in query:
                    say(f"Opening {site_name} sir...")
                    webbrowser.open(url)
                    break

            # Time
            if "the time" in query or "time" in query:
                strfTime = datetime.datetime.now().strftime("%H:%M:%S")
                say(f"Sir, the time is {strfTime}")

            # Notes
            if "add " in query or "please write" in query or "write" in query:
                say("What would you like to note down?")
                note = takeCommand()
                add_note(note)

            if "view notes" in query or "show me notes" in query or "open notes" in query or "i want to see" in query:
                view_notes()

            if "delete notes" in query or "delete a note" in query or "i want to delete" in query:
                delete_note()

            # File and folder management
            if "open file" in query or "open folder" in query:
                say("Please tell me the name of the file or folder on the Desktop to open.")
                name = takeCommand()
                open_file_or_folder(name)

            if "create file" in query or "create folder" in query:
                say("Please tell me the name of the file or folder to create on the Desktop.")
                name = takeCommand()
                create_file_or_folder(name)

            if "rename file" in query or "rename folder" in query:
                say("Please tell me the current name of the file or folder on the Desktop.")
                old_name = takeCommand()
                say("Please tell me the new name of the file or folder.")
                new_name = takeCommand()
                rename_file_or_folder(old_name, new_name)

            if "delete file" in query or "delete folder" in query:
                say("Please tell me the name of the file or folder on the Desktop to delete.")
                name = takeCommand()
                delete_file_or_folder(name)

            # System control commands
            if "volume up" in query or "increase volume" in query or "increase the volume" in query or "increase" in query:
                volume_up()

            if "volume down" in query or "decrease volume" in query or "decrease the volume" in query or "decrease" in query:
                volume_down()

            if "shutdown" in query:
                shutdown_computer()

            if "restart" in query:
                restart_computer()

            if "sleep" in query:
                sleep_computer()

            if "open" in query and any(app in query for app in user['favorite_apps']):
                for app in user["favorite_apps"]:
                    if app in query:
                        open_application(app)
                        break
