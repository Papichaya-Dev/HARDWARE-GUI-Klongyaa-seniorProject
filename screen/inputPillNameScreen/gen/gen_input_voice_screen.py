from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_input_voice(object):
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

        self.retranslateUi(background_input_pil_name)
        QtCore.QMetaObject.connectSlotsByName(background_input_pil_name)

    def retranslateUi(self, background_input_pil_name):
        _translate = QtCore.QCoreApplication.translate
        background_input_pil_name.setWindowTitle(_translate("background_input_pil_name", "Dialog"))
        self.no_channel.setText(_translate("background_input_pil_name", "ช่องที่ 1"))
        self.question_input_voice.setText(_translate("background_input_pil_name", "ดำเนินการกดปุ่ม \n"
" เพื่อพูดชื่อยาของท่าน"))

import screen.inputPillNameScreen.gen.mic_icon

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    background_input_pil_name = QtWidgets.QDialog()
    ui = Ui_input_voice()
    ui.setupUi(background_input_pil_name)
    background_input_pil_name.show()
    sys.exit(app.exec_())

