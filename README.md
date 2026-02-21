# Offline, Privacy-Preserving Hindi Voice Assistant on Raspberry Pi

An offline Hindi Voice Assistant built using Raspberry Pi, Vosk ASR, and Piper TTS.

This project demonstrates real-time Hindi speech recognition and response generation without requiring internet connectivity.

---

## Project Overview

This system is designed to:

- Recognize predefined Hindi voice commands
- Process user intent
- Generate appropriate responses
- Speak responses using a male Hindi voice
- Operate completely offline

The assistant is optimized for Raspberry Pi and low-resource environments.

---

## Features

-  Offline Hindi Speech Recognition (Vosk)
-  Offline Hindi Text-to-Speech (Piper TTS)
-  15 predefined Hindi commands
-  Echo-loop prevention
-  Stable microphone handling
-  Lightweight Raspberry Pi implementation
-  Modular and scalable architecture

---

## Supported Hindi Commands

| Command | Function |
|----------|----------|
| समय बताएं | Tells current time |
| तारीख बताएं | Tells current date |
| आज कौन सा दिन है | Tells current day |
| नमस्ते | Greeting |
| मौसम | Weather (placeholder response) |
| तुम्हारा नाम क्या है | Assistant name |
| तुम कौन हो | About assistant |
| धन्यवाद | Acknowledgement |
| गूगल खोलो | Opens Google |
| यूट्यूब खोलो | Opens YouTube |
| गाना बजाओ | Plays music |
| कैलकुलेटर खोलो | Opens calculator |
| बैटरी | Battery status (placeholder) |
| मदद | Lists supported commands |
| बंद करो | Stops assistant |

---

## System Architecture

```
User Speech
    ↓
Microphone (sounddevice)
    ↓
Vosk ASR Engine
    ↓
Intent Detection (intent.py)
    ↓
Action Processing (actions.py)
    ↓
Text Response
    ↓
Piper TTS
    ↓
Speaker Output
```

---

## Technologies Used

- Python 3
- Raspberry Pi (ARM architecture)
- Vosk Speech Recognition
- Piper TTS
- sounddevice
- NumPy

---

## Project Structure

```
Hindi_Voice_Assistant/
│
├── assistant.py # Main execution file
├── intent.py # Intent recognition logic
├── actions.py # Response & system actions
├── piper_tts.py # TTS interface
│
├── docs/
│ └── Final_Report.pdf
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Installation Guide

### Step-1 Clone Repository

git clone https://github.com/abhisarchauhan1003/Offline_Privacy_Preserving_Hindi_Voice_Assistant_on_Raspberry_Pi

### Step-2 Install Dependencies

pip install -r requirements.txt

If you get PortAudio error on Raspberry Pi:
sudo apt install portaudio19-dev


### Step-3 Download Required Models

Models are not included due to large file size.

Download:

1- Vosk Hindi Model: https://alphacephei.com/vosk/models
Recommended: vosk-model-small-hi-0.22

Extract into project folder.

2- Piper Hindi Model: https://github.com/rhasspy/piper
Download Hindi ONNX model and place inside: model_data/


### Step-4 Run Assistant

python assistant.py

---

Implementation Highlights:

- Only final ASR results are processed (no unstable partial triggers)

- Microphone is paused during TTS playback

- Recognizer reset prevents echo-loop repetition

- Noise filtering ignores single-word triggers

- Modular design for easy extension

---

Results:

- Real-time response latency under 2 seconds

- Stable offline recognition

- No echo feedback loop

- Lightweight execution on Raspberry Pi

---

Limitations:

- Limited to predefined commands

- Weather and battery features currently placeholders

- No wake-word detection (can be added in future)

---

Future Improvements:

- Wake word detection

- Noise suppression

- Expanded command set

- Smart home integration

- GUI dashboard

- Multilingual support

---

Documentation:

Full details are available in: docs/Final_Report.pdf

---

Authors: 

Abhisar Chauhan
Electronics & Communication Engineering
Chandigarh University

Harshada Kajale
Electronics & Communication Engineering
Chandigarh University

Yash Maggu
Electronics & Communication Engineering
Chandigarh University

---

License:

This project is for academic and educational purposes.

