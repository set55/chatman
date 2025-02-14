from PyQt5.QtWidgets import QApplication
import sys
from utils.speakbot import SpeakBot
from utils.thinker import Thinker
from utils.qtui import QtInterface
from utils.storage import Storage


def AskLLM(mind, speak, storage, text):
    res = mind.think(text)
    if res == "":
        return
    try:
        print(f"####Ai Response: {res}")
        # after thinking, save the history message
        storage.save_history_message(mind.history_message)
        audio_data, sample_rate = speak.generate_speech(res)
        speak.play_speech(audio_data, sample_rate)
    except ValueError:
        print("Error in generating speech")

if __name__ == "__main__":
    storage = Storage()
    speak = SpeakBot()
    mind = Thinker(storage.get_history_message(), storage.get_system_message())
    app = QApplication(sys.argv)
    ex = QtInterface()
    ex.set_click_event(lambda: AskLLM(mind, speak, storage, ex.word_input.text().strip()))
    ex.show()
    sys.exit(app.exec_())
    