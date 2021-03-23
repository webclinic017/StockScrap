import sys
import time
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QThread, pyqtSignal, pyqtSlot, QObject
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
#  Intrinsic Widget
################################################################################
class IntrinsicUI(QWidget):
    def __init__(self, ticker, DB_PATH, est_years, exp_ror, per_growth, margin, dl_option):
        super().__init__()

        # Attributes
        # intrinsic_parameters = (ticker, DB_PATH, est_years, exp_ror, per_growth, margin, dl_option)
        self.ticker = ticker
        self.DB_PATH = DB_PATH
        self.est_years = est_years
        self.exp_ror = exp_ror
        self.per_growth = per_growth
        self.margin = margin
        self.dl_option = dl_option

        self.parameters = (self.ticker, self.DB_PATH, self.est_years, self.exp_ror, self.per_growth, self.margin, self.dl_option)

        # ==> Load External UI
        self.ui = uic.loadUi('intrinsic.ui', self)

        # ==> Remove Standard bars
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # ==> Find LineEdits
        self.edit_ticker = self.findChild(QtWidgets.QLineEdit, 'edit_ticker')
        self.edit_intrinsic = self.findChild(QtWidgets.QLineEdit, 'edit_intrinsic')
        self.edit_buyprice = self.findChild(QtWidgets.QLineEdit, 'edit_buyprice')

        # ==> Find PushButtons
        self.bn_quit = self.findChild(QtWidgets.QPushButton, 'bn_quit')
        self.bn_quit.clicked.connect(self.signal_quit)
        
        #######################
        # Intrinsic Thread
        #######################
        
        # ==> Create Intrinsic Worker and thread
        self.obj_intrinsic = IntrinsicWorker(*self.parameters)
        self.thread_intrinsic = QThread()

        # ==> Move the Worker Object to the Thread Object
        self.obj_intrinsic.moveToThread(self.thread_intrinsic)

        # ==> Connect Worker finished to UI, to quit thread when finished is emitted.
        self.obj_intrinsic.finished.connect(self.thread_intrinsic.quit)

        # ==> Connect Thread starting signal to run intrinsic method
        self.thread_intrinsic.started.connect(self.obj_intrinsic.start_intrinsic)

    def set_ticker(self, ticker):
        return self.edit_ticker.setProperty("value", ticker)
    
    def set_value(self, val):
        self.edit_intrinsic.setProperty("value", val)
        self.edit_buyprice.setProperty("value", val * self.margin)

    def signal_quit(self):
        return QApplication.instance().quit()
################################################################################
#  Intrinsic Worker Classes
################################################################################
class IntrinsicWorker(QObject):

    # Thread emits / outputs
    finished = pyqtSignal()


    # Initialize Attribute types for Intrinsic Class
    def __init__(self, ticker, DB_PATH, est_years, exp_ror, per_growth, margin, dl_option):
        super().__init__()
        self.ticker = ticker
        self.DB_PATH = DB_PATH
        self.est_years = est_years
        self.exp_ror = exp_ror
        self.per_growth = per_growth
        self.margin = margin
        self.dl_option = dl_option
    
    @pyqtSlot() # Mark connector as pyqtSlot
    def start_intrinsic(self):
        i = Intrinsic()
        i.intrinsic(self.ticker, self.DB_PATH, self.est_years, self.exp_ror, self.per_growth, self.margin, self.dl_option)

        # Emit when finished intrinsic
        self.finished.emit()


################################################################################
#  Open Window
################################################################################
def window():
    app = QApplication(sys.argv)
    ui = IntrinsicUI()
    ui.show()
    app.exec_()

window()