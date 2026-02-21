import subprocess
import sounddevice as sd
import numpy as np


class PiperTTS:
    def __init__(self, model_path, piper_binary):

        self.sample_rate = 22050

        self.process = subprocess.Popen(
            [
                piper_binary,
                "--model", model_path,
                "--output-raw",
                "--length_scale", "0.9"
            ],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
            bufsize=0
        )


    def _synthesize_and_play(self, text):
        self.process.stdin.write((text + "\n").encode("utf-8"))
        self.process.stdin.flush()

        audio_chunks = []

        while True:
            chunk = self.process.stdout.read(4096)
            if not chunk:
                break

            audio_chunks.append(chunk)

            if len(chunk) < 4096:
                break

        if audio_chunks:
            audio = b"".join(audio_chunks)

            audio_np = (
                np.frombuffer(audio, dtype=np.int16)
                .astype(np.float32) / 32768.0
            )

            sd.play(audio_np, self.sample_rate)
            sd.wait()   

    def speak(self, text):
        try:
            # Stop any currently playing audio
            sd.stop()


            self._synthesize_and_play("जी.....")

            
            self._synthesize_and_play(text)

        except Exception as e:
            print("TTS Error:", e)
