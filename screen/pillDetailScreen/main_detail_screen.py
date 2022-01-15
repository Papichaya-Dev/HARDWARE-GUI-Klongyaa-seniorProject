from PyQt5 import QtCore, QtGui, QtWidgets
import __main__

class DetailScreen(QtWidgets.QDialog):
    def __init__(self, pill_channel_data):
        super().__init__()
        self.pill_channel_data = pill_channel_data
        self.setupUi(self)

    def setupUi(self, background_detail_screen):
        background_detail_screen.setObjectName("background_detail_screen")
        background_detail_screen.resize(1020, 600)
        background_detail_screen.setStyleSheet("QWidget#background_detail_screen{\n"
"background-color: #97C7F9}")
        self.text_header_summary_screen = QtWidgets.QLabel(background_detail_screen)
        self.text_header_summary_screen.setGeometry(QtCore.QRect(300, 80, 375, 61))
        self.text_header_summary_screen.setStyleSheet("font: 75 34pt \"JasmineUPC\";\n"
"")
        self.text_header_summary_screen.setScaledContents(False)
        self.text_header_summary_screen.setAlignment(QtCore.Qt.AlignCenter)
        self.text_header_summary_screen.setWordWrap(False)
        self.text_header_summary_screen.setIndent(50)
        self.text_header_summary_screen.setObjectName("text_header_summary_screen")
        self.scroll_area = QtWidgets.QScrollArea(background_detail_screen)
        self.scroll_area.setGeometry(QtCore.QRect(20, 160, 981, 300))
        self.scroll_area.setMinimumSize(QtCore.QSize(0, 300))
        self.scroll_area.setStyleSheet("background-color:rgb(156, 183, 255);\n"
"border-color:rgb(156, 183, 255);\n"
"\n"
"")
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setObjectName("scroll_area")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 958, 324))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.data_total_pills = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.data_total_pills.setEnabled(True)
        self.data_total_pills.setMinimumSize(QtCore.QSize(350, 60))
        self.data_total_pills.setStyleSheet("font: 75 34pt \"JasmineUPC\";\n"
"color: #070021;\n"
"margin-right:50px")
        self.data_total_pills.setObjectName("data_total_pills")
        self.gridLayout_2.addWidget(self.data_total_pills, 5, 1, 1, 1)
        self.label_total_pills = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(15)
        sizePolicy.setHeightForWidth(self.label_total_pills.sizePolicy().hasHeightForWidth())
        self.label_total_pills.setSizePolicy(sizePolicy)
        self.label_total_pills.setMinimumSize(QtCore.QSize(20, 30))
        self.label_total_pills.setMaximumSize(QtCore.QSize(360, 16777215))
        self.label_total_pills.setSizeIncrement(QtCore.QSize(0, 0))
        self.label_total_pills.setStyleSheet("background-color: none;\n"
"font: 75 30pt \"JasmineUPC\";\n"
"border-radius: 25px;\n"
"color: #070021;\n"
"background-color: #C5E1FF;")
        self.label_total_pills.setTextFormat(QtCore.Qt.AutoText)
        self.label_total_pills.setScaledContents(True)
        self.label_total_pills.setAlignment(QtCore.Qt.AlignCenter)
        self.label_total_pills.setWordWrap(True)
        self.label_total_pills.setObjectName("label_total_pills")
        self.gridLayout_2.addWidget(self.label_total_pills, 5, 0, 1, 1)
        self.data_time_0 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.data_time_0.setStyleSheet("font: 75 34pt \"JasmineUPC\";\n"
"color: #070021;\n"
"")

        self.data_time_0.setObjectName("data_time_0")
        self.gridLayout_2.addWidget(self.data_time_0, 12, 1, 1, 1)
        
        self.label_amount_pill = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_amount_pill.setMinimumSize(QtCore.QSize(350, 0))
        self.label_amount_pill.setMaximumSize(QtCore.QSize(400, 16777215))
        self.label_amount_pill.setStyleSheet("background-color: none;\n"
"font: 75 30pt \"JasmineUPC\";\n"
"border-radius: 25px;\n"
"color: #070021;\n"
"background-color: #C5E1FF;")
        self.label_amount_pill.setAlignment(QtCore.Qt.AlignCenter)
        self.label_amount_pill.setWordWrap(True)
        self.label_amount_pill.setObjectName("label_amount_pill")
        self.gridLayout_2.addWidget(self.label_amount_pill, 8, 0, 1, 1)
        self.label_pill_name = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_pill_name.sizePolicy().hasHeightForWidth())
        self.label_pill_name.setSizePolicy(sizePolicy)
        self.label_pill_name.setMinimumSize(QtCore.QSize(250, 35))
        self.label_pill_name.setMaximumSize(QtCore.QSize(2, 100))
        self.label_pill_name.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("JasmineUPC")
        font.setPointSize(30)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_pill_name.setFont(font)
        self.label_pill_name.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_pill_name.setStyleSheet("background-color: #C5E1FF;\n"
"font: 75 30pt \"JasmineUPC\";\n"
"border-radius: 25px;\n"
"color: #070021;\n"
"\n"
"")
        self.label_pill_name.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_pill_name.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_pill_name.setScaledContents(False)
        self.label_pill_name.setAlignment(QtCore.Qt.AlignCenter)
        self.label_pill_name.setWordWrap(True)
        self.label_pill_name.setObjectName("label_pill_name")
        self.gridLayout_2.addWidget(self.label_pill_name, 0, 0, 1, 1)

        #---------------------------------------------------------------------------------------#
        #------------------------- SHOW TIME USE FOR LOOP ---------------------------------------#
        for time in self.pill_channel_data["timeToTake"] :
            timeIndex = self.pill_channel_data["timeToTake"].index(time)

            timeToTakeLabelObjectName = "label_time_no_" + str(timeIndex)
            timeToTakeLabelNameText = "เวลาที่ " + str(timeIndex + 1)
            timeToTakeLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
            timeToTakeLabel.setMinimumSize(QtCore.QSize(250, 0))
            timeToTakeLabel.setMaximumSize(QtCore.QSize(250, 16777215))
            timeToTakeLabel.setStyleSheet("background-color: none;\n" "font: 75 30pt \"JasmineUPC\";\n" "border-radius: 25px;\n" "color: #070021;\n" "background-color: #C5E1FF;")
            timeToTakeLabel.setAlignment(QtCore.Qt.AlignCenter)
            timeToTakeLabel.setText(timeToTakeLabelNameText)
            timeToTakeLabel.setObjectName(timeToTakeLabelObjectName)
            self.gridLayout_2.addWidget(timeToTakeLabel, timeIndex + 12, 0, 1, 1)

            timeToTakeDataObjectName = "data_time_no_" + str(timeIndex)
            timeToTakeDataNameText = str(time) + " น."
            timeToTakeData = QtWidgets.QLabel(self.scrollAreaWidgetContents)
            timeToTakeData.setText(timeToTakeDataNameText)
            timeToTakeData.setStyleSheet("font: 75 34pt \"JasmineUPC\";\n" "color: #070021;\n" "")
            timeToTakeData.setObjectName(timeToTakeDataObjectName)
            self.gridLayout_2.addWidget(timeToTakeData, timeIndex + 12, 1, 1, 1)
            #--------------- CREATE BUTTON FAKE -------------------------------------------#
            button_fake = QtWidgets.QToolButton(self.scrollAreaWidgetContents)
            button_fake.setMinimumSize(QtCore.QSize(70, 70))
            button_fake.setStyleSheet("QToolButton#button_fake {\n"
"   font-size: 40px;\n"
"  background-color:rgb(156, 183, 255);\n"
"  border-radius: 35px;\n"
"  color: white;\n"
"}\n"
"QToolButton#button_fake :hover {\n"
" font-size: 40px;\n"
" background-color:rgb(156, 183, 255);\n"
"  border-radius:35px;\n"
"  color: white;\n"
"}")
            button_fake.setText("")
            button_fake.setObjectName("button_fake")
            self.gridLayout_2.addWidget(button_fake, timeIndex + 12, 2, 1, 1)

        
        self.data_pill_name = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.data_pill_name.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.data_pill_name.sizePolicy().hasHeightForWidth())
        self.data_pill_name.setSizePolicy(sizePolicy)
        self.data_pill_name.setMinimumSize(QtCore.QSize(379, 0))
        self.data_pill_name.setStyleSheet("font: 75 32pt \"JasmineUPC\";\n"
"color: #070021;\n"
"border: none;\n"
"margin-right:50px")
        self.data_pill_name.setObjectName("data_pill_name")
        self.gridLayout_2.addWidget(self.data_pill_name, 0, 1, 1, 1)
        self.data_amount_pill = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(50)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.data_amount_pill.sizePolicy().hasHeightForWidth())
        self.data_amount_pill.setSizePolicy(sizePolicy)
        self.data_amount_pill.setStyleSheet("font: 75 34pt \"JasmineUPC\";\n"
"color: #070021;\n"
"margin-right:50px")
        self.data_amount_pill.setObjectName("data_amount_pill")
        self.gridLayout_2.addWidget(self.data_amount_pill, 8, 1, 1, 1)
        
        self.button_fake = QtWidgets.QToolButton(self.scrollAreaWidgetContents)
        self.button_fake.setMinimumSize(QtCore.QSize(70, 70))
        self.button_fake.setStyleSheet("QToolButton#button_fake  {\n"
"   font-size: 40px;\n"
"  background-color:rgb(156, 183, 255);\n"
"  border-radius: 35px;\n"
"  color: white;\n"
"}\n"
"QToolButton#button_fake :hover {\n"
" font-size: 40px;\n"
" background-color:rgb(156, 183, 255);\n"
"  border-radius:35px;\n"
"  color: white;\n"
"}")
        self.button_fake.setText("")
        self.button_fake.setObjectName("button_fake")
        self.gridLayout_2.addWidget(self.button_fake, 0, 2, 1, 1)
        self.button_fake_2 = QtWidgets.QToolButton(self.scrollAreaWidgetContents)
        self.button_fake_2.setMinimumSize(QtCore.QSize(70, 70))
        self.button_fake_2.setStyleSheet("QToolButton#button_fake_2  {\n"
"   font-size: 40px;\n"
"  background-color:rgb(156, 183, 255);\n"
"  border-radius: 35px;\n"
"  color: white;\n"
"}\n"
"QToolButton#button_fake_name_2 :hover {\n"
" font-size: 40px;\n"
" background-color:rgb(156, 183, 255);\n"
"  border-radius:35px;\n"
"  color: white;\n"
"}")
        self.button_fake_2.setText("")
        self.button_fake_2.setObjectName("button_fake_2")
        self.gridLayout_2.addWidget(self.button_fake_2, 5, 2, 1, 1)
        self.button_fake_3 = QtWidgets.QToolButton(self.scrollAreaWidgetContents)
        self.button_fake_3.setMinimumSize(QtCore.QSize(70, 70))
        self.button_fake_3.setStyleSheet("QToolButton#button_fake_3  {\n"
"   font-size: 40px;\n"
"  background-color:rgb(156, 183, 255);\n"
"  border-radius: 35px;\n"
"  color: white;\n"
"}\n"
"QToolButton#button_fake_3 :hover {\n"
" font-size: 40px;\n"
" background-color:rgb(156, 183, 255);\n"
"  border-radius:35px;\n"
"  color: white;\n"
"}")
        self.button_fake_3.setText("")
        self.button_fake_3.setObjectName("button_fake_3")
        self.gridLayout_2.addWidget(self.button_fake_3, 8, 2, 1, 1)

        self.button_fake_4 = QtWidgets.QToolButton(self.scrollAreaWidgetContents)
        self.button_fake_4.setMinimumSize(QtCore.QSize(70, 70))
        self.button_fake_4.setStyleSheet("QToolButton#button_fake_4  {\n"
"   font-size: 40px;\n"
"  background-color:rgb(156, 183, 255);\n"
"  border-radius: 35px;\n"
"  color: white;\n"
"}\n"
"QToolButton#button_fake_4 :hover {\n"
" font-size: 40px;\n"
" background-color:rgb(156, 183, 255);\n"
"  border-radius:35px;\n"
"  color: white;\n"
"}")
        self.button_fake_4.setText("")
        self.button_fake_4.setObjectName("button_fake_4")
        self.gridLayout_2.addWidget(self.button_fake_4, 12, 2, 1, 1)
        
        self.scroll_area.setWidget(self.scrollAreaWidgetContents)
        self.button_go_back = QtWidgets.QToolButton(background_detail_screen,clicked = lambda:self.goBack())
        self.button_go_back.setGeometry(QtCore.QRect(240, 490, 221, 91))
        self.button_go_back.setMinimumSize(QtCore.QSize(100, 50))
        self.button_go_back.setStyleSheet("QToolButton#button_go_back {\n"
"       font: 75 36pt \"JasmineUPC\";\n"
"    background-color:#24BD73;\n"
"    color: #ffffff;\n"
"    border-radius:20px;\n"
"        width: 170px;\n"
"    height: 100px;\n"
"}\n"
"QToolButton#button_go_back:hover {\n"
"    font: 75 36pt \"JasmineUPC\";\n"
"    background-color:#23B36D;\n"
"    color: #ffffff;\n"
"    border-radius:20px;\n"
"        width: 170px;\n"
"    height: 100px;\n"
"}")

        self.button_go_back.setObjectName("button_go_back")
        self.no_channel = QtWidgets.QLabel(background_detail_screen)
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
        self.button_edit_pill_data = QtWidgets.QToolButton(background_detail_screen)
        self.button_edit_pill_data.setGeometry(QtCore.QRect(920, 30, 75, 75))
        self.button_edit_pill_data.setMinimumSize(QtCore.QSize(70, 70))
        self.button_edit_pill_data.setStyleSheet("QToolButton#button_edit_pill_data  {\n"
"   font-size: 40px;\n"
"  background-color: rgb(255, 74, 74);\n"
"  border-radius: 35px;\n"
"  color: white;\n"
"}\n"
"QToolButton#button_edit_pill_data :hover {\n"
" font-size: 40px;\n"
"  background-color: rgb(255, 50, 50);\n"
"  border-radius:35px;\n"
"  color: white;\n"
"}")
        self.button_edit_pill_data.setObjectName("button_edit_pill_data")
        self.button_edit_pill_data.clicked.connect(self.goToEditPage)

        self.button_delete_pill_channel = QtWidgets.QToolButton(background_detail_screen)
        self.button_delete_pill_channel.setGeometry(QtCore.QRect(520, 490, 221, 91))
        self.button_delete_pill_channel.setStyleSheet("QToolButton#button_delete_pill_channel {\n"
"       font: 75 36pt \"JasmineUPC\";\n"
"    background-color:#DD5D5D;\n"
"    color: #ffffff;\n"
"    border-radius:20px;\n"
"    width: 190px;\n"
"    height: 70px;\n"
"}\n"
"QToolButton#button_delete_pill_channel:hover {\n"
"    font: 75 36pt \"JasmineUPC\";\n"
"    background-color:#F98A8A;\n"
"    color: #ffffff;\n"
"    border-radius:20px;\n"
"    width: 190px;\n"
"    height: 70px;\n"
"}")
        self.button_delete_pill_channel.setObjectName("button_delete_pill_channel")
        self.button_delete_pill_channel.clicked.connect(self.deletePillData)

        self.retranslateUi(background_detail_screen)
        QtCore.QMetaObject.connectSlotsByName(background_detail_screen)

    def deletePillData(self):
        id = self.pill_channel_data["id"]
        __main__.pill_channel_datas[str(id)] = {}
        __main__.widget.removeWidget(self)
        __main__.widget.addWidget(__main__.HomeScreen(__main__.pill_channel_datas, __main__.config))
        __main__.widget.setCurrentIndex(__main__.widget.currentIndex()+1)

    def retranslateUi(self, background_detail_screen):
        headerText = "ข้อมูลยาช่องที่ " + str(self.pill_channel_data["id"] + 1)
        pillAmountText = str(self.pill_channel_data["pillsPerTime"]) + " เม็ด/มื้อ"
        channelNotext = "ช่องที่ " + str(self.pill_channel_data["id"] + 1)
        pillTotalText = str(self.pill_channel_data["totalPills"]) + " เม็ด"

        _translate = QtCore.QCoreApplication.translate
        background_detail_screen.setWindowTitle(_translate("background_detail_screen", "Pill Detail Screen"))
        self.text_header_summary_screen.setText(_translate("background_detail_screen", headerText))
        
        self.label_amount_pill.setText(_translate("background_detail_screen", "จำนวนยาที่ต้องทาน"))
        self.label_total_pills.setText(_translate("background_detail_screen", "จำนวนยาทั้งหมด"))
        self.label_pill_name.setText(_translate("background_detail_screen", "ชื่อยา"))

        self.data_pill_name.setText(_translate("background_detail_screen", self.pill_channel_data["name"]))
        self.data_amount_pill.setText(_translate("background_detail_screen", pillAmountText))
        self.data_total_pills.setText(_translate("background_detail_screen", pillTotalText))

        self.button_go_back.setText(_translate("background_detail_screen", "ย้อนกลับ"))
        self.button_delete_pill_channel.setText(_translate("background_detail_screen", "ลบ"))
        self.button_edit_pill_data.setText(_translate("background_detail_screen", "🖉"))

        self.no_channel.setText(_translate("background_detail_screen", channelNotext))
    def goBack(self) :
        __main__.widget.removeWidget(self)
        __main__.widget.addWidget(__main__.HomeScreen(__main__.pill_channel_datas, __main__.config))
        __main__.widget.setCurrentIndex(__main__.widget.currentIndex() + 1)

    def goToEditPage(self) :
        pillSummaryScreen = __main__.PillSummaryScreen(self.pill_channel_data)
        __main__.widget.removeWidget(self)
        __main__.widget.addWidget(pillSummaryScreen)
        __main__.widget.setCurrentIndex(__main__.widget.currentIndex()+1)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    detailScreen = QtWidgets.QDialog()
    ui = DetailScreen()
    ui.setupUi(detailScreen)
    detailScreen.show()
    sys.exit(app.exec_())
