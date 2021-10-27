import sys
from gen.gen_pill_summary_screen import *
from PyQt5.QtWidgets import QDialog, QApplication, QWidget
from mock.pill_data import pill_data

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

    def savePillSummary(self):
        print("mock data :", pill_data)

        
        

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