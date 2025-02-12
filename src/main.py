from utils.speakbot import SpeakBot
from utils.listenbot import ListenBot
from utils.thinker import Thinker
import speech_recognition as sr

if __name__ == "__main__":
    speak = SpeakBot()
    listen = ListenBot()
    mind = Thinker()
    with sr.Microphone() as source:
        # Adjust for ambient noise and record the audio
        listen.recognizer.adjust_for_ambient_noise(source)
        while True:
            text = listen.listen(source)
            if text:
                print(f"Text detected: {text}")
                res = mind.think(text)
                if res == "":
                    continue
                audio_data, sample_rate = speak.generate_speech(res)
                speak.play_speech(audio_data, sample_rate)