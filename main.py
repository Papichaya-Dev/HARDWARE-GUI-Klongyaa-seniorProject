import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QStackedWidget
#from shared.data.mock.pill_channel_datas import pill_channel_datas
from shared.data.light_list import lightList
from shared.data.mock.config import config
import speech_recognition as sr
from screen.pillSummaryScreen.main_pillSummaryScreen import PillSummaryScreen
from screen.inputTimesToTakePill.main_inputTimesToTakePill import *

import requests

# Screen UI
from screen.homeScreen.main_homeScreen import HomeScreen

haveToTake = []

def speech_recog_function():
    mic = sr.Microphone(2)
    recog = sr.Recognizer()

    with mic as source :
        audio = recog.listen(source)
        text = recog.recognize_google(audio, language="th")
    return text

if __name__ == "__main__":
     pill_channel_datas = {
         "0": {},
         "1": {},
         "2": {},
         "3": {},
         "4": {},
         "5": {},
         "6": {}
         }
     res = requests.get(config["url"] + "/pill-data/getHardwarePillChannelDatas/" + config["userId"])
     
     for pill in res.json()['pill_channel_datas']:
         times = []
         for time in pill['take_times']:
             times.append(time.replace('.', ':'))
             
         idStr = str(int(pill['channel_id']) - 1)
         pill_channel_datas[idStr]['id'] = int(idStr)
         pill_channel_datas[idStr]['name'] = pill['pill_name']
         pill_channel_datas[idStr]['totalPills'] = pill['total']
         pill_channel_datas[idStr]['pillsPerTime'] = pill['pillsPerTime']
         pill_channel_datas[idStr]['timeToTake'] = times
     print(pill_channel_datas)
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