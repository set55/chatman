import speech_recognition as sr
from utils.speakbot import SpeakBot
from utils.listenbot import ListenBot
from utils.thinker import Thinker
from utils.storage import Storage


if __name__ == "__main__":
    storage = Storage()
    speak = SpeakBot()
    listen = ListenBot()
    mind = Thinker(storage.get_history_message(), storage.get_system_message())
    
    while True:
        with sr.Microphone() as source:
            # Adjust for ambient noise and record the audio
            listen.recognizer.adjust_for_ambient_noise(source)
            print("Listening...")
            text = listen.listen(source)
            if text:
                print(f"Text detected: {text}")
                res = mind.think(text)
                if res == "":
                    continue
                try:
                    # after thinking, save the history message
                    storage.save_history_message(mind.history_message)
                    audio_data, sample_rate = speak.generate_speech(res)
                    speak.play_speech(audio_data, sample_rate)
                except ValueError:
                    print("Error in generating speech")
                    continue