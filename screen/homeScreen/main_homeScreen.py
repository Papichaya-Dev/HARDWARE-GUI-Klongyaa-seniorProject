from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog
import __main__
from screen.inputPillNameScreen.main_inputPillnameScreen import InputPillNameScreen
from screen.pillDetailScreen.main_detail_screen import DetailScreen
from functools import partial

class HomeScreen(QDialog):
    def __init__(self, pill_channel_datas, config):
        super().__init__()
        self.pill_channel_datas = pill_channel_datas
        self.config = config
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
                clicked = partial(gotoPillDetailScreen, index, pill_channel_datas[str(index)])
            )   

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
        print(self.config["isFirstUse"] )
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

        self.retranslateUi(UIHomeScreen)
        QtCore.QMetaObject.connectSlotsByName(UIHomeScreen)

    def retranslateUi(self, UIHomeScreen):
        _translate = QtCore.QCoreApplication.translate
        UIHomeScreen.setWindowTitle(_translate("UIHomeScreen", "Dialog"))

def gotoPillDetailScreen(channelID, pill_channel_data):
    if len(pill_channel_data) != 0 :
        # Change screen to pill detail screen
        detailScreen = DetailScreen(pill_channel_data)
        __main__.widget.addWidget(detailScreen)
        __main__.widget.setCurrentIndex(__main__.widget.currentIndex() + 1)
    else :
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
    