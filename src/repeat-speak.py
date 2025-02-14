from utils.speakbot import SpeakBot
from utils.listenbot import ListenBot
import speech_recognition as sr

if __name__ == "__main__":
    speak = SpeakBot()
    listen = ListenBot()

    while True:
        with sr.Microphone() as source:
            # Adjust for ambient noise and record the audio
            listen.recognizer.adjust_for_ambient_noise(source)
            print("Listening...")
            text = listen.listen(source)
            if text:
                print(f"Text detected: {text}")
                audio_data, sample_rate = speak.generate_speech(text)
                speak.play_speech(audio_data, sample_rate)