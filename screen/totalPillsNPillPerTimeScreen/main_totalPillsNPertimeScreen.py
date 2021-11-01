import sys
from gen.gen_total_pills_screen import *
from gen.gen_amount_pill_per_time_screen import *
from PyQt5.QtWidgets import QDialog, QApplication, QWidget
from shared.gen_mock_screen import *

class TotalPillsScreen(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_total_pills() 
        self.ui.setupUi(self)
        #========= set max-min of total pills =========#
        self.ui.slider_total_pills.setMaximum(30)
        self.ui.slider_total_pills.setMinimum(0)
        self.ui.slider_total_pills.valueChanged.connect(self.updateSliderTotalPills)
        self.ui.button_skip_total_pills.clicked.connect(self.goToAmountPillPerTimeScreen)
        self.ui.button_save_total_pills.clicked.connect(self.goToAmountPillPerTimeScreen)
        
    def updateSliderTotalPills(self,count_of_total_pills):
        self.ui.lcdNumber.display(count_of_total_pills)
        print("[total of pills] : ",count_of_total_pills)
        self.total_pills = [{
            "id": 1,
            "total_pills": count_of_total_pills,
        }]

    def goToAmountPillPerTimeScreen(self):
        pill_per_time_screen = AmountPillPerTimeScreen(self.total_pills)
        widget.addWidget(pill_per_time_screen)
        widget.setCurrentIndex(widget.currentIndex()+1)

class AmountPillPerTimeScreen(QDialog):
    def __init__(self,total_pills):
        super().__init__()
        self.ui = Ui_amount_pill_per_time() 
        self.ui.setupUi(self)
        #========= set max-min of total pills =========#
        self.ui.slider_amount_pill_per_time.setMaximum(10)
        self.ui.slider_amount_pill_per_time.setMinimum(0)
        self.ui.slider_amount_pill_per_time.valueChanged.connect(self.updateSliderPillPerTime)
        self.ui.button_next.clicked.connect(self.nextPage)

        self.total_pills = total_pills
        print("รายละเอียดข้อมูลยา",self.total_pills)  
          
        
    def updateSliderPillPerTime(self,amount_of_pill_per_time):
        self.ui.lcdNumberPillPerTime.display(amount_of_pill_per_time)
        print("[amount of pill per time] : ",amount_of_pill_per_time)
        self.amount_pill = [{
            "amount_pill": amount_of_pill_per_time
        }]
        #=========add amount pill to array object=========#
        self.total_pills[0]['amount_pill'] = amount_of_pill_per_time
        

    def nextPage(self):
        print("บันทึกจำนวนยาที่ต้องทานเเต่ละมื้อ = ", self.total_pills)

if __name__ == "__main__":
     app = QApplication(sys.argv)
     screen = TotalPillsScreen()
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