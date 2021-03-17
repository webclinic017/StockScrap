import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor
from PyQt5 import uic
from Download import Downloader

################################################################################
#  Main Widget
################################################################################
# Create UI Object
class UI(QMainWindow):
    def __init__(self):
        super().__init__()

        # Load UI from QtDesigner
        self.ui = uic.loadUi('stockscrap.ui', self)

        # Remove standard bars
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        ################################################################################
        #  PushButtons
        ################################################################################
        #---- ==> fr_botmenu
        self.bn_botmenu_download = self.findChild(QtWidgets.QPushButton, 'bn_botmenu_download')
        self.bn_botmenu_download.clicked.connect(self.signal_download)
        self.bn_botmenu_intrinsic = self.findChild(QtWidgets.QPushButton, 'bn_botmenu_intrinsic')

        #---- ==> fr_download
        self.bn_dl_dbbrowse = self.findChild(QtWidgets.QPushButton, 'bn_dl_dbbrowse')
        self.bn_dl_dbbrowse.clicked.connect(self.signal_db_path)
        self.bn_dl_csvbrowse = self.findChild(QtWidgets.QPushButton, 'bn_dl_csvbrowse')
        self.bn_dl_csvbrowse.clicked.connect(self.signal_csv_path)

        #---- ==> fr_header

        #---- ==> fr_intrinsic
        self.bn_int_dbbrowse = self.findChild(QtWidgets.QPushButton, 'bn_int_dbbrowse')
        self.bn_int_dbbrowse.clicked.connect(self.signal_db_path)
        self.bn_int_csvbrowse = self.findChild(QtWidgets.QPushButton, 'bn_int_csvbrowse')

        #---- ==> fr_topmenu
        self.bn_topmenu_github = self.findChild(QtWidgets.QPushButton, 'bn_topmenu_github')
        self.bn_topmenu_quit = self.findChild(QtWidgets.QPushButton, 'bn_topmenu_quit')
        self.bn_topmenu_quit.clicked.connect(self.signal_quit)

        ################################################################################
        #  LineEdits (Input Fields)
        ################################################################################
        #---- ==> fr_botmenu

        #---- ==> fr_download
        self.edit_dl_dbpath = self.findChild(QtWidgets.QLineEdit, 'edit_dl_dbpath')
        self.edit_dl_csvpath = self.findChild(QtWidgets.QLineEdit, 'edit_dl_csvpath')
        self.edit_dl_ticker = self.findChild(QtWidgets.QLineEdit, 'edit_dl_ticker')

        #---- ==> fr_header

        #---- ==> fr_intrinsic
        self.edit_int_dbpath = self.findChild(QtWidgets.QLineEdit, 'edit_int_dbpath')
        self.edit_int_ticker = self.findChild(QtWidgets.QLineEdit, 'edit_int_ticker')
        self.edit_int_margin = self.findChild(QtWidgets.QLineEdit, 'edit_int_margin')
        self.edit_int_estyears = self.findChild(QtWidgets.QLineEdit, 'edit_int_estyears')
        self.edit_int_expror = self.findChild(QtWidgets.QLineEdit, 'edit_int_expror')
        self.edit_int_pergrowth = self.findChild(QtWidgets.QLineEdit, 'edit_int_pergrowth')

        #---- ==> fr_topmenu

        ################################################################################
        #  ComboBoxes (Input Fields)
        ################################################################################
        #---- ==> fr_botmenu

        #---- ==> fr_download
        self.combo_dl_downloadopt = self.findChild(QtWidgets.QComboBox, 'combo_dl_downloadopt')
        self.combo_dl_downloadt = self.findChild(QtWidgets.QComboBox, 'combo_dl_downloadt')
        
        #---- ==> fr_header

        #---- ==> fr_intrinsic
        self.combo_int_downloadopt = self.findChild(QtWidgets.QComboBox, 'combo_int_downloadopt')
        
        #---- ==> fr_topmenu


################################################################################
#  Button Signals
################################################################################
    def signal_quit(self):
        # Quit application
        return QApplication.instance().quit()
    
    def signal_github(self):
        pass

    def signal_db_path(self):
        # Get directory of chosen folder in a string format, then add it into lineEdit field
        db_path = str(QFileDialog.getExistingDirectory(self, 'Select Database PATH'))
        self.edit_dl_dbpath.setText(db_path)
        self.edit_int_dbpath.setText(db_path)
        return db_path
    
    def signal_csv_path(self):
        # Get directory of chosen csv file in a string format, then add it into lineEdit field
        csv_path = QFileDialog.getOpenFileName(self, 'Select CSV PATH', "", "CSV files (*.csv)" )
        self.edit_dl_csvpath.setText(csv_path[0])
        return csv_path

    def signal_download(self):
        # ==> Get Line Edit inputs
        # ---- ==> DB_PATH:
        DB_PATH = self.edit_dl_dbpath.text()
        print(DB_PATH)

        # ---- ==> CSV_PATH:
        CSV_PATH = self.edit_dl_csvpath.text()

        # ---- ==> Ticker Symbol:
        ticker = self.edit_dl_ticker.text()

        #  ==> Get Combo box inputs
        # ---- ==> DL Options:
        dl_options = {
            "All Data": "ALL",
            "Price": "PRICE",
            "Main": "MAIN", 
            "Profile": "PROFILE",
            "Income": "INCOME",
            "Balance": "BALANCE",
            "CashFlow": "CASHFLOW"
        }
        download_option = dl_options.get(self.combo_dl_downloadopt.currentText())

        # ---- ==> DL Type
        dl_type = {
            'Ticker': "string",
            'CSV': "csv"
        }
        type_option = dl_type.get(self.combo_dl_downloadt.currentText())


        # ==> Run Download Function
        d = Downloader()
        d.download(type_=type_option, DB_PATH=DB_PATH, ticker=ticker, csv=CSV_PATH, download=download_option, buffer=1)


    def signal_intrinsic(self):
        pass

################################################################################
#  Open Window
################################################################################
def window():
    app = QApplication(sys.argv)
    ui = UI()
    ui.show()
    app.exec_()

window()
