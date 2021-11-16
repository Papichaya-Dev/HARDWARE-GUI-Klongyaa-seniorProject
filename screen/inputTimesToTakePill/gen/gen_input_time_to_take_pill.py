from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_input_times_to_take_pill(object):
    def setupUi(self, background_input_times_to_take_pill):
        background_input_times_to_take_pill.setObjectName("background_input_times_to_take_pill")
        background_input_times_to_take_pill.resize(1020, 600)
        background_input_times_to_take_pill.setStyleSheet("QWidget#background_input_times_to_take_pill{\n"
"background-color: #97C7F9}")
        self.no_channel = QtWidgets.QLabel(background_input_times_to_take_pill)
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
        self.question_input_times_to_take_pill = QtWidgets.QLabel(background_input_times_to_take_pill)
        self.question_input_times_to_take_pill.setGeometry(QtCore.QRect(190, 150, 621, 201))
        self.question_input_times_to_take_pill.setStyleSheet("font: 34pt \"JasmineUPC\";")
        self.question_input_times_to_take_pill.setAlignment(QtCore.Qt.AlignCenter)
        self.question_input_times_to_take_pill.setObjectName("question_input_times_to_take_pill")
        self.button_input_times_to_take_pill = QtWidgets.QToolButton(background_input_times_to_take_pill)
        self.button_input_times_to_take_pill.setGeometry(QtCore.QRect(430, 350, 141, 125))
        self.button_input_times_to_take_pill.setStyleSheet("QToolButton#button_input_times_to_take_pill {\n"
"   background-image: url(:/newPrefix/mic_icon.png); \n"
"   border-radius: 35;\n"
"   width:30px;\n"
"}\n"
"QToolButton#button_input_times_to_take_pill:hover {\n"
"    background-color:#24BD73;\n"
"    background-image: url(:/newPrefix/mic_icon.png);\n"
"   border-radius: 35;\n"
"   background-color:#B9D974;\n"
"    width: 170px;\n"
"    height: 100px;\n"
"}")
        self.button_input_times_to_take_pill.setText("")
        self.button_input_times_to_take_pill.setObjectName("button_input_times_to_take_pill")

        self.retranslateUi(background_input_times_to_take_pill)
        QtCore.QMetaObject.connectSlotsByName(background_input_times_to_take_pill)

    def retranslateUi(self, background_input_times_to_take_pill):
        _translate = QtCore.QCoreApplication.translate
        background_input_times_to_take_pill.setWindowTitle(_translate("background_input_times_to_take_pill", "Dialog"))
        self.no_channel.setText(_translate("background_input_times_to_take_pill", "ช่องที่ 1"))
        self.question_input_times_to_take_pill.setText(_translate("background_input_times_to_take_pill", "ดำเนินการกดปุ่ม \n"
" เพื่อพูดเวลาทานยาพาราเซตามอล"))

import mic_icon


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    background_input_times_to_take_pill = QtWidgets.QDialog()
    ui = Ui_input_times_to_take_pill()
    ui.setupUi(background_input_times_to_take_pill)
    background_input_times_to_take_pill.show()
    sys.exit(app.exec_())

