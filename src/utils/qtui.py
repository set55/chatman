from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QInputDialog
from PyQt5.QtGui import QFont
import sys

class QtInterface(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Chatman')
        self.setGeometry(100, 100, 300, 200)

        layout = QVBoxLayout()

        self.word_input = QLineEdit(self)
        self.word_input.setPlaceholderText("Enter any word you want")
        layout.addWidget(self.word_input)

        self.start_button = QPushButton('Start', self)
        self.start_button.setShortcut('Return')
        self.start_button.clicked.connect(self.enter)
        layout.addWidget(self.start_button)

        self.setLayout(layout)
    
    def enter(self):
        inputText = self.word_input.text().strip()
        print(inputText)
        self.show_message('Info', f"Text detected: {inputText}")

    def set_click_event(self, function):
        self.start_button.clicked.connect(function)

    def show_message(self, title, text, icon=QMessageBox.Information):
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle(title)
        msg_box.setText(text)
        msg_box.setIcon(icon)
        # msg_box.setFont(QFont('Arial', 14))  # Set font size
        # msg_box.setStyleSheet("QLabel{min-width: 300px; min-height: 100px; text-align: left;}")  # Set minimum size and align text left
        msg_box.exec_()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = QtInterface()
    ex.show()
    sys.exit(app.exec_())