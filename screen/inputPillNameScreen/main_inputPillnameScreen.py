import sys,os
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QLabel
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QMovie
from gen.gen_input_pill_name_screen import *
from gen.gen_voice_loading_screen import *
from gen.gen_confirm_pill_name_screen import *

class InputPillNameScreen(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_input_pil_name()
        self.ui.setupUi(self)
        self.ui.button_input_pill_name.clicked.connect(self.clickVoiceButton)

    def clickVoiceButton(self):
        loading_screen = LoadingVoiceScreen()
        widget.addWidget(loading_screen)
        widget.setCurrentIndex(widget.currentIndex()+1)

class LoadingVoiceScreen(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_voice_loading()
        self.ui.setupUi(self)

        #================ set voice loading gif ====================#
        self.movie = QMovie('screen\inputPillNameScreen\sound.gif')
        self.ui.label_voice_gif.setMovie(self.movie)
        #================ set delay 2 second ====================#
        timer = QTimer(self)
        self.startAnimation()
        timer.singleShot(2000, self.stopAnimation)
        self.show()

    def startAnimation(self):
        self.movie.start()

    def stopAnimation(self):
        self.movie.stop()
        self.close()
        #================ go to pill name screen ====================#
        confirm_pill_name_screen = ConfirmPillNameScreen()
        widget.addWidget(confirm_pill_name_screen)
        widget.setCurrentIndex(widget.currentIndex()+1)

class ConfirmPillNameScreen(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_confirm_pill_name()
        self.ui.setupUi(self)
        #================ click button correct or incorrect ====================#
        # self.ui.button_correct_pill_name.clicked.connect(self.clickCorrectButton)
        self.ui.button_incorrect_pill_name.clicked.connect(self.clickIncorrectButton)

    def clickIncorrectButton(self):
          self.ui = Ui_input_pil_name()


if __name__ == "__main__":
     app = QApplication(sys.argv)
     screen = InputPillNameScreen()
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
