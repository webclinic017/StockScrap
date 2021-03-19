import sys
import webbrowser
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QThread, pyqtSignal
from PyQt5.QtGui import QColor
from PyQt5 import uic
from Download import Downloader
from Intrinsic import Intrinsic

################################################################################
#  Globals
################################################################################
counter = 0

################################################################################
#  PyQt5 Settings
################################################################################
# ---- ==> Enable high res settings
if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

################################################################################
#  SplashScreen Widget
################################################################################
# --- ==> Import SplashScreen python file
from ui_Circular_Splash import Ui_SplashScreen

# --- ==> Import Download python file
from ui_download import DownloadUI

class SplashScreen(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_SplashScreen() # set UI ==> Ui_SplashScreen class
        self.ui.setupUi(self)

        # Set intial progress bar to 0
        self.progress_bar_val(0)

        # Remove Standard bars
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # Apply Drop Shadow Effect
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 100))
        self.ui.circularBg.setGraphicsEffect(self.shadow)
        
        # Get QTimer
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        self.timer.start(35)
        

    # Function to calculate progress %
    def progress(self):
        global counter
        value = counter

        # HTML Text Percentage
        htmlText = '''<html><head/><body><p><span style=" font-size:20pt; color:#ffffff;">{VALUE}</span><span style=" color:#ffffff; vertical-align:super;">%</span></p></body></html>'''

        # REPLACE VALUE
        newHtmlText = htmlText.replace("{VALUE}", str(int(value)))

        # APPLY NEW PERCENTAGE TEXT
        self.ui.labelPercentage.setText(newHtmlText)

        # SET VALUE to progres bar
        self.progress_bar_val(value)

        if value >= 100 : value = 1.000

        # Close Splash Screen and open APP
        if counter > 100:
            # Stop Timer
            self.timer.stop()

            # Launch main window
            self.launch_main()

            # Close splash scren
            self.close()

            
        # Increase Counter
        counter += 1

    # Fuction for progress bar value
    def progress_bar_val(self, value):
        # ProgressBar StyleSheet Base
        styleSheet = '''
        QFrame{
	border-radius: 150px;
	background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:{STOP_1} rgba(255,0,127,0), stop:{STOP_2} rgba(85, 170, 255, 255));
    }

        '''

        # Get ProgressBar Value, then convert it to float and invert values.
        # Stop values from 1.000 to 0.000
    
        progress = (100 - value) / 100.0

        # Get new values of STOP.
        STOP_1 = progress - 0.001
        STOP_2 = progress

        # Fix stop_errors, then convert into string values to fit QFrame
        if STOP_1 < 0: STOP_1 = 0.0001
        if STOP_2 < 0: STOP_2 = 0.0002

        STOP_1 = str(STOP_1)
        STOP_2 = str(STOP_2)

        # Set values to new stylesheet
        newStyleSheet = styleSheet.replace("{STOP_1}", STOP_1).replace("{STOP_2}", STOP_2)

        # Apply stylesheet with new values
        self.ui.circularProgress.setStyleSheet(newStyleSheet)
        return STOP_1

    def launch_main(self):
        self.main_ui = UI()
        self.main_ui.show()

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
        self.bn_botmenu_intrinsic.clicked.connect(self.signal_intrinsic)

        #---- ==> fr_download
        self.bn_dl_dbbrowse = self.findChild(QtWidgets.QPushButton, 'bn_dl_dbbrowse')
        self.bn_dl_dbbrowse.clicked.connect(self.signal_db_path)
        self.bn_dl_csvbrowse = self.findChild(QtWidgets.QPushButton, 'bn_dl_csvbrowse')
        self.bn_dl_csvbrowse.clicked.connect(self.signal_csv_path)

        #---- ==> fr_header

        #---- ==> fr_intrinsic
        self.bn_int_dbbrowse = self.findChild(QtWidgets.QPushButton, 'bn_int_dbbrowse')
        self.bn_int_dbbrowse.clicked.connect(self.signal_db_path)
        
        #---- ==> fr_topmenu
        self.bn_topmenu_github = self.findChild(QtWidgets.QPushButton, 'bn_topmenu_github')
        self.bn_topmenu_github.clicked.connect(self.signal_github)
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
        return webbrowser.open('https://github.com/rawsashimi1604/StockScrap')

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
        d_status = d.download(type_=type_option, DB_PATH=DB_PATH, ticker=ticker, csv=CSV_PATH, download=download_option, buffer=1)

        return d_status


    def signal_intrinsic(self):
        # ==> Get Line Edit inputs
        # ---- ==> DB_PATH:
        DB_PATH = self.edit_int_dbpath.text()

        # ---- ==> Ticker:
        ticker = self.edit_int_ticker.text()

        # ---- ==> Margin of Safety:
        margin = float(self.edit_int_margin.text())

        # ---- ==> Estimated Years:
        est_years = int(self.edit_int_estyears.text())

        # ---- ==> Expected Rate Of Return:
        exp_ror = float(self.edit_int_expror.text())

        # ---- ==> Perpetual Growth:
        per_growth = float(self.edit_int_pergrowth.text())

        # ==> Get ComboBox inputs
        # ---- ==> Download true?:
        int_options = {
            "True": True,
            "False": False
        }
        dl_option = int_options.get(self.combo_int_downloadopt.currentText())
        
        # ==> Run Intrinsic Function
        i = Intrinsic()
        i.intrinsic(ticker=ticker, DB_PATH=DB_PATH, estimated_yrs=est_years, expected_rate_return=exp_ror,perpetual_growth=per_growth,margin_safety=margin,download=dl_option)

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
        
        # ==> Find label
        self.lb_stockName = self.findChild(QtWidgets.QLabel, 'lb_stockName')

    def set_value(self, value):
        return self.prog_progbar.setProperty("value", value)

    def set_ticker(self, ticker):
        return self.lb_stockName.setProperty("text", f'TICKER: {ticker}')

    def start_progress_bar(self):
        self.thread = DLThread()
        self.thread.change_value.connect(self.set_value)
        self.thread.start()
        
################################################################################
#  QThread Class
################################################################################
class DLThread(QThread):

    change_value = pyqtSignal(int)
    
    def run(self):
        count = 0
        while count < 100:
            count+=1

            time.sleep(0.5)
            self.change_value.emit(count)

            

################################################################################
#  Open Window
################################################################################
def window():
    app = QApplication(sys.argv)
    ui = SplashScreen()
    ui.show()
    app.exec_()

window()
