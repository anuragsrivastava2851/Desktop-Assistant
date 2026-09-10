# Desktop-Assistant

A voice-controlled desktop assistant built in Python, developed progressively across multiple levels/iterations — from a basic command-response script to a more complete assistant capable of managing notes, files, applications, and system controls through voice.

---

## 📂 Repository Structure

```
Desktop-Assistant/
│
├── .idea/            # IDE project configuration files
├── jarvis.py         # Current version of the assistant
├── level 1.py         # Initial version — early voice command handling
├── level 2.py         # Iteration 2 — added functionality over level 1
├── level 3.py         # Iteration 3 — added functionality over level 2
├── level 4.py         # Current version of the assistant
├── devlopment.py      # Development/testing script
└── features           # Additional feature-related file
```

The `level 1.py` through `level 4.py` files represent the step-by-step evolution of the assistant as new capabilities were added, with `level 4.py` and `jarvis.py` being the current, most feature-complete versions.

---

## ✨ Features (level 4.py / jarvis.py — Current Version)

- 🗣️ **Voice Command Recognition** using Google Speech Recognition
- 🔊 **Text-to-Speech Responses** via Windows SAPI (`SAPI.SpVoice`)
- 🌐 **Website Launcher** — opens YouTube, Google, Wikipedia, Instagram, and more
- ⏰ **Time Announcement** on voice request
- 📝 **Notes Management** — add, view, and delete voice-dictated notes
- 📁 **File & Folder Operations** — create, open, and rename files/folders on the Desktop
- 🔉 **System Volume Control** — increase/decrease volume via voice
- 🔌 **Power Controls** — shutdown, restart, and sleep the computer
- 🖥️ **Application Launcher** — opens Notepad, Calculator, Paint, Word, and Excel

---

## 🛠️ Tech Stack

| Category            | Technology                              |
|---------------------|-------------------------------------------|
| Language             | Python 3                                |
| Speech Recognition   | `SpeechRecognition` (Google Speech API) |
| Text-to-Speech       | `win32com.client` (Windows SAPI)        |
| System Automation    | `os`, `shutil`, `ctypes`, `subprocess`  |
| Web Interaction      | `webbrowser`                            |
| Platform             | Windows OS                              |

---

## ⚙️ Installation

### Prerequisites
- Python 3.8+
- Windows OS (required for `win32com.client` and SAPI TTS)
- A working microphone

### Setup

```bash
git clone https://github.com/anuragsrivastava2851/Desktop-Assistant.git
cd Desktop-Assistant
pip install SpeechRecognition pywin32 pyaudio
python "level 4.py"
# or
python jarvis.py
```

> 💡 If `pyaudio` fails to install via pip on Windows, install it using a precompiled wheel or via `pipwin install pyaudio`.

---

## 🎯 Usage

Once running, the assistant listens continuously for voice commands. Example commands include:

| Say...                              | Assistant Will...                        |
|--------------------------------------|--------------------------------------------|
| "Open YouTube"                      | Opens YouTube in your default browser      |
| "What's the time"                   | Announces the current system time          |
| "Write" / "Please write"            | Prompts you to dictate and saves a note    |
| "View notes"                        | Reads back all saved notes                 |
| "Delete a note"                     | Asks for a note number and deletes it      |
| "Create folder" / "Create file"     | Creates a new file/folder on the Desktop   |
| "Open file" / "Open folder"         | Opens a specified file/folder              |
| "Rename file" / "Rename folder"     | Renames a specified file/folder            |
| "Increase volume" / "Decrease volume" | Adjusts system volume                    |
| "Open notepad" / "Open calculator"  | Launches the specified application         |
| "Shutdown" / "Restart" / "Sleep"    | Controls system power state                |

---

## ⚠️ Notes

- Requires an active internet connection (Google Speech API) and a working microphone (`device_index` may need adjustment depending on your system's audio devices).
- File/folder deletion via voice exists in the code but is commented out as a safety precaution against accidental data loss.
- Power commands (shutdown/restart/sleep) directly affect the host machine — use with caution while testing.

---

## 📄 License

This project is open-source and available for learning purposes.
