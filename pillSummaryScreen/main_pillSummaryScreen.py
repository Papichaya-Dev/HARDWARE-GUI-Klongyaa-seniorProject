import sys
from gen.gen_pill_summary_screen import *
from PyQt5.QtWidgets import QDialog, QApplication, QWidget 
from mock.pill_data import pill_data
from shared.gen_mock_screen import *
from PyQt5 import QtCore, QtGui, QtWidgets 

class PillSummaryScreen(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_pill_summary_screen() 
        self.ui.setupUi(self)
        self.ui.button_save_pill_summary.clicked.connect(self.savePillSummary)
        self.ui.show_pill_name.setText(pill_data[0]["pill_name"])
        self.ui.show_total_pills.setText(str(pill_data[0]["total_pills"]))
        self.ui.show_amount_pill.setText(str(pill_data[0]["amount_pill"]))
        self.ui.show_time.setText(pill_data[0]["times"][1])
        #----------- SET EDIT BUTTON TO CONNECT EACH PAGE -----------#
        self.ui.button_edit_pill_name.clicked.connect(self.editPillName)
        self.ui.button_edit_total_pills.clicked.connect(self.editPillName)


    def savePillSummary(self):
        print("mock data :", pill_data)
        #----------- SAVE AND THEN GO TO HOME SCREEN -----------#
        mock_home_screen = MockHomescreen()
        widget.addWidget(mock_home_screen)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def editPillName(self):
        mock_home_screen = MockHomescreen()
        widget.addWidget(mock_home_screen)
        if pill_data[0]["pill_name"] :
            print("(ไปหน้าแก้ไขชื่อยา)")
            print("ชื่อยา :", pill_data[0]["pill_name"] )
            widget.setCurrentIndex(widget.currentIndex()+1)
        if pill_data[0]["total_pills"] :
            print("(ไปหน้าแก้ไขจำนวนเม็ดยาทั้งหมด)")
            print("จำนวนเม็ดยาทั้งหมด :", pill_data[0]["total_pills"] )
            widget.setCurrentIndex(widget.currentIndex()+1)


class MockHomescreen(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_home_screen() 
        self.ui.setupUi(self)
        self.ui.text_screen_name.setText("Home screen")
        if pill_data[0]["pill_name"] : 
            self.ui.text_screen_name.setText("pill name screen")
        if pill_data[0]["total_pills"] : 
            self.ui.text_screen_name.setText("total pill screen")
        if pill_data[0]["amount_pill"] : 
            self.ui.text_screen_name.setText("amount pill screen")
        

if __name__ == "__main__":
     app = QApplication(sys.argv)
     screen = PillSummaryScreen()
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