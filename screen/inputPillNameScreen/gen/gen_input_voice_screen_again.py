from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_input_voice_again(object):
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

import gen.mic_icon

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    bankground_input_voice_again = QtWidgets.QDialog()
    ui =  Ui_input_voice_again()
    ui.setupUi(bankground_input_voice_again)
    bankground_input_voice_again.show()
    sys.exit(app.exec_())

