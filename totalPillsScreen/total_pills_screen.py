import sys
from gen.gen_total_pills_screen import *
from PyQt5.QtWidgets import QDialog, QApplication, QWidget

class MainApp(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_total_pills() 
        self.ui.setupUi(self)
        #========= set max-min of total pills =========#
        self.ui.slider_total_pills.setMaximum(30)
        self.ui.slider_total_pills.setMinimum(0)
        self.ui.slider_total_pills.valueChanged.connect(self.updateSlider)
        
    def updateSlider(self,count_of_total_pills):
        self.ui.lcdNumber.display(count_of_total_pills)
        print("[total of pills] : ",count_of_total_pills)
        
            

if __name__ == "__main__":
     app = QApplication(sys.argv)
     mi_app = MainApp()
     mi_app.show()
     sys.exit(app.exec_())	