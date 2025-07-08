import sys
from requests import get
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QImage, QPixmap
from qt_widgets.LoginWindowV1 import Ui_LoginWindow
from spotify_backend import spotifyapi

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_LoginWindow()
        self.ui.setupUi(self)
        

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())