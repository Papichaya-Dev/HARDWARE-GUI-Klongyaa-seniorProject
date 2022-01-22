from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog
import __main__
from screen.inputPillNameScreen.main_inputPillnameScreen import InputPillNameScreen
from screen.pillDetailScreen.main_detail_screen import DetailScreen
from functools import partial

from PyQt5.QtCore import QObject, QThread, pyqtSignal
from time import sleep
from datetime import datetime, timedelta

import threading
import time
from pygame import mixer


isChangePage = False
isSoundOn = False
mixer.init()
sound_notification = mixer.Sound("screen\homeScreen\sound_notification.wav")
print(sound_notification)
 #---------------- Function play sound notification ----------------#
def releaseCooldown():
    global sound_cooldown
    sound_cooldown = False

def playSound():
    sound_notification.play(time.daylight)
    sound_cooldown = True
    threading.Timer(2, releaseCooldown).start()

def stopSound():
    sound_notification.stop()
class HomeScreen(QDialog):
    def __init__(self, pill_channel_datas, config):
        super().__init__()
        self.pill_channel_datas = pill_channel_datas
        self.config = config
        global isChangePage
        isChangePage = False
        self.setupUi(self)
    
    def setupUi(self, UIHomeScreen):
        pill_channel_buttons = []
        pill_channel_datas = self.pill_channel_datas
        width_height_of_channel = [
            [0, 0, 510, 200],
            [510, 0, 510, 200],
            [0, 200, 510, 200],
            [510, 200, 510, 200],
            [0, 400, 340, 200],
            [340, 400, 340, 200],
            [680, 400, 340, 200],
        ]
        UIHomeScreen.setObjectName("UIHomeScreen")
        UIHomeScreen.resize(1020, 600)

        # Set data to every channel of pill
        for index in range(7) :
            pill_channel_btn = QtWidgets.QPushButton(
                UIHomeScreen, 
            )   

            pill_channel_btn.clicked.connect(partial(self.gotoPillDetailScreen, index, pill_channel_datas[str(index)]))

            pill_channel_btn.setGeometry(QtCore.QRect(
                width_height_of_channel[index][0], 
                width_height_of_channel[index][1], 
                width_height_of_channel[index][2], 
                width_height_of_channel[index][3]
                )
            )

            # If have data in that slot
            if len(self.pill_channel_datas[str(index)]) != 0 :
                font = QtGui.QFont()
                font.setPointSize(18)
                pill_channel_btn.setFont(font)

                channel_text = "ช่องที่ " + str(index + 1) + " \n" + self.pill_channel_datas[str(index)]["name"]
                pill_channel_btn.setText(channel_text)
                pill_channel_btn.setStyleSheet("background-color : #F8F37D")
            else :
                # If don't have data in that slot
                pill_channel_btn.setStyleSheet("background-color : #97C7F9 ")
                pill_channel_btn.setIcon(QtGui.QIcon('shared\images\plus_icon.png'))
                pill_channel_btn.setIconSize(QtCore.QSize(60, 60))

            pill_channel_buttons.append(pill_channel_btn)

        if self.config["isFirstUse"] :
            self.frame = QtWidgets.QFrame(UIHomeScreen)
            self.frame.setGeometry(QtCore.QRect(30, 20, 961, 551))
            self.frame.setStyleSheet("background-color: white; border-radius: 20px")
            self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
            self.frame.setObjectName("frame")

            self.frame_2 = QtWidgets.QFrame(UIHomeScreen)
            self.frame_2.setGeometry(QtCore.QRect(0, 0, 1020, 600))
            self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
            self.frame_2.setObjectName("frame_2")

            self.label = QtWidgets.QLabel(self.frame_2)
            self.label.setGeometry(QtCore.QRect(80, 240, 321, 81))
            font = QtGui.QFont()
            font.setPointSize(26)
            self.label.setFont(font)
            self.label.setObjectName("label")
            self.label.setText("1. กดไปที่ช่องที่ 1")

            for i in range(6, 0, -1) :
                pill_channel_buttons[i].raise_()

            self.frame.raise_()
            self.frame_2.raise_()
            pill_channel_buttons[0].raise_()

        self.checkTakePillThread(pill_channel_buttons, pill_channel_datas)

    def gotoPillDetailScreen(self, channelID, pill_channel_data):
        global isChangePage
        isChangePage = True
        stopSound()

        if len(pill_channel_data) != 0 :
            pillThatHaveToTakeFlag = 0
            takeEveryPillFlag = 0

            for index, item in enumerate(__main__.haveToTake) :
                if item["id"] == channelID :
                    pillThatHaveToTakeFlag = 1
                    __main__.haveToTake[index]["isTaken"] = True

                if item["isTaken"] == False :
                    takeEveryPillFlag = 1

            if pillThatHaveToTakeFlag == 1 or takeEveryPillFlag == 0:
                # Change screen to pill detail screen
                detailScreen = DetailScreen(pill_channel_data)
                __main__.widget.addWidget(detailScreen)
                __main__.widget.setCurrentIndex(__main__.widget.currentIndex() + 1)
        else :
            flag = 0
            for item in __main__.haveToTake :
                if item["isTaken"] == False :
                    flag = 1
            
            if flag == 0:
                pillData = {
                    "id" : channelID,
                    "name": "",
                    "totalPills": -1,
                    "pillsPerTime": -1,
                    "timeToTake": []
                }
                voiceInputScreen = InputPillNameScreen(pillData)
                __main__.widget.addWidget(voiceInputScreen)
                __main__.widget.setCurrentIndex(__main__.widget.currentIndex() + 1)



    def checkTakePill(self, n, pill_channel_buttons, pill_channel_datas) :
        for index in range(7) :
            pill_channel_btn = pill_channel_buttons[index]
            pill_channel_data = pill_channel_datas[str(index)]

            # If have data in that slot
            if len(pill_channel_data) != 0 :
                for time in pill_channel_data['timeToTake'] :
                    now = datetime.now()

                    if time.split(":")[0] == "00" :
                        now += timedelta(days=1)

                    nowDate = now.strftime("%Y-%m-%d")
                    takePillDateTime = nowDate + " " + time
                    timeObject = datetime.strptime(takePillDateTime, '%Y-%m-%d %H:%M')
                    stringCompareTime = str(timeObject - now)

                    # if time to take is not already past
                    if not stringCompareTime.startswith('-1') :
                        willTakeMinute = int(stringCompareTime.split(':')[1])
                        willTakeHour = int(stringCompareTime.split(':')[0])

                        # if time to take is in 10 minute or less that 10 minute
                        if willTakeMinute <= 10 and willTakeMinute >= 0 and willTakeHour == 0 :
                            alreadyTakeFlag = False
                            haveItemFlag = False
                            for item in __main__.haveToTake :
                                if item["id"] == index:
                                    haveItemFlag = True
                                if item["id"] == index and item["isTaken"] :
                                    alreadyTakeFlag = True
                            
                            # If not have item in haveToTake list
                            if not haveItemFlag :
                                takeTimeData = {
                                    "id": index,
                                    "time": time,
                                    "isTaken": False
                                }
                                __main__.haveToTake.append(takeTimeData)

                            # If user are not already take that pill
                            # ถ้ายังไม่ได้หยิบยา
                            if not alreadyTakeFlag :
                                global isSoundOn
                                if not isSoundOn :
                                    playSound()
                                    isSoundOn = True

                                pill_channel_btn.setStyleSheet("background-color : #F8F37D")
                                channel_text = "ช่องที่ " + str(index + 1) + " \n" + pill_channel_data["name"] + " \n" + str(pill_channel_data["pillsPerTime"]) + " เม็ด"
                                pill_channel_btn.setText(channel_text)
                            else :
                                pill_channel_btn.setStyleSheet("background-color : #FBFADD")
                                pill_channel_btn.setText("")
                                stopSound()
                        else :
                            haveItemFlag = False
                            for item in __main__.haveToTake :
                                if item["id"] == index:
                                    haveItemFlag = True
                            if not haveItemFlag :
                                pill_channel_btn.setStyleSheet("background-color : #FBFADD")
                                pill_channel_btn.setText("")
                    else :
                        # check that it have item in haveToTake pill list that not taken
                        flag = 0
                        for item in __main__.haveToTake :
                            if item["id"] == index and not item["isTaken"]:
                                flag = 1

                        if flag == 1 :
                            for item in __main__.haveToTake :
                                if item["id"] == index :
                                    __main__.haveToTake.remove(item)

                        data = {
                            "id": index,
                            "time": time,
                            "isTaken": True
                        }

                        # If time to take is already pass and you already take pill remove that data from haveToTake list
                        if data in __main__.haveToTake:
                            __main__.haveToTake.remove(data)


                        pill_channel_btn.setStyleSheet("background-color : #FBFADD")
                        pill_channel_btn.setText("")

        flag = 0
        for item in __main__.haveToTake :
            if item["isTaken"] == False:
                flag = 1

        if len(__main__.haveToTake) != 0 and flag == 1 :
            for index in range(7) :
                pill_channel_btn = pill_channel_buttons[index]
                pill_channel_data = pill_channel_datas[str(index)]

                # If have data in that slot
                if len(pill_channel_data) == 0 :
                    pill_channel_btn.setStyleSheet("background-color : #FBFADD")
                    pill_channel_btn.setIcon(QtGui.QIcon())
        else :
            # Set data to every channel of pill
            for index in range(7) :
                pill_channel_btn = pill_channel_buttons[index]
                pill_channel_data = pill_channel_datas[str(index)] 

                # If have data in that slot
                if len(self.pill_channel_datas[str(index)]) != 0 :
                    font = QtGui.QFont()
                    font.setPointSize(18)
                    pill_channel_btn.setFont(font)

                    channel_text = "ช่องที่ " + str(index + 1) + " \n" + self.pill_channel_datas[str(index)]["name"]
                    pill_channel_btn.setText(channel_text)
                    pill_channel_btn.setStyleSheet("background-color : #F8F37D")
                else :
                    # If don't have data in that slot
                    pill_channel_btn.setStyleSheet("background-color : #97C7F9")
                    pill_channel_btn.setIcon(QtGui.QIcon('shared\images\plus_icon.png'))
                    pill_channel_btn.setIconSize(QtCore.QSize(60, 60))

    def checkTakePillThread(self, pill_channel_buttons, pill_channel_datas):
        # Step 2: Create a QThread object
        self.thread = QThread()
        # Step 3: Create a worker object
        self.worker = Worker()
        # Step 4: Move worker to the thread
        self.worker.moveToThread(self.thread)
        # Step 5: Connect signals and slots
        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        self.worker.progress.connect(lambda n : self.checkTakePill(n, pill_channel_buttons, pill_channel_datas))
        # Step 6: Start the thread
        self.thread.start()
        # )
isFirstLoop = True

class Worker(QObject):
    finished = pyqtSignal()
    progress = pyqtSignal(int)

    def run(self):
        global isFirstLoop
        num = 0
        while True :
            if not isFirstLoop:
                sleep(1)
            isFirstLoop = False
            if isChangePage : break
            self.progress.emit(num + 1)
            num += 1
        self.finished.emit()
    