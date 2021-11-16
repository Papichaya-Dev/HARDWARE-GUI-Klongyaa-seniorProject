import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QStackedWidget
from shared.data.mock.pill_channel_datas import pill_channel_datas

# Screen UI
from screen.homeScreen.main_homeScreen import HomeScreen

if __name__ == "__main__":
     app = QApplication(sys.argv)
     screen = HomeScreen(pill_channel_datas)
     widget = QStackedWidget()
     widget.setWindowTitle("GUI - KLONG_YAA")
     widget.addWidget(screen)
     widget.setFixedWidth(1024)
     widget.setFixedHeight(600)
     widget.show()
     sys.exit(app.exec_())
