import sys
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QLabel
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QMovie
from PyQt5 import QtCore, QtGui, QtWidgets 
from screen.inputPillNameScreen.gen.gen_input_voice_screen import *
from screen.inputPillNameScreen.gen.gen_voice_loading_screen import *
from screen.inputPillNameScreen.gen.gen_input_voice_screen_again import *
from screen.pillSummaryScreen.main_pillSummaryScreen import PillSummaryScreen
import __main__

timesToTakePillArr = []
mockTime = 12

class InputTimeToTakePillScreen(QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
    #======================= set max-min of total pills =======================#
        self.button_input_times_to_take_pill.clicked.connect(self.voice_button_input_clicked)

    def setupUi(self, background_input_times_to_take_pill):
        background_input_times_to_take_pill.setObjectName("background_input_times_to_take_pill")
        background_input_times_to_take_pill.resize(1020, 600)
        background_input_times_to_take_pill.setStyleSheet("QWidget#background_input_times_to_take_pill{\n""background-color: #97C7F9}")
        self.no_channel = QtWidgets.QLabel(background_input_times_to_take_pill)
        self.no_channel.setGeometry(QtCore.QRect(40, 30, 191, 71))
        font = QtGui.QFont()
        font.setFamily("JasmineUPC")
        font.setPointSize(36)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.no_channel.setFont(font)
        self.no_channel.setStyleSheet("background-color: #C5E1FF;\n""font: 75 36pt \"JasmineUPC\";\n""border-radius: 25px;\n""color: #070021;\n""")
        self.no_channel.setAlignment(QtCore.Qt.AlignCenter)
        self.no_channel.setObjectName("no_channel")
        self.question_input_times_to_take_pill = QtWidgets.QLabel(background_input_times_to_take_pill)
        self.question_input_times_to_take_pill.setGeometry(QtCore.QRect(190, 150, 621, 201))
        self.question_input_times_to_take_pill.setStyleSheet("font: 34pt \"JasmineUPC\";")
        self.question_input_times_to_take_pill.setAlignment(QtCore.Qt.AlignCenter)
        self.question_input_times_to_take_pill.setObjectName("question_input_times_to_take_pill")
        self.button_input_times_to_take_pill = QtWidgets.QToolButton(background_input_times_to_take_pill)
        self.button_input_times_to_take_pill.setGeometry(QtCore.QRect(430, 350, 141, 125))
        self.button_input_times_to_take_pill.setStyleSheet("QToolButton#button_input_times_to_take_pill {\n""   background-image: url(:/newPrefix/mic_icon.png); \n""   border-radius: 35;\n""   width:30px;\n""}\n""QToolButton#button_input_times_to_take_pill:hover {\n""    background-color:#24BD73;\n""    background-image: url(:/newPrefix/mic_icon.png);\n""   border-radius: 35;\n""   background-color:#B9D974;\n""    width: 170px;\n""    height: 100px;\n""}")
        self.button_input_times_to_take_pill.setText("")
        self.button_input_times_to_take_pill.setObjectName("button_input_times_to_take_pill")

        self.retranslateUi(background_input_times_to_take_pill)
        QtCore.QMetaObject.connectSlotsByName(background_input_times_to_take_pill)

    def retranslateUi(self, background_input_times_to_take_pill):
        _translate = QtCore.QCoreApplication.translate
        background_input_times_to_take_pill.setWindowTitle(_translate("background_input_times_to_take_pill", "Dialog"))
        self.no_channel.setText(_translate("background_input_times_to_take_pill", "ช่องที่ 1"))
        self.question_input_times_to_take_pill.setText(_translate("background_input_times_to_take_pill", "ดำเนินการกดปุ่ม \n"" เพื่อพูดเวลาทานยาพาราเซตามอล"))

    import screen.inputPillNameScreen.gen.mic_icon

    #======================= define function : when user click voice button =======================#
    def voice_button_input_clicked(self):
        loading_screen = LoadingVoiceScreen()
        __main__.widget.addWidget(loading_screen)
        __main__.widget.setCurrentIndex(__main__.widget.currentIndex()+1)

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
        #================ go to add summary time screen ====================#
        global mockTime
        global timesToTakePillArr
        mockTime = mockTime + 1
        timesToTakePillArr.append(str(mockTime) + ".00")
        add_summary_time_screen = AddSummaryTimeScreen(timesToTakePillArr)
        __main__.widget.addWidget( add_summary_time_screen)
        __main__.widget.setCurrentIndex(__main__.widget.currentIndex()+1)


class AddSummaryTimeScreen(QDialog):
    def __init__(self, mockTimesArr):
        super().__init__()
        self.timesToTakesPillArr = mockTimesArr
        self.setupUi(self)
        #================ when click button ==========================#
        self.success_button.clicked.connect(self.goToPillSummaryScreen)


    def setupUi(self, background_confirm_times_to_take_pill):
        background_confirm_times_to_take_pill.setObjectName("background_confirm_times_to_take_pill")
        background_confirm_times_to_take_pill.resize(1024, 600)
        background_confirm_times_to_take_pill.setStyleSheet("QWidget#background_confirm_times_to_take_pill{\n""background-color: #97C7F9}")
        self.no_channel = QtWidgets.QLabel(background_confirm_times_to_take_pill)
        self.no_channel.setGeometry(QtCore.QRect(40, 30, 191, 71))
        font = QtGui.QFont()
        font.setFamily("JasmineUPC")
        font.setPointSize(36)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.no_channel.setFont(font)
        self.no_channel.setStyleSheet("background-color: #C5E1FF;\n""font: 75 36pt \"JasmineUPC\";\n""border-radius: 25px;\n""color: #070021;\n""")
        self.no_channel.setAlignment(QtCore.Qt.AlignCenter)
        self.no_channel.setObjectName("no_channel")
        self.header_text = QtWidgets.QLabel(background_confirm_times_to_take_pill)
        self.header_text.setGeometry(QtCore.QRect(350, 30, 331, 201))
        self.header_text.setStyleSheet("font: 34pt \"JasmineUPC\";")
        self.header_text.setAlignment(QtCore.Qt.AlignCenter)
        self.header_text.setObjectName("header_text")
        self.scrollArea = QtWidgets.QScrollArea(background_confirm_times_to_take_pill)
        self.scrollArea.setGeometry(QtCore.QRect(80, 180, 871, 271))
        self.scrollArea.setStyleSheet("background-color:rgb(156, 183, 255);\n""border-color:rgb(156, 183, 255);")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 869, 269))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName("gridLayout")
        

        for time in self.timesToTakesPillArr :
            objIndex = self.timesToTakesPillArr.index(time)
            timeToTakePillLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
            timeToTakePillLabel.setMinimumSize(QtCore.QSize(250, 0))
            timeToTakePillLabel.setMaximumSize(QtCore.QSize(250, 16777215))
            timeToTakePillLabel.setStyleSheet("background-color: none;\n""font: 75 30pt \"JasmineUPC\";\n""border-radius: 25px;\n""color: #070021;\n""background-color: #C5E1FF;")
            timeToTakePillLabel.setAlignment(QtCore.Qt.AlignCenter)
            timeToTakePillLabel.setText("เวลาที่ " + str(objIndex + 1))
            timeToTakePillLabel.setObjectName("question_time_no" + str(objIndex))
            self.gridLayout.addWidget(timeToTakePillLabel, 9+objIndex, 0, 1, 1)

            timeToTakePillData = QtWidgets.QLabel(self.scrollAreaWidgetContents)
            timeToTakePillData.setStyleSheet("font: 75 34pt \"JasmineUPC\";\n""color: #070021;\n""")
            timeToTakePillData.setText(time)
            timeToTakePillData.setObjectName("show_time_" + str(objIndex))
            self.gridLayout.addWidget(timeToTakePillData, 9+objIndex, 1, 1, 1)

            timeToTakePillEditButton = QtWidgets.QToolButton(self.scrollAreaWidgetContents)
            timeToTakePillEditButton.setMinimumSize(QtCore.QSize(70, 70))
            timeToTakePillEditButton.setStyleSheet("font-size: 40px; background-color: rgb(255, 74, 74); border-radius: 35px; color: white;")
            timeToTakePillEditButton.setObjectName("button_edit_time_" + str(objIndex))
            timeToTakePillEditButton.setText( "🖉")
            self.gridLayout.addWidget(timeToTakePillEditButton, 9+objIndex, 2, 1, 1)

            if objIndex + 1 == len(self.timesToTakesPillArr) :
                timeToTakePillAddButton = QtWidgets.QToolButton(self.scrollAreaWidgetContents)
                timeToTakePillAddButton.setMinimumSize(QtCore.QSize(70, 70))
                timeToTakePillAddButton.setStyleSheet("QToolButton#add_time_button {\n""   font-size: 40px;\n""    background-color:#24BD73;\n""  border-radius: 35px;\n""  color: white;\n""}\n""QToolButton#add_time_button {\n""    font-size: 40px;\n""    background-color:#24BD73;\n""  border-radius: 35px;\n""  color: white;\n""}")
                timeToTakePillAddButton.setText("+")
                timeToTakePillAddButton.clicked.connect(self.goToInputTimeToTakePillScreen)
                timeToTakePillAddButton.setObjectName("add_time_button")
                self.gridLayout.addWidget(timeToTakePillAddButton, 9+objIndex, 3, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.success_button = QtWidgets.QToolButton(background_confirm_times_to_take_pill)
        self.success_button.setGeometry(QtCore.QRect(400, 470, 231, 103))
        self.success_button.setMinimumSize(QtCore.QSize(100, 50))
        self.success_button.setStyleSheet("QToolButton#success_button {\n""       font: 75 36pt \"JasmineUPC\";\n""    background-color:#24BD73;\n""    color: #ffffff;\n""    border-radius:20px;\n""    width: 170px;\n""    height: 100px;\n""}\n""QToolButton#success_button:hover {\n""    font: 75 36pt \"JasmineUPC\";\n""    background-color:#23B36D;\n""    color: #ffffff;\n""    border-radius:20px;\n""    width: 170px;\n""    height:100px;\n""}")
        self.success_button.setObjectName("success_button")

        self.retranslateUi(background_confirm_times_to_take_pill)
        QtCore.QMetaObject.connectSlotsByName(background_confirm_times_to_take_pill)

    def retranslateUi(self, background_confirm_times_to_take_pill):
        _translate = QtCore.QCoreApplication.translate
        background_confirm_times_to_take_pill.setWindowTitle(_translate("background_confirm_times_to_take_pill", "Dialog"))
        self.no_channel.setText(_translate("background_confirm_times_to_take_pill", "ช่องที่ 1"))
        self.header_text.setText(_translate("background_confirm_times_to_take_pill", "เวลาที่ต้องทานยา"))
        self.success_button.setText(_translate("background_confirm_times_to_take_pill", "เสร็จสิ้น"))

    def goToInputTimeToTakePillScreen(self):
         #================ go to add summary time screen ====================#
        screen = InputTimeToTakePillScreen()
        __main__.widget.removeWidget(self)
        __main__.widget.addWidget(screen)
        __main__.widget.setCurrentIndex(__main__.widget.currentIndex()+1)

    def goToPillSummaryScreen(self):
         #================ go to add summary time screen ====================#
        add_summary_time_screen = PillSummaryScreen()
        __main__.widget.addWidget(add_summary_time_screen)
        __main__.widget.setCurrentIndex(__main__.widget.currentIndex()+1)