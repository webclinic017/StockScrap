import sys
import pandas as pd
from PyQt5.QtWidgets import QApplication, QTableView
from PyQt5.QtCore import QAbstractTableModel, Qt


df = pd.read_json(r'C:\Users\Gavin\Desktop\FinData\U.S\A\AAPL\IncomeStatement', typ='frame')

# Pandas to PyQt5 Readable
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
    


if __name__ == '__main__':
    app = QApplication(sys.argv)
    model = PandasModel(df)
    view = QTableView()
    view.setModel(model)
    view.resize(1200, 800)
    view.show()
    sys.exit(app.exec_())