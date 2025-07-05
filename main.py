import sys
from requests import get
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QImage, QPixmap
from qt_widgets.playlistAlbumTest import Ui_MainWindow
from spotify_backend import spotifyapi
from spotify_backend import spotifyapi

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui._submitButton.clicked.connect(self.searchAlbum)
        
    def searchAlbum(self):
        albumName = self.ui._albumField.text()
        albumLink = spotifyapi.searchForAlbumCover(albumName)

        albumImage = QImage()
        albumImage.loadFromData(get(albumLink).content)

        self.ui._image.setPixmap(QPixmap(albumImage))

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())