from Download import Downloader
import sys
import time
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QObject, Qt, QThread, pyqtSignal, pyqtSlot
from PyQt5.QtGui import QColor
from PyQt5 import uic


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
        
        # ==> Remove Standard bars
        # self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        # self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # ==> Find progress bar widget
        self.prog_progbar = self.findChild(QtWidgets.QProgressBar, 'prog_progbar')
        self.prog_progbar.setProperty("value", 0)

        # ==> Find label
        self.lb_stockName = self.findChild(QtWidgets.QLabel, 'lb_stockName')
        self.set_ticker('AAPL')
        #######################
        # Progress Bar Thread
        #######################
        # ==> Create Loading Worker and Thread
        self.obj_loader = LoadingWorker()
        self.thread_loader = QThread()

        # ==> Move the Worker Object to the Thread Object
        self.obj_loader.moveToThread(self.thread_loader)

        # ==> Connect Worker Int Value (for loop) to progress bar value
        self.obj_loader.int_val.connect(self.set_value)

        # ==> Connect Worker Finished (for loop) to UI, to quit threadd when finished is emitted.
        self.obj_loader.finished.connect(self.thread_loader.quit)
        
        # ==> Connect Thread starting signal to run procCounter method
        self.thread_loader.started.connect(self.obj_loader.procCounter)
        # ---------------------------------------------------------
        
        #######################
        # Downloading Thread
        #######################
        # ==> Create Loading Worker and Thread
        self.obj_download = DownloadWorker("string", r'C:\Users\Dennis Loo.000\Desktop\FinData', 'AAPL', None, 'ALL', 1)
        self.thread_download = QThread()

        # ==> Move the Worker Object to the Thread Object
        self.obj_download.moveToThread(self.thread_download)

        # ==> Connect Worker Finished (for loop) to UI, to quit thread when finished is emitted.
        self.obj_download.finished.connect(self.thread_download.quit)

        # ==> Connect Thread starting signal to run download method
        self.thread_download.started.connect(self.obj_download.start_download)

        # ==> When thread is finished, run finished method
        self.obj_download.finished.connect(self.finished)
        # ---------------------------------------------------------

        # ==> Start the Threads
        self.thread_loader.start()
        self.thread_download.start()

    def set_value(self, value):
        return self.prog_progbar.setProperty("value", value)

    def set_ticker(self, ticker):
        return self.lb_stockName.setProperty("text", f'TICKER: {ticker}')

    def finished(self):
        # When download is finished, I want to stop loader Thread, and set progress bar to finish, the time sleep 0.1 secs, then self.close
        self.thread_loader.quit()
        self.set_value(100)
        time.sleep(5)
        self.close()

################################################################################
#  Worker Classes
################################################################################
# Loading Progress Bar Class
class LoadingWorker(QObject):

    # Thread emits / outputs
    finished = pyqtSignal()
    int_val = pyqtSignal(int)
    
    @pyqtSlot() # Mark connector as pyqtSlot
    def procCounter(self):
        # For loop to add value to counter
        counter = 0
        while counter < 100:
            time.sleep(0.2)
            counter += 1
            self.int_val.emit(counter) # Emit counter every iteration
        
        self.finished.emit() # Emit when finished loop

# Loading DL Class
class DownloadWorker(QObject):

    # Thread emits / outputs
    finished = pyqtSignal()

    # Initialize Attribute types for Download Class
    def __init__(self, type_, DB_PATH, ticker, csv, download, buffer):
        super().__init__()
        self.type_ = type_
        self.DB_PATH = DB_PATH
        self.ticker = ticker
        self.csv = csv
        self.download = download
        self.buffer = buffer

    @pyqtSlot() # Mark connector as pyqtSlot
    def start_download(self):
        d = Downloader()
        d.download(type_ = self.type_, DB_PATH = self.DB_PATH, ticker = self.ticker, csv = self.csv, download = self.download, buffer = self.buffer)

        # Emit when finished downloading
        self.finished.emit() 

################################################################################
#  Open Window
################################################################################
def window():
    app = QApplication(sys.argv)
    ui = DownloadUI()
    ui.show()
    app.exec_()

window()
