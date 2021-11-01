from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_home_screen(object):
    def setupUi(self, background_home_screen):
        background_home_screen.setObjectName("background_home_screen")
        background_home_screen.resize(1020, 600)
        background_home_screen.setStyleSheet("QWidget#background_home_screen{\n"
"background-color: #97C7F9}")
        self.text_screen_name = QtWidgets.QLabel(background_home_screen)
        self.text_screen_name.setGeometry(QtCore.QRect(230, 210, 561, 131))
        self.text_screen_name.setStyleSheet("font: 24pt \"Gill Sans Ultra Bold\";\n"
"")
        self.text_screen_name.setAlignment(QtCore.Qt.AlignCenter)
        self.text_screen_name.setObjectName("text_screen_name")

        self.retranslateUi(background_home_screen)
        QtCore.QMetaObject.connectSlotsByName(background_home_screen)

    def retranslateUi(self, background_home_screen):
        _translate = QtCore.QCoreApplication.translate
        background_home_screen.setWindowTitle(_translate("background_home_screen", "Dialog"))
        self.text_screen_name.setText(_translate("background_home_screen", "Another screen"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    background_home_screen = QtWidgets.QDialog()
    ui = Ui_home_screen()
    ui.setupUi(background_home_screen)
    background_home_screen.show()
    sys.exit(app.exec_())

