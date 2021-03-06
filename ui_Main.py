import sys
import webbrowser
import time
import pandas as pd
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QThread, pyqtSignal, pyqtSlot, QObject, QAbstractTableModel
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
        self.timer.start(5)
        

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
        self.bn_topmenu_view = self.findChild(QtWidgets.QPushButton, 'bn_topmenu_view')
        self.bn_topmenu_view.clicked.connect(self.signal_view)
        self.bn_topmenu_how = self.findChild(QtWidgets.QPushButton, 'bn_topmenu_how')
        self.bn_topmenu_how.clicked.connect(self.signal_how)

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

    def signal_view(self):
        self.ViewUI = ViewUI()
        self.ViewUI.show()
    
    def signal_how(self):
        self.HowUI = HowUI()
        self.HowUI.show()

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

    def params_download(self):
        # ==> Get Line Edit inputs
        # ---- ==> DB_PATH:
        DB_PATH = self.edit_dl_dbpath.text()
        if DB_PATH == '':
            DB_PATH == None

        # ---- ==> CSV_PATH:
        CSV_PATH = self.edit_dl_csvpath.text()
        if CSV_PATH == '':
            CSV_PATH = None

        # ---- ==> Ticker Symbol:
        ticker = self.edit_dl_ticker.text()
        if ticker == '':
            ticker = None

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

        buffer = 1
        download_parameters = (type_option, DB_PATH, ticker, CSV_PATH, download_option, buffer)

        return download_parameters

    def signal_download(self):
        self.download_UI = DownloadUI(*self.params_download())
        self.download_UI.show()

    def signal_intrinsic(self):
        parameters = self.params_intrinsic()

        if parameters[-1] == False:
            self.intrinsic_UI = IntrinsicUI(*parameters)
            self.intrinsic_UI.show()
        
        elif parameters[-1] == True:
            self.download_UI = DownloadUI("string", parameters[1], parameters[0], None, 'ALL', 1)
            self.download_UI.show()
            self.intrinsic_UI = IntrinsicUI(*parameters)
            self.intrinsic_UI.show()

    def params_intrinsic(self):
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

        intrinsic_parameters = (ticker, DB_PATH, est_years, exp_ror, per_growth, margin, dl_option)
        return intrinsic_parameters


################################################################################
#  Download Widget
################################################################################      
class DownloadUI(QWidget):
    def __init__(self, type_option, DB_PATH, ticker, CSV_PATH, download_option, buffer):
        super().__init__()

        # Attributes
        self.type_option = type_option
        self.DB_PATH = DB_PATH
        self.ticker = ticker
        self.CSV_PATH = CSV_PATH
        self.download_option = download_option
        self.buffer = buffer

        self.parameters = (self.type_option, self.DB_PATH, self.ticker, self.CSV_PATH, self.download_option, self.buffer)
    
        # ==> Load UI from QtDesigner
        self.ui = uic.loadUi('download.ui', self)
        
        # ==> Remove Standard bars
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # ==> Find progress bar widget
        self.prog_progbar = self.findChild(QtWidgets.QProgressBar, 'prog_progbar')
        self.prog_progbar.setProperty("value", 0)

        # ==> Find label
        self.lb_stockName = self.findChild(QtWidgets.QLabel, 'lb_stockName')
        if self.type_option == "string":
            self.set_ticker(self.parameters[2])
        elif self.type_option == "csv":
            self.lb_stockName.setText('Downloading CSV!')

        #######################
        # Progress Bar Thread
        #######################
        # length of CSV
        self.numline = 1
        if self.type_option == "csv":
            file_ = open(self.CSV_PATH)
            self.numline = len(file_.readlines())

        # ==> Create Loading Worker and Thread
        self.obj_loader = LoadingWorker(self.type_option, self.numline)
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

        # ==> Create Download Worker and Thread, input Downloader.download args (unpacked from tuple)
        self.obj_download = DownloadWorker(*self.parameters)
        self.thread_download = QThread()

        # ==> Move the Worker Object to the Thread Object
        self.obj_download.moveToThread(self.thread_download)

        # ==> Connect Worker Finished to UI, to quit thread when finished is emitted.
        self.obj_download.finished.connect(self.thread_download.quit)

        # ==> Connect Thread error signal to run error method
        self.obj_download.error.connect(self.error)

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

    def error(self, error_signal):
        if error_signal == "Yes":
            self.error_dialog = QtWidgets.QErrorMessage()
            self.error_dialog.showMessage('''
Error Retrieving Ticker Data, please check ticker.
Please note that StockScrap only works with listed US Equities.
''')

    def finished(self):
        # When download is finished, I want to stop loader Thread, and set progress bar to finish, the time sleep 0.1 secs, then self.close
        self.thread_loader.quit()
        self.thread_download.quit()
        self.set_value(100)
        time.sleep(0.5)
        self.close()

################################################################################
#  Download Worker Classes
################################################################################
# Loading Progress Bar Class
class LoadingWorker(QObject):

    def __init__(self, download_type, len_):
        super().__init__()
        self.download_type = download_type
        self.len_ = len_

    # Thread emits / outputs
    finished = pyqtSignal()
    int_val = pyqtSignal(int)
    
    @pyqtSlot() # Mark connector as pyqtSlot
    def procCounter(self):
        # For loop to add value to counter
        if self.download_type != "csv":
            counter = 0
            while counter < 100:
                time.sleep(0.2)
                counter += 1
                self.int_val.emit(counter) # Emit counter every iteration
        
        if self.download_type == "csv":
            counter = 0
            while counter < 100:
                time.sleep(0.2 * self.len_)
                counter += 1
                self.int_val.emit(counter) # Emit counter every iteration

        self.finished.emit() # Emit when finished loop

# Loading DL Class
class DownloadWorker(QObject):

    # Thread emits / outputs
    finished = pyqtSignal()
    error = pyqtSignal(str)

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
        error = "No"
        try:
            d = Downloader()
            d.download(type_ = self.type_, DB_PATH = self.DB_PATH, ticker = self.ticker, csv = self.csv, download = self.download, buffer = self.buffer)

        except (AttributeError, ValueError):
            error = "Yes"

        # Emit when finished downloading
        self.error.emit(error)
        self.finished.emit()

################################################################################
#  Intrinsic Widget
################################################################################
class IntrinsicUI(QWidget):
    def __init__(self, ticker, DB_PATH, est_years, exp_ror, per_growth, margin, dl_option):
        super().__init__()
        
        # Attributes
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
        
        # ==> Set Ticker
        self.set_ticker(self.ticker)

        #######################
        # Intrinsic Thread
        #######################
        
        # ==> Create Intrinsic Worker and thread
        self.obj_intrinsic = IntrinsicWorker(*self.parameters)
        self.thread_intrinsic = QThread()

        # ==> Move the Worker Object to the Thread Object
        self.obj_intrinsic.moveToThread(self.thread_intrinsic)

        # ==> Send intrinsic therad emit to set_value
        self.obj_intrinsic.intrinsic_val.connect(self.set_value)

        # ==> Connect Worker finished to UI, to quit thread when finished is emitted.
        self.obj_intrinsic.finished.connect(self.thread_intrinsic.quit)

        # ==> Connect Thread starting signal to run intrinsic method
        self.thread_intrinsic.started.connect(self.obj_intrinsic.start_intrinsic)

        # ==> Start the Thread
        self.thread_intrinsic.start()

    def set_ticker(self, ticker):
        return self.edit_ticker.setText(ticker)
    
    def set_value(self, val):
        self.edit_intrinsic.setText(str(val/self.margin))
        self.edit_buyprice.setText(str(val))

    def signal_quit(self):
        return self.close()
    

################################################################################
#  Intrinsic Worker Classes
################################################################################
class IntrinsicWorker(QObject):

    # Thread emits / outputs
    finished = pyqtSignal()
    intrinsic_val = pyqtSignal(float)

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
        val = i.intrinsic(self.ticker, self.DB_PATH, self.est_years, self.exp_ror, self.per_growth, self.margin, self.dl_option)

        # Emit when finished intrinsic
        self.intrinsic_val.emit(val)
        self.finished.emit()
        
################################################################################
#  View Widget
################################################################################
class ViewUI(QWidget):
    def __init__(self):
        super().__init__()

        # ==> Load External UI
        self.ui = uic.loadUi('view.ui', self)

        # ==> Remove Standard bars
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # ==> Find Line Edits
        self.edit_filepath = self.findChild(QtWidgets.QLineEdit, 'edit_filepath')

        # ==> Find PushButtons
        self.bn_filepath = self.findChild(QtWidgets.QPushButton, 'bn_filepath')
        self.bn_filepath.clicked.connect(self.signal_filepath)
        self.bn_view = self.findChild(QtWidgets.QPushButton, 'bn_view')
        self.bn_view.clicked.connect(self.signal_view)
        self.bn_close = self.findChild(QtWidgets.QPushButton, 'bn_close')
        self.bn_close.clicked.connect(self.signal_close)

    def signal_close(self):
        return self.close()

    def signal_filepath(self):
        file_path = QFileDialog.getOpenFileName(self, 'Select File PATH', "", "All files (*.*)" )
        self.edit_filepath.setText(file_path[0])
        return file_path

    def signal_view(self):
        df = pd.read_json(self.edit_filepath.text())
        self.model = PandasModel(df)
        self.view = QTableView()
        self.view.setModel(self.model)
        self.view.setWindowTitle("DataView")
        self.view.resize(1200, 700)
        self.view.show()


################################################################################
#  PandasModel
################################################################################
class PandasModel(QAbstractTableModel):

    def __init__(self, data):
        super(PandasModel, self).__init__()
        self._data = data

    def data(self, index, role):
        if role == Qt.DisplayRole:
            value = self._data.iloc[index.row(), index.column()]
            return str(value)

    def rowCount(self, index):
        return self._data.shape[0]

    def columnCount(self, index):
        return self._data.shape[1]

    def headerData(self, section, orientation, role):
        # section is the index of the column/row.
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return str(self._data.columns[section])

            if orientation == Qt.Vertical:
                return str(self._data.index[section])

################################################################################
#  How Widget
################################################################################
class HowUI(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi('usage.ui', self)
        # ==> Remove Standard bars
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        # ==> Find PushButton
        self.bn_quit = self.findChild(QtWidgets.QPushButton, 'bn_quit')
        self.bn_quit.clicked.connect(self.signal_quit)

        # ==> Find 
    def signal_quit(self):
        self.close()

################################################################################
#  Open Window
################################################################################
def window():
    app = QApplication(sys.argv)
    ui = SplashScreen()
    ui.show()
    app.exec_()

if __name__ == "__main__":
    window()
