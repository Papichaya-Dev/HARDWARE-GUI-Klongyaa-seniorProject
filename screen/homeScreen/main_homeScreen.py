from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog
import __main__
from screen.inputPillNameScreen.main_inputPillnameScreen import InputPillNameScreen
from screen.pillDetailScreen.main_detail_screen import DetailScreen

class HomeScreen(QDialog):
    def __init__(self, pill_channel_datas):
        super().__init__()
        self.pill_channel_datas = pill_channel_datas
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

        self.pill_channel_btn_0 = QtWidgets.QPushButton(
            UIHomeScreen, 
            clicked = lambda: gotoPillDetailScreen(
                0,
                pill_channel_datas["0"]
                )
            )   
        pill_channel_buttons.append(self.pill_channel_btn_0)
        
        self.pill_channel_btn_1 = QtWidgets.QPushButton(
            UIHomeScreen, 
            clicked = lambda: gotoPillDetailScreen(
                1,
                pill_channel_datas["1"]
                )
            )   
        pill_channel_buttons.append(self.pill_channel_btn_1)
        
        self.pill_channel_btn_2 = QtWidgets.QPushButton(
            UIHomeScreen, 
            clicked = lambda: gotoPillDetailScreen(
                2,
                pill_channel_datas["2"]
                )
            )   
        pill_channel_buttons.append(self.pill_channel_btn_2)
        
        self.pill_channel_btn_3 = QtWidgets.QPushButton(
            UIHomeScreen, 
            clicked = lambda: gotoPillDetailScreen(
                3,
                pill_channel_datas["3"]
                )
            )   
        pill_channel_buttons.append(self.pill_channel_btn_3)
        
        self.pill_channel_btn_4 = QtWidgets.QPushButton(
            UIHomeScreen, 
            clicked = lambda: gotoPillDetailScreen(
                4,
                pill_channel_datas["4"]
                )
            )   
        pill_channel_buttons.append(self.pill_channel_btn_4)
        
        self.pill_channel_btn_5 = QtWidgets.QPushButton(
            UIHomeScreen, 
            clicked = lambda: gotoPillDetailScreen(
                5,
                pill_channel_datas["5"]
                )
            )   
        pill_channel_buttons.append(self.pill_channel_btn_5)
        
        self.pill_channel_btn_6 = QtWidgets.QPushButton(
            UIHomeScreen, 
            clicked = lambda: gotoPillDetailScreen(
                6,
                pill_channel_datas["6"]
                )
            )   
        pill_channel_buttons.append(self.pill_channel_btn_6)

        # Set data to every channel of pill
        for channel in pill_channel_buttons :
            channel_id = pill_channel_buttons.index(channel)
            channel.setGeometry(QtCore.QRect(
                width_height_of_channel[channel_id][0], 
                width_height_of_channel[channel_id][1], 
                width_height_of_channel[channel_id][2], 
                width_height_of_channel[channel_id][3]
                )
            )

            # If have data in that slot
            if len(self.pill_channel_datas[str(channel_id)]) != 0 :
                font = QtGui.QFont()
                font.setPointSize(18)
                channel.setFont(font)

                channel_text = "ช่องที่ " + str(channel_id + 1) + " \n" + self.pill_channel_datas[str(channel_id)]["name"]
                channel.setText(channel_text)
                channel.setStyleSheet("background-color : #F8F37D")
                flag = 1
                continue

            # If don't have data in that slot
            channel.setStyleSheet("background-color : #97C7F9")
            channel.setIcon(QtGui.QIcon('shared\images\plus_logo.png'))
            channel.setIconSize(QtCore.QSize(40, 40))

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
    