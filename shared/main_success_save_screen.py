import sys
from PyQt5.QtWidgets import QDialog, QApplication, QWidget 
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import Qt, QTimer
from PyQt5 import QtCore, QtGui, QtWidgets 
# from screen.homeScreen.main_homeScreen import HomeScreen
import __main__
import shared.images.success_icon

class SuccessSaveScreen(QDialog):
    def __init__(self, pillData):
        super().__init__()
        self.pillData = pillData
        self.setupUi(self)

        self.timer = QTimer()
        self.timer.timeout.connect(self.stopDelay)
        self.timer.start(1000)


    def stopDelay(self):
        self.timer.stop()
        channelID = self.pillData["id"]
        allPillDatas = __main__.pill_channel_datas
        allPillDatas[str(channelID)] = self.pillData
        __main__.widget.removeWidget(self)
        __main__.widget.addWidget(__main__.HomeScreen(allPillDatas))
        __main__.widget.setCurrentIndex(__main__.widget.currentIndex()+1)

    def setupUi(self, background_success_save_screen):
        background_success_save_screen.setObjectName("background_success_save_screen")
        background_success_save_screen.resize(1024, 600)
        background_success_save_screen.setStyleSheet("QWidget#background_success_save_screen{\n"
"background-color: #97C7F9}")
        self.frame_of_loading = QtWidgets.QFrame(background_success_save_screen)
        self.frame_of_loading.setGeometry(QtCore.QRect(40, 38, 941, 521))
        self.frame_of_loading.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:40px")
        self.frame_of_loading.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_of_loading.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_of_loading.setObjectName("frame_of_loading")
        self.label = QtWidgets.QLabel(self.frame_of_loading)
        self.label.setGeometry(QtCore.QRect(290, 40, 361, 331))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/newPrefix/success_icon.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame_of_loading)
        self.label_2.setGeometry(QtCore.QRect(200, 370, 541, 101))
        self.label_2.setStyleSheet("font: 38pt \"JasmineUPC\";")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(background_success_save_screen)
        QtCore.QMetaObject.connectSlotsByName(background_success_save_screen)

    def retranslateUi(self, background_success_save_screen):
        _translate = QtCore.QCoreApplication.translate
        background_success_save_screen.setWindowTitle(_translate("background_success_save_screen", "Dialog"))
        self.label_2.setText(_translate("background_success_save_screen", "บันทึกข้อมูลสำเร็จ"))
