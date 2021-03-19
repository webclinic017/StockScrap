import sys
import webbrowser
import time
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QThread, pyqtSignal
from PyQt5.QtGui import QColor
from PyQt5 import uic
from Download import Downloader
from Intrinsic import Intrinsic


################################################################################
#  PyQt5 Settings
################################################################################
# ---- ==> Enable high res settings
if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

################################################################################
#  Download Widget
################################################################################
class DownloadUI(QWidget):
    def __init__(self):
        super().__init__()

        # ==> Load UI from QtDesigner
        self.ui = uic.loadUi('download.ui', self)  
        
        # Remove Standard bars
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # ==> Find progress bar widget
        self.prog_progbar = self.findChild(QtWidgets.QProgressBar, 'prog_progbar')
        self.prog_progbar.setProperty("value", 0)

        # ==> Find label
        self.lb_stockName = self.findChild(QtWidgets.QLabel, 'lb_stockName')

        self.start_progress_bar()



    def set_value(self, value):
        return self.prog_progbar.setProperty("value", value)

    def set_ticker(self, ticker):
        return self.lb_stockName.setProperty("text", f'TICKER: {ticker}')

    def start_progress_bar(self):
        self.thread = ProgThread()
        self.thread.change_value.connect(self.set_value)
        self.thread.start()

    def end_progress_bar(self):
        self.thread = ProgThread()
        self.thread.quit()
################################################################################
#  QThread Class
################################################################################
class ProgThread(QThread):

    change_value = pyqtSignal(int)
    
    def run(self):
        count = 0
        while count < 99:
            count+=1

            time.sleep(0.1)
            self.change_value.emit(count)        

################################################################################
#  Open Window
################################################################################
def window():
    app = QApplication(sys.argv)
    ui = DownloadUI()
    ui.show()
    app.exec_()

window()
