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
        #----------- SET VARIABLE OF TEXT LABEL ------------#
        unit_pill = " เม็ด"
        unit_time = " น."
        message_total_pills = pill_data[0]["total_pills"]
        message_amount_pill = pill_data[0]["amount_pill"]
        message_time = pill_data[0]["times"][1]

        self.ui.show_pill_name.setText(pill_data[0]["pill_name"])
        self.ui.show_total_pills.setText(str(message_total_pills) + unit_pill)
        self.ui.show_amount_pill.setText(str(message_amount_pill) + unit_pill)
        self.ui.show_time.setText(str(message_time) + unit_time)
        #----------- SET EDIT BUTTON TO CONNECT EACH PAGE -----------#
        self.ui.button_edit_pill_name.clicked.connect(lambda:self.editPillName("pill_name"))
        self.ui.button_edit_total_pills.clicked.connect(lambda:self.editPillName("total_pills"))
        self.ui.button_edit_amount_pill.clicked.connect(lambda:self.editPillName("amount_pill"))
        self.ui.button_edit_time.clicked.connect(lambda:self.editPillName("time"))

    def savePillSummary(self,edit_mode):
        print("mock data :", pill_data)
        #----------- SAVE AND THEN GO TO HOME SCREEN -----------#
        mock_home_screen = MockHomescreen(edit_mode)
        # self.ui.text_screen_name.setText("Home screen")
        widget.addWidget(mock_home_screen)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def editPillName(self, edit_mode):
        mock_home_screen = MockHomescreen(edit_mode)
        widget.addWidget(mock_home_screen)
        if edit_mode == "pill_name" :
            print("ชื่อยา :", pill_data[0]["pill_name"] )
            widget.setCurrentIndex(widget.currentIndex()+1)
        if edit_mode == "total_pills" :
            print("จำนวนเม็ดยาทั้งหมด :", pill_data[0]["total_pills"] )
            widget.setCurrentIndex(widget.currentIndex()+1)
        if edit_mode == "amount_pill" :
            print("จำนวนเม็ดยาที่ต้องทาน :", pill_data[0]["amount_pill"] )
            widget.setCurrentIndex(widget.currentIndex()+1)
        if edit_mode == "time" :
            print("เวลาทานยา :", pill_data[0]["times"][0] )
            widget.setCurrentIndex(widget.currentIndex()+1)


class MockHomescreen(QDialog):
    def __init__(self, edit_mode):
        super().__init__()
        self.edit_mode = edit_mode
        self.ui = Ui_home_screen() 
        self.ui.setupUi(self)
        self.ui.text_screen_name.setText("Home screen")
        if edit_mode == "pill_name" :
            self.ui.text_screen_name.setText("pill name")
        if edit_mode == "total_pills" :
            self.ui.text_screen_name.setText("total pills screen")
        if edit_mode == "amount_pill" :
            self.ui.text_screen_name.setText("amount_pill screen")
        if edit_mode == "time" :
            self.ui.text_screen_name.setText("time screen")


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