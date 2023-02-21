from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton
from PyQt5 import uic, QtWidgets, QtCore, QtGui

# Not needed if using PyQt6
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

import sys


class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        # Load the ui file
        uic.loadUi("schedgui.ui", self)

        # Show the app
        self.show()


# Initialize the app
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()
