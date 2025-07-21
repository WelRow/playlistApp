import sys
from requests import get
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QImage, QPixmap
from qt_widgets.LoginWindowV1 import Ui_LoginWindow
from spotify_backend.spotifyapi import SpotifyClient
from qt_widgets.PlaylistCardWidgetV1 import CustomPlaylistCard

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_LoginWindow()
        self.ui.setupUi(self)
        self.connectSignals()
        self.playlists_loaded = False
        
    def connectSignals(self):
        self.ui.loginButton.clicked.connect(self.handleLogin)
        self.ui.homeButton.clicked.connect(self.showHomePage)
        self.ui.playlistButton.clicked.connect(self.showPlaylistPage)

    def handleLogin(self):
        # Spotify Authentication
        self.sp = SpotifyClient()
        self.ui.stackedWidget.setCurrentIndex(1)
    
    def showHomePage(self):
        self.ui.stackedWidget_2.setCurrentIndex(0)

    def showPlaylistPage(self):
        self.ui.stackedWidget_2.setCurrentIndex(1)

        if not self.playlists_loaded:
            print("Loading playlists for the first time...")
            self.loadPlaylists()
            self.playlists_loaded = True
    
    def loadPlaylists(self):
        targetLayout = self.ui.gridLayout_3

        # If there's playlists already loaded, they will be deleted
        while targetLayout.count():
            child = targetLayout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
        
        playlistData = self.sp.getCurrentUserPlaylists()

        itemsPerRow = 4
        for i, playlist in enumerate(playlistData['items']):
            row = i // itemsPerRow
            col = i % itemsPerRow

            card = CustomPlaylistCard()
            card.setData(name=playlist['name'], image_url=playlist['images'][0]['url'])

            targetLayout.addWidget(card, row, col)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())