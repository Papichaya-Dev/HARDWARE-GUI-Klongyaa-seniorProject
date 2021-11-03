from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_confirm_pill_name(object):
    def setupUi(self, background_confirm_pill_name):
        background_confirm_pill_name.setObjectName("background_confirm_pill_name")
        background_confirm_pill_name.resize(1024, 600)
        background_confirm_pill_name.setStyleSheet("QWidget#background_confirm_pill_name{\n"
"background-color: #97C7F9}")
        self.no_channel = QtWidgets.QLabel(background_confirm_pill_name)
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
        self.label_1 = QtWidgets.QLabel(background_confirm_pill_name)
        self.label_1.setGeometry(QtCore.QRect(410, 130, 171, 81))
        self.label_1.setStyleSheet("font:42pt \"JasmineUPC\";")
        self.label_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_1.setObjectName("label_1")
        self.show_pill_name = QtWidgets.QLabel(background_confirm_pill_name)
        self.show_pill_name.setGeometry(QtCore.QRect(220, 230, 561, 81))
        self.show_pill_name.setStyleSheet("font: 52pt \"JasmineUPC\";")
        self.show_pill_name.setAlignment(QtCore.Qt.AlignCenter)
        self.show_pill_name.setObjectName("show_pill_name")
        self.button_correct_pill_name = QtWidgets.QToolButton(background_confirm_pill_name)
        self.button_correct_pill_name.setGeometry(QtCore.QRect(220, 410, 251, 91))
        self.button_correct_pill_name.setStyleSheet("\n"
"\n"
"QToolButton#button_correct_pill_name {\n"
"       font: 75 36pt \"JasmineUPC\";\n"
"   background-color:#24BD73;\n"
"   color: #ffffff;\n"
"   border-radius:20px;\n"
"}\n"
"QToolButton#button_correct_pill_name:hover {\n"
"    font: 75 36pt \"JasmineUPC\";\n"
"    background-color:#23B36D;\n"
"    color: #ffffff;\n"
"    border-radius:20px;\n"
"    width: 170px;\n"
"    height:100px;\n"
"}")
        self.button_correct_pill_name.setObjectName("button_correct_pill_name")
        self.button_incorrect_pill_name = QtWidgets.QToolButton(background_confirm_pill_name)
        self.button_incorrect_pill_name.setGeometry(QtCore.QRect(560, 410, 251, 91))
        self.button_incorrect_pill_name.setStyleSheet("QToolButton#button_incorrect_pill_name {\n"
"       font: 75 36pt \"JasmineUPC\";\n"
"    background-color: #DD5D5D;\n"
"      border-radius:20px;\n"
"    color: white;\n"
"}\n"
"QToolButton#button_incorrect_pill_name:hover {\n"
"       font: 75 36pt \"JasmineUPC\";\n"
"    background-color: rgb(255, 50, 50);\n"
"      border-radius:20px;\n"
"    color: white;\n"
"}")
        self.button_incorrect_pill_name.setObjectName("button_incorrect_pill_name")

        self.retranslateUi(background_confirm_pill_name)
        QtCore.QMetaObject.connectSlotsByName(background_confirm_pill_name)

    def retranslateUi(self, background_confirm_pill_name):
        _translate = QtCore.QCoreApplication.translate
        background_confirm_pill_name.setWindowTitle(_translate("background_confirm_pill_name", "Dialog"))
        self.no_channel.setText(_translate("background_confirm_pill_name", "ช่องที่ 1"))
        self.label_1.setText(_translate("background_confirm_pill_name", "ชื่อยา"))
        self.show_pill_name.setText(_translate("background_confirm_pill_name", "ยาพาราแซลมอน"))
        self.button_correct_pill_name.setText(_translate("background_confirm_pill_name", "ถูกต้อง"))
        self.button_incorrect_pill_name.setText(_translate("background_confirm_pill_name", "ไม่ถูกต้อง"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    background_confirm_pill_name = QtWidgets.QDialog()
    ui = Ui_confirm_pill_name()
    ui.setupUi(background_confirm_pill_name)
    background_confirm_pill_name.show()
    sys.exit(app.exec_())

