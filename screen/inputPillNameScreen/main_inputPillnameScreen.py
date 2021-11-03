import sys
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QLabel
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QMovie
from gen.gen_input_pill_name_screen import *
from gen.gen_voice_loading_screen import *

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


























# class LoadingScreen(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setFixedSize(941,521)
#         self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.CustomizeWindowHint)
        
#         self.label_animation = QLabel(self)

#         self.movie = QMovie('screen\inputPillNameScreen\sound.gif')
#         self.label_animation.setMovie(self.movie)

#         timer = QTimer(self)
#         self.startAnimation()
#         # timer.singleShot(3000, self.stopAnimation)

#         self.show()

#     def startAnimation(self):
#         self.movie.start()

#     def stopAnimation(self):
#         self.movie.stop()
#         self.close()

# class AppDemo(QWidget):
#     def __init__(self):
#         super().__init__()
#         label = QLabel("Hi", self)
#         label.setGeometry(400,600,300,50)
#         self.loading_screen = LoadingScreen()
#         self.show()

# class TotalPillsScreen(QDialog):
#     def __init__(self):
#         super().__init__()
#         self.ui = Ui_total_pills() 
#         self.ui.setupUi(self)
#         #========= set max-min of total pills =========#
#         self.ui.slider_total_pills.setMaximum(30)
#         self.ui.slider_total_pills.setMinimum(0)
#         self.ui.slider_total_pills.valueChanged.connect(self.updateSliderTotalPills)
#         self.ui.button_skip_total_pills.clicked.connect(self.goToAmountPillPerTimeScreen)
#         self.ui.button_save_total_pills.clicked.connect(self.goToAmountPillPerTimeScreen)
        
#     def updateSliderTotalPills(self,count_of_total_pills):
#         self.ui.lcdNumber.display(count_of_total_pills)
#         print("[total of pills] : ",count_of_total_pills)
#         self.total_pills = [{
#             "id": 1,
#             "total_pills": count_of_total_pills,
#         }]

#     def goToAmountPillPerTimeScreen(self):
#         pill_per_time_screen = AmountPillPerTimeScreen(self.total_pills)
#         widget.addWidget(pill_per_time_screen)
#         widget.setCurrentIndex(widget.currentIndex()+1)

# app =QApplication(sys.argv)
# demo = AppDemo()
# app.exit(app.exec_())