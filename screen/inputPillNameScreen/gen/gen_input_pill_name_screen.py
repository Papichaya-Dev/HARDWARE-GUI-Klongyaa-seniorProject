from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_input_pil_name(object):
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
        self.question_input_pill_name_1 = QtWidgets.QLabel(background_input_pil_name)
        self.question_input_pill_name_1.setGeometry(QtCore.QRect(350, 150, 311, 81))
        self.question_input_pill_name_1.setStyleSheet("font: 34pt \"JasmineUPC\";")
        self.question_input_pill_name_1.setAlignment(QtCore.Qt.AlignCenter)
        self.question_input_pill_name_1.setObjectName("question_input_pill_name_1")
        self.question_input_pill_name_2 = QtWidgets.QLabel(background_input_pil_name)
        self.question_input_pill_name_2.setGeometry(QtCore.QRect(310, 230, 381, 81))
        self.question_input_pill_name_2.setStyleSheet("font: 38pt \"JasmineUPC\";")
        self.question_input_pill_name_2.setAlignment(QtCore.Qt.AlignCenter)
        self.question_input_pill_name_2.setObjectName("question_input_pill_name_2")
        self.button_input_pill_name = QtWidgets.QToolButton(background_input_pil_name)
        self.button_input_pill_name.setGeometry(QtCore.QRect(430, 350, 141, 125))
        self.button_input_pill_name.setStyleSheet("QToolButton#button_input_pill_name {\n"
"   background-image: url(:/newPrefix/mic_icon.png); \n"
"   border-radius: 35;\n"
"   width:30px;\n"
"}\n"
"QToolButton#button_input_pill_name:hover {\n"
"    background-color:#24BD73;\n"
"    background-image: url(:/newPrefix/mic_icon.png);\n"
"   border-radius: 35;\n"
"   background-color:#B9D974;\n"
"    width: 170px;\n"
"    height: 100px;\n"
"}")
        self.button_input_pill_name.setText("")
        self.button_input_pill_name.setObjectName("button_input_pill_name")

        self.retranslateUi(background_input_pil_name)
        QtCore.QMetaObject.connectSlotsByName(background_input_pil_name)

    def retranslateUi(self, background_input_pil_name):
        _translate = QtCore.QCoreApplication.translate
        background_input_pil_name.setWindowTitle(_translate("background_input_pil_name", "Dialog"))
        self.no_channel.setText(_translate("background_input_pil_name", "ช่องที่ 1"))
        self.question_input_pill_name_1.setText(_translate("background_input_pil_name", "ดำเนินการกดปุ่ม"))
        self.question_input_pill_name_2.setText(_translate("background_input_pil_name", "เพื่อพูดชื่อยาของท่าน"))

import gen.icon_microphone_button

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    background_input_pil_name = QtWidgets.QDialog()
    ui = Ui_input_pil_name()
    ui.setupUi(background_input_pil_name)
    background_input_pil_name.show()
    sys.exit(app.exec_())

