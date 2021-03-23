import sys
import pandas as pd
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QThread, pyqtSignal, pyqtSlot, QObject, QAbstractTableModel
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
#  Open Window
################################################################################
def window():
    app = QApplication(sys.argv)
    ui = ViewUI()
    ui.show()
    app.exec_()

window()
