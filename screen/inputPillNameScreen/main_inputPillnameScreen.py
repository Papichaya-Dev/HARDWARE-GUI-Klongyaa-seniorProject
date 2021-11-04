import sys,os
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QLabel
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QMovie
from gen.gen_input_voice_screen import *
from gen.gen_voice_loading_screen import *
from gen.gen_confirm_pill_name_screen import *
from gen.gen_input_voice_screen_again import *

class InputPillNameScreen(QDialog):
    def __init__(self):
        super().__init__()
        self.mockPillName = "ยาพาราแซลมอน"
        self.setupUi(self)
        
    def clickVoiceButton(self):
        loading_screen = LoadingVoiceScreen()
        widget.addWidget(loading_screen)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
    def setupUi(self, background_input_pil_name):
        background_input_pil_name.setObjectName("background_input_pil_name")
        background_input_pil_name.resize(1020, 600)
        background_input_pil_name.setStyleSheet("QWidget#background_input_pil_name{\n"
"background-color: #97C7F9}")
        self.no_channel = QtWidgets.QLabel(background_input_pil_name)
        self.no_channel.setGeometry(QtCore.QRect(40, 30, 191, 71))
        font = QtGui.QFont()
        font.setFamily("JasmineUPC")
        font.setPointSize(36)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.no_channel.setFont(font)
        self.no_channel.setStyleSheet("background-color: #C5E1FF;\n"
"font: 75 36pt \"JasmineUPC\";\n"
"border-radius: 25px;\n"
"color: #070021;\n"
"")
        self.no_channel.setAlignment(QtCore.Qt.AlignCenter)
        self.no_channel.setObjectName("no_channel")
        self.question_input_voice = QtWidgets.QLabel(background_input_pil_name)
        self.question_input_voice.setGeometry(QtCore.QRect(230, 150, 541, 201))
        self.question_input_voice.setStyleSheet("font: 34pt \"JasmineUPC\";")
        self.question_input_voice.setAlignment(QtCore.Qt.AlignCenter)
        self.question_input_voice.setObjectName("question_input_voice")
        self.button_input_voice = QtWidgets.QToolButton(background_input_pil_name)
        self.button_input_voice.setGeometry(QtCore.QRect(430, 350, 141, 125))
        self.button_input_voice.setStyleSheet("QToolButton#button_input_voice {\n"
"   background-image: url(:/newPrefix/mic_icon.png); \n"
"   border-radius: 35;\n"
"   width:30px;\n"
"}\n"
"QToolButton#button_input_voice:hover {\n"
"    background-color:#24BD73;\n"
"    background-image: url(:/newPrefix/mic_icon.png);\n"
"   border-radius: 35;\n"
"   background-color:#B9D974;\n"
"    width: 170px;\n"
"    height: 100px;\n"
"}")
        self.button_input_voice.setText("")
        self.button_input_voice.setObjectName("button_input_voice")
        self.button_input_voice.clicked.connect(self.clickVoiceButton)

        self.retranslateUi(background_input_pil_name)
        QtCore.QMetaObject.connectSlotsByName(background_input_pil_name)

    def retranslateUi(self, background_input_pil_name):
        _translate = QtCore.QCoreApplication.translate
        background_input_pil_name.setWindowTitle(_translate("background_input_pil_name", "Dialog"))
        self.no_channel.setText(_translate("background_input_pil_name", "ช่องที่ 1"))
        self.question_input_voice.setText(_translate("background_input_pil_name", "ดำเนินการกดปุ่ม \n"
" เพื่อพูดชื่อยาของท่าน"))

import gen.mic_icon

class LoadingVoiceScreen(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_voice_loading()
        self.ui.setupUi(self)

        #================ set voice loading gif ====================#
        self.movie = QMovie('screen\inputPillNameScreen\sound.gif')
        self.ui.label_voice_gif.setMovie(self.movie)
        #================ set delay 2 second ====================#
        timer = QTimer(self)
        self.startAnimation()
        timer.singleShot(2000, self.stopAnimation)
        self.show()

    def startAnimation(self):
        self.movie.start()

    def stopAnimation(self):
        self.movie.stop()
        self.close()
        #================ go to pill name screen ====================#
        confirm_pill_name_screen = ConfirmPillNameScreen()
        widget.addWidget(confirm_pill_name_screen)
        widget.setCurrentIndex(widget.currentIndex()+1)

class ConfirmPillNameScreen(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_confirm_pill_name()
        self.ui.setupUi(self)
        #================ click button correct or incorrect ====================#
        self.ui.button_correct_pill_name.clicked.connect(self.clickCorrectButton)
        self.ui.button_incorrect_pill_name.clicked.connect(self.clickIncorrectButton)

    def clickCorrectButton(self):
        print("ไปหน้าใส่เม็ดยาทั้งหมด")

    def clickIncorrectButton(self):
        print("ไปหน้าใส่ชื่อยาอีกครั้ง")
        input_voice_again = InputVoiceAgain()
        widget.addWidget(input_voice_again)
        widget.setCurrentIndex(widget.currentIndex()+1)

class InputVoiceAgain(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_input_voice_again()
        self.ui.setupUi(self)
        self.ui.button_input_voice_again.clicked.connect(self.clickVoiceButtonAgain)

    def clickVoiceButtonAgain(self):
        loading_screen = LoadingVoiceScreen()
        widget.addWidget(loading_screen)
        widget.setCurrentIndex(widget.currentIndex()+1)

if __name__ == "__main__":
     app = QApplication(sys.argv)
     screen = InputPillNameScreen()
     widget = QtWidgets.QStackedWidget()
     widget.setWindowTitle("GUI - KLONG_YAA")
     widget.addWidget(screen)
     widget.setFixedWidth(1024)
     widget.setFixedHeight(600)
     widget.show()
     sys.exit(app.exec_())	
try:
    sys.exit(app.exec_())
except:
    print("Exiting")
