from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog


class HomeScreen(QDialog):
    def __init__(self, pill_channel_datas):
        super().__init__()
        self.pill_channel_data = pill_channel_datas
        self.setupUi(self)
    
    def setupUi(self, UIHomeScreen):
        pill_channel_buttons = []
        pill_channel_datas = self.pill_channel_data
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

        self.gridLayout = QtWidgets.QGridLayout(UIHomeScreen)
        self.gridLayout.setObjectName("gridLayout")

        self.stackedWidget = QtWidgets.QStackedWidget(UIHomeScreen)
        self.stackedWidget.setObjectName("stackedWidget")

        self.homescreen = QtWidgets.QWidget()
        self.homescreen.setObjectName("homescreen")

        self.pill_channel_btn_0 = QtWidgets.QPushButton(
            self.homescreen, 
            clicked = lambda: gotoPillDetailScreen(
                self, 0, pill_channel_datas
                )
            )   
        pill_channel_buttons.append(self.pill_channel_btn_0)
        
        self.pill_channel_btn_1 = QtWidgets.QPushButton(
            self.homescreen, 
            clicked = lambda: gotoPillDetailScreen(
                self, 1, pill_channel_datas
                )
            )   
        pill_channel_buttons.append(self.pill_channel_btn_1)
        
        self.pill_channel_btn_2 = QtWidgets.QPushButton(
            self.homescreen, 
            clicked = lambda: gotoPillDetailScreen(
                self, 2, pill_channel_datas
                )
            )   
        pill_channel_buttons.append(self.pill_channel_btn_2)
        
        self.pill_channel_btn_3 = QtWidgets.QPushButton(
            self.homescreen, 
            clicked = lambda: gotoPillDetailScreen(
                self, 3, pill_channel_datas
                )
            )   
        pill_channel_buttons.append(self.pill_channel_btn_3)
        
        self.pill_channel_btn_4 = QtWidgets.QPushButton(
            self.homescreen, 
            clicked = lambda: gotoPillDetailScreen(
                self, 4, pill_channel_datas
                )
            )   
        pill_channel_buttons.append(self.pill_channel_btn_4)
        
        self.pill_channel_btn_5 = QtWidgets.QPushButton(
            self.homescreen, 
            clicked = lambda: gotoPillDetailScreen(
                self, 5, pill_channel_datas
                )
            )   
        pill_channel_buttons.append(self.pill_channel_btn_5)
        
        self.pill_channel_btn_6 = QtWidgets.QPushButton(
            self.homescreen, 
            clicked = lambda: gotoPillDetailScreen(
                self, 6, pill_channel_datas
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
            channel.setObjectName(f"pill_channel_btn_{channel_id}")

            flag = 0

            for data in pill_channel_datas :
                # If have data in that slot
                if channel_id == data["id"] :
                    font = QtGui.QFont()
                    font.setPointSize(18)
                    channel.setFont(font)

                    channel_text = "ช่องที่ " + str(channel_id + 1) + " \n" + data["name"]
                    channel.setText(channel_text)
                    channel.setStyleSheet("background-color : #F8F37D")
                    flag = 1
                    break

            # If don't have data in that slot
            if flag == 0 :
                channel.setStyleSheet("background-color : #97C7F9")
                channel.setIcon(QtGui.QIcon('shared\images\plus_logo.png'))
                channel.setIconSize(QtCore.QSize(40, 40))

        self.stackedWidget.addWidget(self.homescreen)

        # self.page_2 = QtWidgets.QWidget()
        # self.page_2.setObjectName("page_2")
        # self.stackedWidget.addWidget(self.page_2)

        self.gridLayout.addWidget(self.stackedWidget, 0, 0, 1, 1)

        self.retranslateUi(UIHomeScreen)
        QtCore.QMetaObject.connectSlotsByName(UIHomeScreen)

    def retranslateUi(self, UIHomeScreen):
        _translate = QtCore.QCoreApplication.translate
        UIHomeScreen.setWindowTitle(_translate("UIHomeScreen", "Dialog"))

def gotoPillDetailScreen(self, id, pill_channel_datas):
    print('homepage :')
    
    flag = 0
    for data in pill_channel_datas :
        if id == data["id"] :
            flag = 1
            break
    if flag == 1 :
        print("test")
        # self.stackedWidget.setCurrentWidget(self.pill_detail_screen)
    else :
        print("Add pill")
    