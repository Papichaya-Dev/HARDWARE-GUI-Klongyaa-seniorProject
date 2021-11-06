import sys
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QLabel
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QMovie
from screen.inputPillNameScreen.gen.gen_input_voice_screen import *
from screen.inputPillNameScreen.gen.gen_voice_loading_screen import *
from screen.inputPillNameScreen.gen.gen_confirm_pill_name_screen import *
from screen.inputPillNameScreen.gen.gen_input_voice_screen_again import *
from screen.totalPillsNPillPerTimeScreen.main_totalPillsNPertimeScreen import *
import __main__

globalInputPillName = ""
mockNum = 0
globalPillData = {}

class InputPillNameScreen(QDialog):
    def __init__(self, pillData):
        super().__init__()
        global globalPillData
        globalPillData = pillData
        print("xxxxxx")
        print(pillData)
        print(globalPillData)
        self.setupUi(self)
    #========================= 
    def clickVoiceButton(self):
        loading_screen = LoadingVoiceScreen()
        # __main__.widget.removeWidget(self)
        __main__.widget.addWidget(loading_screen)
        __main__.widget.setCurrentIndex(__main__.widget.currentIndex()+1)
    
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

        global globalPillData
        print("yyyyyyyyy")
        print(globalPillData["id"])
        channelID = "ช่องที่ " + str(globalPillData["id"] + 1)
        background_input_pil_name.setWindowTitle(_translate("background_input_pil_name", "Dialog"))
        self.no_channel.setText(_translate("background_input_pil_name", channelID))
        self.question_input_voice.setText(_translate("background_input_pil_name", "ดำเนินการกดปุ่ม \n"
" เพื่อพูดชื่อยาของท่าน"))

import screen.inputPillNameScreen.gen.mic_icon

class LoadingVoiceScreen(QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def setupUi(self, background_voice_loading):
        background_voice_loading.setObjectName("background_voice_loading")
        background_voice_loading.resize(1020, 600)
        background_voice_loading.setStyleSheet("QWidget#background_voice_loading{\n"
    "background-color: #97C7F9}")
        self.frame_of_loading = QtWidgets.QFrame(background_voice_loading)
        self.frame_of_loading.setGeometry(QtCore.QRect(40, 38, 941, 521))
        self.frame_of_loading.setStyleSheet("background-color: rgb(255, 255, 255);\n"
    "border-radius:40px")
        self.frame_of_loading.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_of_loading.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_of_loading.setObjectName("frame_of_loading")
        self.label_voice_gif = QtWidgets.QLabel(self.frame_of_loading)
        self.label_voice_gif.setGeometry(QtCore.QRect(170, 100, 601, 231))
        self.label_voice_gif.setStyleSheet("background-color: #ffffff;\n"
    "font: 75 36pt \"JasmineUPC\";")
        self.label_voice_gif.setAlignment(QtCore.Qt.AlignCenter)
        self.label_voice_gif.setObjectName("label_voice_gif")
        self.text_of_waiting_process = QtWidgets.QLabel(self.frame_of_loading)
        self.text_of_waiting_process.setGeometry(QtCore.QRect(170, 360, 651, 61))
        self.text_of_waiting_process.setStyleSheet("font: 34pt \"JasmineUPC\";")
        self.text_of_waiting_process.setObjectName("text_of_waiting_process")

        self.retranslateUi(background_voice_loading)
        QtCore.QMetaObject.connectSlotsByName(background_voice_loading)

    def retranslateUi(self, background_voice_loading):
        _translate = QtCore.QCoreApplication.translate
        background_voice_loading.setWindowTitle(_translate("background_voice_loading", "Dialog"))
        self.label_voice_gif.setText(_translate("background_voice_loading", "sound loading gif"))
        self.text_of_waiting_process.setText(_translate("background_voice_loading", "ระบบกำลังประมวลผล โปรดรอสักครู่"))

        #================ set voice loading gif ====================#
        self.movie = QMovie('shared/images/sound.gif')
        self.label_voice_gif.setMovie(self.movie)
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
        global globalInputPillName
        global mockNum
        mockNum = mockNum + 1
        globalInputPillName = "พาราเซตาม่อน " + str(mockNum)

        confirm_pill_name_screen = ConfirmPillNameScreen(globalInputPillName)
        # __main__.widget.removeWidget(self)
        __main__.widget.addWidget(confirm_pill_name_screen)
        __main__.widget.setCurrentIndex(__main__.widget.currentIndex()+1)

class ConfirmPillNameScreen(QDialog):
    def __init__(self, inputPillName):
        super().__init__()
        self.inputPillName = inputPillName
        self.setupUi(self)
        #================ click button correct or incorrect ====================#
        self.button_correct_pill_name.clicked.connect(self.clickCorrectButton)
        self.button_incorrect_pill_name.clicked.connect(self.clickIncorrectButton)

    def setupUi(self, background_confirm_pill_name):
        background_confirm_pill_name.setObjectName("background_confirm_pill_name")
        background_confirm_pill_name.resize(1024, 600)
        background_confirm_pill_name.setStyleSheet("QWidget#background_confirm_pill_name{\n"
"background-color: #97C7F9}")
        self.no_channel = QtWidgets.QLabel(background_confirm_pill_name)
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
        self.label_1 = QtWidgets.QLabel(background_confirm_pill_name)
        self.label_1.setGeometry(QtCore.QRect(410, 130, 171, 81))
        self.label_1.setStyleSheet("font:42pt \"JasmineUPC\";")
        self.label_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_1.setObjectName("label_1")
        self.show_pill_name = QtWidgets.QLabel(background_confirm_pill_name)
        self.show_pill_name.setGeometry(QtCore.QRect(220, 230, 561, 81))
        self.show_pill_name.setStyleSheet("font: 52pt \"JasmineUPC\";")
        self.show_pill_name.setAlignment(QtCore.Qt.AlignCenter)
        self.show_pill_name.setObjectName("show_pill_name")
        self.button_correct_pill_name = QtWidgets.QToolButton(background_confirm_pill_name)
        self.button_correct_pill_name.setGeometry(QtCore.QRect(220, 410, 251, 91))
        self.button_correct_pill_name.setStyleSheet("\n"
"\n"
"QToolButton#button_correct_pill_name {\n"
"       font: 75 36pt \"JasmineUPC\";\n"
"   background-color:#24BD73;\n"
"   color: #ffffff;\n"
"   border-radius:20px;\n"
"}\n"
"QToolButton#button_correct_pill_name:hover {\n"
"    font: 75 36pt \"JasmineUPC\";\n"
"    background-color:#23B36D;\n"
"    color: #ffffff;\n"
"    border-radius:20px;\n"
"    width: 170px;\n"
"    height:100px;\n"
"}")
        self.button_correct_pill_name.setObjectName("button_correct_pill_name")
        self.button_incorrect_pill_name = QtWidgets.QToolButton(background_confirm_pill_name)
        self.button_incorrect_pill_name.setGeometry(QtCore.QRect(560, 410, 251, 91))
        self.button_incorrect_pill_name.setStyleSheet("QToolButton#button_incorrect_pill_name {\n"
"       font: 75 36pt \"JasmineUPC\";\n"
"    background-color: #DD5D5D;\n"
"      border-radius:20px;\n"
"    color: white;\n"
"}\n"
"QToolButton#button_incorrect_pill_name:hover {\n"
"       font: 75 36pt \"JasmineUPC\";\n"
"    background-color: rgb(255, 50, 50);\n"
"      border-radius:20px;\n"
"    color: white;\n"
"}")
        self.button_incorrect_pill_name.setObjectName("button_incorrect_pill_name")

        self.retranslateUi(background_confirm_pill_name)
        QtCore.QMetaObject.connectSlotsByName(background_confirm_pill_name)

    def retranslateUi(self, background_confirm_pill_name):
        _translate = QtCore.QCoreApplication.translate

        global globalPillData
        channelID = "ช่องที่ " + str(globalPillData["id"] + 1)

        background_confirm_pill_name.setWindowTitle(_translate("background_confirm_pill_name", "Dialog"))
        self.no_channel.setText(_translate("background_confirm_pill_name", channelID))
        self.label_1.setText(_translate("background_confirm_pill_name", "ชื่อยา"))
        self.show_pill_name.setText(_translate("background_confirm_pill_name", self.inputPillName))
        self.button_correct_pill_name.setText(_translate("background_confirm_pill_name", "ถูกต้อง"))
        self.button_incorrect_pill_name.setText(_translate("background_confirm_pill_name", "ไม่ถูกต้อง"))

    def clickCorrectButton(self):
        print("ไปหน้าใส่เม็ดยาทั้งหมด")

        global globalPillData
        globalPillData["name"] = globalInputPillName
        print(globalPillData)

        total_pill_screen = TotalPillsScreen(globalPillData)
        # __main__.widget.removeWidget(self)
        __main__.widget.addWidget(total_pill_screen)
        __main__.widget.setCurrentIndex(__main__.widget.currentIndex()+1)

    def clickIncorrectButton(self):
        print("ไปหน้าใส่ชื่อยาอีกครั้ง")
        input_voice_again = InputVoiceAgain()
        # __main__.widget.removeWidget(self)
        __main__.widget.addWidget(input_voice_again)
        __main__.widget.setCurrentIndex(__main__.widget.currentIndex()+1)

class InputVoiceAgain(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_input_voice_again()
        self.ui.setupUi(self)
        self.ui.button_input_voice_again.clicked.connect(self.clickVoiceButtonAgain)

    def setupUi(self, bankground_input_voice_again):
        bankground_input_voice_again.setObjectName("bankground_input_voice_again")
        bankground_input_voice_again.resize(1024, 600)
        bankground_input_voice_again.setStyleSheet("QWidget#bankground_input_voice_again{\n"
"background-color: #97C7F9}")
        self.frame_of_input_voice_again = QtWidgets.QFrame(bankground_input_voice_again)
        self.frame_of_input_voice_again.setGeometry(QtCore.QRect(40, 40, 941, 521))
        self.frame_of_input_voice_again.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:40px")
        self.frame_of_input_voice_again.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_of_input_voice_again.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_of_input_voice_again.setObjectName("frame_of_input_voice_again")
        self.question_of_input_voice_again = QtWidgets.QLabel(self.frame_of_input_voice_again)
        self.question_of_input_voice_again.setGeometry(QtCore.QRect(140, 170, 651, 61))
        self.question_of_input_voice_again.setStyleSheet("font: 34pt \"JasmineUPC\";")
        self.question_of_input_voice_again.setAlignment(QtCore.Qt.AlignCenter)
        self.question_of_input_voice_again.setObjectName("question_of_input_voice_again")
        self.button_input_voice_again = QtWidgets.QToolButton(self.frame_of_input_voice_again)
        self.button_input_voice_again.setGeometry(QtCore.QRect(400, 280, 141, 125))
        self.button_input_voice_again.setStyleSheet("QToolButton#button_input_voice_again {\n"
"   background-image: url(:/newPrefix/mic_icon.png); \n"
"   border-radius: 35;\n"
"   width:30px;\n"
"}\n"
"QToolButton#button_input_voice_again:hover {\n"
"    background-color:#24BD73;\n"
"    background-image: url(:/newPrefix/mic_icon.png);\n"
"   border-radius: 35;\n"
"   background-color:#B9D974;\n"
"    width: 170px;\n"
"    height: 100px;\n"
"}")
        self.button_input_voice_again.setText("")
        self.button_input_voice_again.setObjectName("button_input_voice_again")

        self.retranslateUi(bankground_input_voice_again)
        QtCore.QMetaObject.connectSlotsByName(bankground_input_voice_again)

    def retranslateUi(self, bankground_input_voice_again):
        _translate = QtCore.QCoreApplication.translate
        bankground_input_voice_again.setWindowTitle(_translate("bankground_input_voice_again", "Dialog"))
        self.question_of_input_voice_again.setText(_translate("bankground_input_voice_again", "กรุณาพูดชื่อยาอีกครั้ง"))

    import screen.inputPillNameScreen.gen.mic_icon

    def clickVoiceButtonAgain(self):
        loading_screen = LoadingVoiceScreen()
        # __main__.widget.removeWidget(self)
        __main__.widget.addWidget(loading_screen)
        __main__.widget.setCurrentIndex(__main__.widget.currentIndex()+1)

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
