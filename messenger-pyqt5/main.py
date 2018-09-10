import sys
from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSignal
import requests
from ui.login import Ui_LoginWindow
from ui.main import Ui_MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QMainWindow()
    main_ui = Ui_MainWindow()
    main_ui.login()
    sys.exit(app.exec_())