import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout
from Download import Downloader

# Create UI Object
class UI(QWidget):
    def __init__(self):
        super().__init__()

        # Initialize UI
        self.setGeometry(300,300,300,150)
        self.setWindowTitle('StockScrap')

        # Create buttons
        download_button = QPushButton("Download")
        quit_button = QPushButton("Quit")

        # Quit button usage
        quit_button.clicked.connect(QApplication.instance().quit)

        # Create and align layouts
        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(download_button)
        hbox.addWidget(quit_button)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        # Add hbox to vbox, then set layout.
        self.setLayout(vbox)


    



app = QApplication(sys.argv)
ui = UI()
ui.show()
app.exec_()

