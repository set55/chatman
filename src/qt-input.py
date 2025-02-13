from utils.speakbot import SpeakBot
from utils.thinker import Thinker
from utils.qtui import QtInterface
from PyQt5.QtWidgets import QApplication
import sys


def AskLLM(mind, speak, text):
    res = mind.think(text)
    if res == "":
        return
    try:
        print(f"####Ai Response: {res}")
        audio_data, sample_rate = speak.generate_speech(res)
        speak.play_speech(audio_data, sample_rate)
    except ValueError:
        print("Error in generating speech")

if __name__ == "__main__":
    speak = SpeakBot()
    mind = Thinker()
    app = QApplication(sys.argv)
    ex = QtInterface()
    ex.set_click_event(lambda: AskLLM(mind, speak, ex.word_input.text().strip()))
    ex.show()
    sys.exit(app.exec_())
    