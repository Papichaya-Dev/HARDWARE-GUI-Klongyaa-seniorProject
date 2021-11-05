import sys
from  screen.totalPillsNPillPerTimeScreen.gen.gen_total_pills_screen import *
from screen.totalPillsNPillPerTimeScreen.gen.gen_amount_pill_per_time_screen import *
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QLabel
from screen.totalPillsNPillPerTimeScreen.shared.gen_mock_screen import *
from screen.inputTimesToTakePill.main_inputTimesToTakePill import *
import __main__

globalPillData = {}

class TotalPillsScreen(QDialog):
    def __init__(self, pillData):
        super().__init__()
        global globalPillData
        globalPillData = pillData
        self.setupUi(self)
        #======================= set max-min of total pills =======================#
        self.slider_total_pills.setMaximum(30)
        self.slider_total_pills.setMinimum(0)
        self.slider_total_pills.valueChanged.connect(self.updateSliderTotalPills)
        self.button_skip_total_pills.clicked.connect(lambda: self.goToAmountPillPerTimeScreen(True))
        self.button_save_total_pills.clicked.connect(lambda: self.goToAmountPillPerTimeScreen(False))
        
    def setupUi(self, background_total_pills):
        background_total_pills.setObjectName("background_total_pills")
        background_total_pills.resize(1024, 600)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        background_total_pills.setFont(font)
        background_total_pills.setStyleSheet("QWidget#background_total_pills{\n"
"background-color: #97C7F9}")
        self.no_channel = QtWidgets.QLabel(background_total_pills)
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
        self.text_question_inputting_total_pills = QtWidgets.QLabel(background_total_pills)
        self.text_question_inputting_total_pills.setGeometry(QtCore.QRect(200, 120, 841, 81))
        self.text_question_inputting_total_pills.setStyleSheet("font: 34pt \"JasmineUPC\";")
        self.text_question_inputting_total_pills.setObjectName("text_question_inputting_total_pills")
        self.lcdNumber = QtWidgets.QLCDNumber(background_total_pills)
        self.lcdNumber.setGeometry(QtCore.QRect(310, 220, 371, 131))
        self.lcdNumber.setStyleSheet("background-color: #ffffff;")
        self.lcdNumber.setObjectName("lcdNumber")
        self.slider_total_pills = QtWidgets.QSlider(background_total_pills)
        self.slider_total_pills.setGeometry(QtCore.QRect(200, 390, 601, 31))
        self.slider_total_pills.setStyleSheet("QSlider{\n"
"border-radius: 10px ;\n"
"}\n"
"\n"
"QSlider::groove:horizontal{\n"
"border: 10px ;\n"
"height: 15px;\n"
"background: #1C84A9;\n"
"}\n"
"\n"
"QSlider::handle:horizontal{\n"
"background: #1C84A9;\n"
"border: 10px ;\n"
"width: 25px;\n"
"margin: -8px 0;\n"
"border-radius: 10px;\n"
"}\n"
"QSlider::add-page:horizontal{\n"
"background-color: white;\n"
"border: 10px;\n"
"}")
        self.slider_total_pills.setSliderPosition(0)
        self.slider_total_pills.setOrientation(QtCore.Qt.Horizontal)
        self.slider_total_pills.setObjectName("slider_total_pills")
        self.button_save_total_pills = QtWidgets.QToolButton(background_total_pills)
        self.button_save_total_pills.setGeometry(QtCore.QRect(250, 450, 211, 91))
        self.button_save_total_pills.setStyleSheet("font: 75 36pt \"JasmineUPC\";\n"
"background-color:#24BD73;\n"
"color: #ffffff;\n"
"border-radius:20px;")
        self.button_save_total_pills.setObjectName("button_save_total_pills")
        self.button_skip_total_pills = QtWidgets.QToolButton(background_total_pills)
        self.button_skip_total_pills.setGeometry(QtCore.QRect(530, 450, 211, 91))
        self.button_skip_total_pills.setStyleSheet("font: 75 36pt \"JasmineUPC\";\n"
"background-color:#DD5D5D;\n"
"color: #ffffff;\n"
"border-radius:20px;")
        self.button_skip_total_pills.setObjectName("button_skip_total_pills")

        self.retranslateUi(background_total_pills)
        QtCore.QMetaObject.connectSlotsByName(background_total_pills)

    def retranslateUi(self, background_total_pills):
        _translate = QtCore.QCoreApplication.translate

        global globalPillData
        channelID = "ช่องที่ " + str(globalPillData["id"] + 1)
        
        background_total_pills.setWindowTitle(_translate("background_total_pills", "Dialog"))
        self.no_channel.setText(_translate("background_total_pills", channelID))
        self.text_question_inputting_total_pills.setText(_translate("background_total_pills", "กรุณาระบุจำนวนเม็ดยาทั้งหมดที่บรรจุ"))
        self.button_save_total_pills.setText(_translate("background_total_pills", "บันทึก"))
        self.button_skip_total_pills.setText(_translate("background_total_pills", "ข้าม"))

    #======================= define function : update slibar =======================#
    def updateSliderTotalPills(self,count_of_total_pills):
        self.lcdNumber.display(count_of_total_pills)
        print("test", self.lcdNumber.display)
        print("[total of pills] : ",count_of_total_pills)
        self.total_pills = count_of_total_pills

    #======================= define function : Go to amount pill per time =======================#
    def goToAmountPillPerTimeScreen(self, isSkip):
        if not hasattr(self, 'total_pills') or isSkip:
            self.total_pills = -1
            
        global globalPillData
        globalPillData["totalPills"] = self.total_pills
        print(globalPillData)

        pill_per_time_screen = AmountPillPerTimeScreen()
        __main__.widget.addWidget(pill_per_time_screen)
        __main__.widget.setCurrentIndex(__main__.widget.currentIndex()+1)

class AmountPillPerTimeScreen(QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
    #======================= set min-max of amount pill per time screen =======================#
        self.slider_amount_pill_per_time.setMaximum(10)
        self.slider_amount_pill_per_time.setMinimum(0)
        self.slider_amount_pill_per_time.valueChanged.connect(self.updateSliderPillPerTime)
        self.button_next.clicked.connect(self.gotoInputTimesToTakePill)
          
    def setupUi(self, background_amount_pill_per_time):
        background_amount_pill_per_time.setObjectName("background_amount_pill_per_time")
        background_amount_pill_per_time.resize(1024, 600)
        background_amount_pill_per_time.setStyleSheet("QWidget#background_amount_pill_per_time{\n"
"background-color: #97C7F9}")
        self.no_channel = QtWidgets.QLabel(background_amount_pill_per_time)
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
        self.text_question_amount_pill_per_time = QtWidgets.QLabel(background_amount_pill_per_time)
        self.text_question_amount_pill_per_time.setGeometry(QtCore.QRect(200, 120, 841, 81))
        self.text_question_amount_pill_per_time.setStyleSheet("font: 34pt \"JasmineUPC\";")
        self.text_question_amount_pill_per_time.setObjectName("text_question_amount_pill_per_time")
        self.lcdNumberPillPerTime = QtWidgets.QLCDNumber(background_amount_pill_per_time)
        self.lcdNumberPillPerTime.setGeometry(QtCore.QRect(310, 220, 371, 131))
        self.lcdNumberPillPerTime.setStyleSheet("background-color: #ffffff;")
        self.lcdNumberPillPerTime.setObjectName("lcdNumberPillPerTime")
        self.slider_amount_pill_per_time = QtWidgets.QSlider(background_amount_pill_per_time)
        self.slider_amount_pill_per_time.setGeometry(QtCore.QRect(200, 390, 601, 31))
        self.slider_amount_pill_per_time.setStyleSheet("QSlider{\n"
"border-radius: 10px ;\n"
"}\n"
"\n"
"QSlider::groove:horizontal{\n"
"border: 10px ;\n"
"height: 15px;\n"
"background: #1C84A9;\n"
"}\n"
"\n"
"QSlider::handle:horizontal{\n"
"background: #1C84A9;\n"
"border: 10px ;\n"
"width: 25px;\n"
"margin: -8px 0;\n"
"border-radius: 10px;\n"
"}\n"
"QSlider::add-page:horizontal{\n"
"background-color: white;\n"
"border: 10px;\n"
"}")
        self.slider_amount_pill_per_time.setSliderPosition(0)
        self.slider_amount_pill_per_time.setOrientation(QtCore.Qt.Horizontal)
        self.slider_amount_pill_per_time.setObjectName("slider_amount_pill_per_time")
        self.button_next = QtWidgets.QToolButton(background_amount_pill_per_time)
        self.button_next.setGeometry(QtCore.QRect(390, 450, 211, 91))
        self.button_next.setStyleSheet("font: 75 36pt \"JasmineUPC\";\n"
"background-color:#24BD73;\n"
"color: #ffffff;\n"
"border-radius:20px;")
        self.button_next.setObjectName("button_next")

        self.retranslateUi(background_amount_pill_per_time)
        QtCore.QMetaObject.connectSlotsByName(background_amount_pill_per_time)

    def retranslateUi(self, background_amount_pill_per_time):
        _translate = QtCore.QCoreApplication.translate

        global globalPillData
        channelID = "ช่องที่ " + str(globalPillData["id"] + 1)

        background_amount_pill_per_time.setWindowTitle(_translate("background_amount_pill_per_time", "Dialog"))
        self.no_channel.setText(_translate("background_amount_pill_per_time", channelID))
        self.text_question_amount_pill_per_time.setText(_translate("background_amount_pill_per_time", "กรุณาระบุจำนวนเม็ดยาที่ต้องทานในเเต่ละมื้อ"))
        self.button_next.setText(_translate("background_amount_pill_per_time", "ถัดไป"))

    #======================= define function : update slibar =======================#
    def updateSliderPillPerTime(self,amount_of_pill_per_time):
        self.lcdNumberPillPerTime.display(amount_of_pill_per_time)
        print("[amount of pill per time] : ",amount_of_pill_per_time)
        self.amount_pill =  amount_of_pill_per_time
        #======================= add amount pill per time data to array object =======================#

    def gotoInputTimesToTakePill(self):

        if hasattr(self, 'amount_pill') :
            print("ไปหน้าเพิ่มเวลาทานยา")

            global globalPillData
            globalPillData["pillsPerTime"] = self.amount_pill
            print(globalPillData)

            input_times_to_take_pill_screen = InputTimeToTakePillScreen(globalPillData, -1)
            __main__.widget.addWidget(input_times_to_take_pill_screen)
            __main__.widget.setCurrentIndex(__main__.widget.currentIndex()+1)
