from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_amount_pill_per_time(object):
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
        background_amount_pill_per_time.setWindowTitle(_translate("background_amount_pill_per_time", "Dialog"))
        self.no_channel.setText(_translate("background_amount_pill_per_time", "ช่องที่ 1"))
        self.text_question_amount_pill_per_time.setText(_translate("background_amount_pill_per_time", "กรุณาระบุจำนวนเม็ดยาที่ต้องทาน"))
        self.button_next.setText(_translate("background_amount_pill_per_time", "ถัดไป"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    background_amount_pill_per_time = QtWidgets.QDialog()
    ui = Ui_amount_pill_per_time()
    ui.setupUi(background_amount_pill_per_time)
    background_amount_pill_per_time.show()
    sys.exit(app.exec_())

