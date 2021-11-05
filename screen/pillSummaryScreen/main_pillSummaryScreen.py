import sys
from screen.pillSummaryScreen.gen.gen_pill_summary_screen import *
from PyQt5.QtWidgets import QDialog, QApplication, QWidget 
from screen.pillSummaryScreen.mock.pill_data import pill_data
from PyQt5 import QtCore, QtGui, QtWidgets 
from shared.main_success_save_screen import SuccessSaveScreen

import __main__

globalPillData = {}

class PillSummaryScreen(QDialog):
    def __init__(self, pillData):
        super().__init__()
        global globalPillData
        globalPillData = pillData

        self.setupUi(self)
        self.button_save_pill_summary.clicked.connect(self.savePillSummary)

        #----------- SET VARIABLE OF TEXT LABEL ------------#
        unit_pill = " เม็ด"
        unit_time = " น."

        #----------- SET EDIT BUTTON TO CONNECT EACH PAGE -----------#
        self.button_edit_pill_name.clicked.connect(lambda:self.editPillName("pill_name"))
        self.button_edit_amount_pill.clicked.connect(lambda:self.editPillName("amount_pill"))
        self.button_edit_time.clicked.connect(lambda:self.editPillName("time"))

        if globalPillData["totalPills"] > 0 :
                self.button_edit_total_pills.clicked.connect(lambda:self.editPillName("total_pills"))

    def setupUi(self, background_summary_screen):
        global globalPillData

        currentRow = 0

        background_summary_screen.setObjectName("background_summary_screen")
        background_summary_screen.resize(1020, 600)
        background_summary_screen.setStyleSheet("QWidget#background_summary_screen{\n" "background-color: #97C7F9}")
        self.text_header_summary_screen = QtWidgets.QLabel(background_summary_screen)
        self.text_header_summary_screen.setGeometry(QtCore.QRect(300, 80, 375, 61))
        self.text_header_summary_screen.setStyleSheet("font: 75 34pt \"JasmineUPC\";\n" "")
        self.text_header_summary_screen.setScaledContents(False)
        self.text_header_summary_screen.setAlignment(QtCore.Qt.AlignCenter)
        self.text_header_summary_screen.setWordWrap(False)
        self.text_header_summary_screen.setIndent(50)
        self.text_header_summary_screen.setObjectName("text_header_summary_screen")
        self.scroll_area = QtWidgets.QScrollArea(background_summary_screen)
        self.scroll_area.setGeometry(QtCore.QRect(20, 160, 981, 300))
        self.scroll_area.setMinimumSize(QtCore.QSize(0, 300))
        self.scroll_area.setStyleSheet("background-color:rgb(156, 183, 255);\n" "border-color:rgb(156, 183, 255);\n" "\n" "")
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setObjectName("scroll_area")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 958, 324))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")

        self.question_pill_name = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.question_pill_name.sizePolicy().hasHeightForWidth())
        self.question_pill_name.setSizePolicy(sizePolicy)
        self.question_pill_name.setMinimumSize(QtCore.QSize(250, 35))
        self.question_pill_name.setMaximumSize(QtCore.QSize(2, 100))
        self.question_pill_name.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("JasmineUPC")
        font.setPointSize(30)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.question_pill_name.setFont(font)
        self.question_pill_name.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.question_pill_name.setStyleSheet("background-color: #C5E1FF;\n" "font: 75 30pt \"JasmineUPC\";\n" "border-radius: 25px;\n" "color: #070021;\n" "\n" "")
        self.question_pill_name.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.question_pill_name.setFrameShadow(QtWidgets.QFrame.Plain)
        self.question_pill_name.setScaledContents(False)
        self.question_pill_name.setAlignment(QtCore.Qt.AlignCenter)
        self.question_pill_name.setWordWrap(True)
        self.question_pill_name.setObjectName("question_pill_name")
        self.gridLayout_2.addWidget(self.question_pill_name, currentRow, 0, 1, 1)

        self.show_pill_name = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.show_pill_name.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.show_pill_name.sizePolicy().hasHeightForWidth())
        self.show_pill_name.setSizePolicy(sizePolicy)
        self.show_pill_name.setMinimumSize(QtCore.QSize(379, 0))
        self.show_pill_name.setStyleSheet("font: 75 32pt \"JasmineUPC\";\n" "color: #070021;\n" "border: none;\n" "margin-right:50px")
        self.show_pill_name.setObjectName("show_pill_name")
        self.gridLayout_2.addWidget(self.show_pill_name, currentRow, 1, 1, 1)

        self.button_edit_pill_name = QtWidgets.QToolButton(self.scrollAreaWidgetContents)
        self.button_edit_pill_name.setMinimumSize(QtCore.QSize(70, 70))
        self.button_edit_pill_name.setStyleSheet("QToolButton#button_edit_pill_name  {\n" "   font-size: 40px;\n" "  background-color: rgb(255, 74, 74);\n" "  border-radius: 35px;\n" "  color: white;\n" "}\n" "QToolButton#button_edit_pill_name :hover {\n" " font-size: 40px;\n" "  background-color: rgb(255, 50, 50);\n" "  border-radius:35px;\n" "  color: white;\n" "}")
        self.button_edit_pill_name.setObjectName("button_edit_pill_name")
        self.gridLayout_2.addWidget(self.button_edit_pill_name, currentRow, 3, 1, 1)

        currentRow = currentRow + 1

        if globalPillData["totalPills"] > 0 :
                self.question_total_pills = QtWidgets.QLabel(self.scrollAreaWidgetContents)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(15)
                sizePolicy.setHeightForWidth(self.question_total_pills.sizePolicy().hasHeightForWidth())
                self.question_total_pills.setSizePolicy(sizePolicy)
                self.question_total_pills.setMinimumSize(QtCore.QSize(20, 30))
                self.question_total_pills.setMaximumSize(QtCore.QSize(360, 16777215))
                self.question_total_pills.setSizeIncrement(QtCore.QSize(0, 0))
                self.question_total_pills.setStyleSheet("background-color: none;\n" "font: 75 30pt \"JasmineUPC\";\n" "border-radius: 25px;\n" "color: #070021;\n" "background-color: #C5E1FF;")
                self.question_total_pills.setTextFormat(QtCore.Qt.AutoText)
                self.question_total_pills.setScaledContents(True)
                self.question_total_pills.setAlignment(QtCore.Qt.AlignCenter)
                self.question_total_pills.setWordWrap(True)
                self.question_total_pills.setText("จำนวนยาทั้งหมด")
                self.question_total_pills.setObjectName("question_total_pills")
                self.gridLayout_2.addWidget(self.question_total_pills, currentRow, 0, 1, 1)

                self.show_total_pills = QtWidgets.QLabel(self.scrollAreaWidgetContents)
                self.show_total_pills.setEnabled(True)
                self.show_total_pills.setMinimumSize(QtCore.QSize(350, 60))
                self.show_total_pills.setStyleSheet("font: 75 34pt \"JasmineUPC\";\n" "color: #070021;\n" "margin-right:50px")
                self.show_total_pills.setText(str(globalPillData["totalPills"]) + " เม็ด")
                self.show_total_pills.setObjectName("show_total_pills")
                self.gridLayout_2.addWidget(self.show_total_pills, currentRow, 1, 1, 1)

                self.button_edit_total_pills = QtWidgets.QToolButton(self.scrollAreaWidgetContents)
                self.button_edit_total_pills.setMinimumSize(QtCore.QSize(70, 70))
                self.button_edit_total_pills.setStyleSheet("QToolButton#button_edit_total_pills {\n" "   font-size: 40px;\n" "  background-color: rgb(255, 74, 74);\n" "  border-radius: 35px;\n" "  color: white;\n" "}\n" "QToolButton#button_edit_total_pills:hover {\n" "    font-size: 40px;\n" "  background-color: rgb(255, 50, 50);\n" "  border-radius: 35px;\n" "  color: white;\n" "}")
                self.button_edit_total_pills.setText("🖉")
                self.button_edit_total_pills.setObjectName("button_edit_total_pills")
                self.gridLayout_2.addWidget(self.button_edit_total_pills, currentRow, 3, 1, 1)

                currentRow = currentRow + 1

        self.question_amount_pill = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.question_amount_pill.setMinimumSize(QtCore.QSize(350, 0))
        self.question_amount_pill.setMaximumSize(QtCore.QSize(400, 16777215))
        self.question_amount_pill.setStyleSheet("background-color: none;\n" "font: 75 30pt \"JasmineUPC\";\n" "border-radius: 25px;\n" "color: #070021;\n" "background-color: #C5E1FF;")
        self.question_amount_pill.setAlignment(QtCore.Qt.AlignCenter)
        self.question_amount_pill.setWordWrap(True)
        self.question_amount_pill.setObjectName("question_amount_pill")
        self.gridLayout_2.addWidget(self.question_amount_pill, currentRow, 0, 1, 1)

        self.show_amount_pill = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(50)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.show_amount_pill.sizePolicy().hasHeightForWidth())
        self.show_amount_pill.setSizePolicy(sizePolicy)
        self.show_amount_pill.setStyleSheet("font: 75 34pt \"JasmineUPC\";\n" "color: #070021;\n" "margin-right:50px")
        self.show_amount_pill.setObjectName("show_amount_pill")
        self.gridLayout_2.addWidget(self.show_amount_pill, currentRow, 1, 1, 1)

        self.button_edit_amount_pill = QtWidgets.QToolButton(self.scrollAreaWidgetContents)
        self.button_edit_amount_pill.setMinimumSize(QtCore.QSize(70, 70))
        self.button_edit_amount_pill.setStyleSheet("QToolButton#button_edit_amount_pill {\n" "   font-size: 40px;\n" "  background-color: rgb(255, 74, 74);\n" "  border-radius: 35px;\n" "  color: white;\n" "}\n" "QToolButton#button_edit_amount_pill {\n" "    font-size: 40px;\n" "  background-color: rgb(255, 50, 50);\n" "  border-radius: 35px;\n" "  color: white;\n" "}")
        self.button_edit_amount_pill.setObjectName("button_edit_amount_pill")
        self.gridLayout_2.addWidget(self.button_edit_amount_pill, currentRow, 3, 1, 1)

        currentRow = currentRow + 1

        self.button_edit_time = QtWidgets.QToolButton(self.scrollAreaWidgetContents)
        self.button_edit_time.setMinimumSize(QtCore.QSize(70, 70))
        self.button_edit_time.setStyleSheet("QToolButton#button_edit_time {\n" "   font-size: 40px;\n" "  background-color: rgb(255, 74, 74);\n" "  border-radius: 35px;\n" "  color: white;\n" "}\n" "QToolButton#button_edit_time {\n" "    font-size: 40px;\n" "  background-color: rgb(255, 50, 50);\n" "  border-radius: 35px;\n" "  color: white;\n" "}")
        self.button_edit_time.setObjectName("button_edit_time")
        self.gridLayout_2.addWidget(self.button_edit_time, currentRow, 3, 1, 1)

        for time in globalPillData["timeToTake"] :
                objIndex = globalPillData["timeToTake"].index(time)
                timeToTakePillLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
                timeToTakePillLabel.setMinimumSize(QtCore.QSize(250, 0))
                timeToTakePillLabel.setMaximumSize(QtCore.QSize(250, 16777215))
                timeToTakePillLabel.setStyleSheet("background-color: none;\n" "font: 75 30pt \"JasmineUPC\";\n" "border-radius: 25px;\n" "color: #070021;\n" "background-color: #C5E1FF;")
                timeToTakePillLabel.setAlignment(QtCore.Qt.AlignCenter)
                timeToTakePillLabel.setText("เวลาที่ " + str(objIndex + 1))
                timeToTakePillLabel.setObjectName("question_time_no_" + str(objIndex))
                self.gridLayout_2.addWidget(timeToTakePillLabel, (currentRow + objIndex), 0, 1, 1)

                timeToTakePillData = QtWidgets.QLabel(self.scrollAreaWidgetContents)
                timeToTakePillData.setStyleSheet("font: 75 34pt \"JasmineUPC\";\n" "color: #070021;\n" "")
                timeToTakePillData.setText(time + " น.")
                timeToTakePillData.setObjectName("show_time")
                self.gridLayout_2.addWidget(timeToTakePillData, (currentRow + objIndex), 1, 1, 1)

                currentRow = currentRow + 1

        self.scroll_area.setWidget(self.scrollAreaWidgetContents)
        self.button_save_pill_summary = QtWidgets.QToolButton(background_summary_screen)
        self.button_save_pill_summary.setGeometry(QtCore.QRect(380, 480, 231, 103))
        self.button_save_pill_summary.setMinimumSize(QtCore.QSize(100, 50))
        self.button_save_pill_summary.setStyleSheet("QToolButton#button_save_pill_summary {\n" "       font: 75 36pt \"JasmineUPC\";\n" "    background-color:#24BD73;\n" "    color: #ffffff;\n" "    border-radius:20px;\n" "        width: 170px;\n" "    height: 100px;\n" "}\n" "QToolButton#button_save_pill_summary:hover {\n" "    font: 75 36pt \"JasmineUPC\";\n" "    background-color:#23B36D;\n" "    color: #ffffff;\n" "    border-radius:20px;\n" "        width: 170px;\n" "    height: 100px;\n" "}")
        self.button_save_pill_summary.setObjectName("button_save_pill_summary")
        self.no_channel = QtWidgets.QLabel(background_summary_screen)
        self.no_channel.setGeometry(QtCore.QRect(40, 30, 191, 71))
        font = QtGui.QFont()
        font.setFamily("JasmineUPC")
        font.setPointSize(36)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.no_channel.setFont(font)
        self.no_channel.setStyleSheet("background-color: #C5E1FF;\n" "font: 75 36pt \"JasmineUPC\";\n" "border-radius: 25px;\n" "color: #070021;\n" "")
        self.no_channel.setAlignment(QtCore.Qt.AlignCenter)
        self.no_channel.setObjectName("no_channel")

        self.retranslateUi(background_summary_screen)
        QtCore.QMetaObject.connectSlotsByName(background_summary_screen)

    def retranslateUi(self, background_summary_screen):
        _translate = QtCore.QCoreApplication.translate

        global globalPillData
        pillName = globalPillData["name"]
        pillsPerTime = str(globalPillData["pillsPerTime"]) + " เม็ด/มื้อ"
        channelID = "ช่องที่ " + str(globalPillData["id"] + 1)

        
        background_summary_screen.setWindowTitle(_translate("background_summary_screen", "Dialog"))
        self.text_header_summary_screen.setText(_translate("background_summary_screen", "ข้อมูลของยาที่ต้องทาน"))
        self.show_pill_name.setText(_translate("background_summary_screen", pillName))
        self.show_amount_pill.setText(_translate("background_summary_screen", pillsPerTime))
        self.button_edit_time.setText(_translate("background_summary_screen", "🖉"))
        self.button_edit_pill_name.setText(_translate("background_summary_screen", "🖉"))
        
        self.question_amount_pill.setText(_translate("background_summary_screen", "จำนวนยาที่ต้องทาน"))
        self.button_edit_amount_pill.setText(_translate("background_summary_screen", "🖉"))
        self.question_pill_name.setText(_translate("background_summary_screen", "ชื่อยา"))
        
        self.button_save_pill_summary.setText(_translate("background_summary_screen", "บันทึก"))
        self.no_channel.setText(_translate("background_summary_screen", channelID))

    # def savePillSummary(self,edit_mode): * อย่าเพิ่งลบคอมเม้นท์
    def savePillSummary(self):
        print("mock data :", pill_data)
        #----------- SAVE AND THEN GO TO HOME SCREEN -----------#
        success_save_screen = SuccessSaveScreen()
        # self.ui.text_screen_name.setText("Home screen")
        __main__.widget.addWidget(success_save_screen)
        __main__.widget.setCurrentIndex(__main__.widget.currentIndex()+1)

    # def editPillName(self, edit_mode): * อย่าเพิ่งลบคอมเม้นท์
    def editPillName(self):
        if edit_mode == "pill_name" :
            print("ชื่อยา :", pill_data[0]["pill_name"] )
            widget.setCurrentIndex(widget.currentIndex()+1)
        if edit_mode == "total_pills" :
            print("จำนวนเม็ดยาทั้งหมด :", pill_data[0]["total_pills"] )
            widget.setCurrentIndex(widget.currentIndex()+1)
        if edit_mode == "amount_pill" :
            print("จำนวนเม็ดยาที่ต้องทาน :", pill_data[0]["amount_pill"] )
            widget.setCurrentIndex(widget.currentIndex()+1)
        if edit_mode == "time" :
            print("เวลาทานยา :", pill_data[0]["times"][0] )
            widget.setCurrentIndex(widget.currentIndex()+1)





if __name__ == "__main__":
     app = QApplication(sys.argv)
     screen = PillSummaryScreen()
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