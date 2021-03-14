import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5 import uic
from Download import Downloader

################################################################################
#  Main Widget
################################################################################
# Create UI Object
class UI(QWidget):
    def __init__(self):
        super().__init__()

        # Load UI from QtDesigner
        uic.loadUi('stockscrap_ui.ui', self)

        # Find push buttons
        self.quit_button = self.findChild(QtWidgets.QPushButton, 'pushButton_quit')
        self.download_button = self.findChild(QtWidgets.QPushButton, 'pushButton_download')
        self.choosefolder_button = self.findChild(QtWidgets.QPushButton, 'pushButton_choosefolder')

        # Assign button signals
        self.quit_button.clicked.connect(self.signal_quit)
        self.choosefolder_button.clicked.connect(self.signal_folder)
        self.download_button.clicked.connect(self.signal_download)
        
        # Find line edits (input fields)
        self.ticker_input = self.findChild(QtWidgets.QLineEdit, 'lineEdit_chooseticker')
        self.choosefolder_input = self.findChild(QtWidgets.QLineEdit, 'lineEdit_choosefolder')

################################################################################
#  Button Signals
################################################################################
    def signal_quit(self):
        # Quit application
        return QApplication.instance().quit()
    
    def signal_folder(self):
        # Get directory of chosen folder in a string format, then add it into lineEdit field
        folder_name = str(QFileDialog.getExistingDirectory(self, 'Open Folder'))
        self.choosefolder_input.setText(folder_name)
        return folder_name
    
    def signal_download(self):
        # Download file according to parameters
        ticker = self.ticker_input.text()
        folder = self.choosefolder_input.text()
        d = Downloader()
        d.download(type_= "string", ticker=ticker, DB_PATH=folder)
        return None

################################################################################
#  Open Window
################################################################################
def window():
    app = QApplication(sys.argv)
    ui = UI()
    ui.show()
    app.exec_()

window()
