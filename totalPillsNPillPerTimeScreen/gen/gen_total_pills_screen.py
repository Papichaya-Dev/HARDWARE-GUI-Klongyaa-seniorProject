from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_total_pills(object):
    def setupUi(self, background_total_pills):
        background_total_pills.setObjectName("background_total_pills")
        background_total_pills.resize(1020, 600)
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
        background_total_pills.setWindowTitle(_translate("background_total_pills", "Dialog"))
        self.no_channel.setText(_translate("background_total_pills", "ช่องที่ 1"))
        self.text_question_inputting_total_pills.setText(_translate("background_total_pills", "กรุณาระบุจำนวนเม็ดยาทั้งหมดที่บรรจุ"))
        self.button_save_total_pills.setText(_translate("background_total_pills", "บันทึก"))
        self.button_skip_total_pills.setText(_translate("background_total_pills", "ข้าม"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    background_total_pills = QtWidgets.QDialog()
    ui = Ui_total_pills()
    ui.setupUi(background_total_pills)
    background_total_pills.show()
    sys.exit(app.exec_())

