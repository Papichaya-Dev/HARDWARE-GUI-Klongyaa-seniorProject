import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QStackedWidget
from shared.data.mock.pill_channel_datas import pill_channel_datas
from shared.data.mock.config import config
import speech_recognition as sr

# Screen UI
from screen.homeScreen.main_homeScreen import HomeScreen

haveToTake = []

def speech_recog_function():
    mic = sr.Microphone(1)
    recog = sr.Recognizer()

    with mic as source :
        audio = recog.listen(source)
        text = recog.recognize_google(audio, language="th")
    return text

if __name__ == "__main__":
     app = QApplication(sys.argv)
     defaultfont = QtGui.QFont('Arial', 8)
     defaultfont.setPixelSize(8)
     QtWidgets.QApplication.setStyle("Windows")
     QtWidgets.QApplication.setFont(defaultfont)
     screen = HomeScreen(pill_channel_datas, config)
     widget = QStackedWidget()
     widget.setWindowTitle("GUI - KLONG_YAA")
     widget.addWidget(screen)
     widget.setFixedWidth(1024)
     widget.setFixedHeight(600)
     widget.show()
     sys.exit(app.exec_())