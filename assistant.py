import sounddevice as sd
import queue
import json
import time
from vosk import Model, KaldiRecognizer

from intent import get_intent
from actions import perform_action
from piper_tts import PiperTTS


# -----------------------------
# Load Vosk Model
# -----------------------------
model = Model("vosk-model-small-hi-0.22")
rec = KaldiRecognizer(model, 16000)

rec.SetWords(False)
rec.SetPartialWords(False)
rec.SetMaxAlternatives(0)


# -----------------------------
# Load Piper TTS
# -----------------------------
tts = PiperTTS(
    "/home/pi/Hindi_Voice_Assistant/model_data/hi_IN-pratham-medium.onnx",
    "/home/pi/Hindi_Voice_Assistant/piper/piper"
)


# -----------------------------
# Audio Queue
# -----------------------------
q = queue.Queue()
stream = None


def callback(indata, frames, time_info, status):
    if status:
        print("Audio status:", status)
    q.put(bytes(indata))


print("Hindi Voice Assistant चालू है...")


# -----------------------------
# Speak Function (Mic Fully Paused)
# -----------------------------
def speak(text):
    global stream

    # Stop microphone completely
    stream.stop()
    rec.Reset()

    tts.speak(text)

    time.sleep(0.5)  # wait a little after speaking

    # Restart microphone
    stream.start()


# -----------------------------
# Process Command
# -----------------------------
def process_command(text):

    text = text.strip()

    # Ignore small noise words
    if len(text.split()) < 2:
        return

    print("🎤 Command:", text)

    intent = get_intent(text)
    response = perform_action(intent)

    print("🤖 Response:", response)

    speak(response)


# -----------------------------
# Start Audio Stream
# -----------------------------
try:
    stream = sd.RawInputStream(
        samplerate=16000,
        blocksize=4096,
        dtype='int16',
        channels=1,
        callback=callback
    )

    stream.start()

    while True:
        data = q.get()

        if rec.AcceptWaveform(data):
            result = json.loads(rec.Result())
            text = result.get("text", "").strip()

            if text:
                process_command(text)

except KeyboardInterrupt:
    print("\n🛑 Assistant बंद किया गया")
    stream.stop()

except Exception as e:
    print("Error:", e)
    stream.stop()
