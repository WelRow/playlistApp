"""
    A custom QWidget that uses the PlaylistCard UI blueprint.
"""

from PyQt6.QtWidgets import QWidget
from PyQt6.QtGui import QPixmap, QPainter, QBrush
from PyQt6.QtCore import Qt
from requests import get

from qt_widgets.PlaylistCardV1 import PlaylistCard

class CustomPlaylistCard(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = PlaylistCard()
        self.ui.setupUi(self)

    # Populates the widget's UI elements with playlist data.
    def setData(self, name, image_url):
        
        self.ui._playlistName.setText(name)

        # Load the playlist image from the URL
        try:
            response = get(image_url)
            
            pixmap = QPixmap()
            pixmap.loadFromData(response.content)
            
            rounded_pixmap = self.round_pixmap(pixmap, 8)

            # Set the scaled pixmap on the image label
            self.ui._playlistImage.setPixmap(rounded_pixmap.scaled(
                self.ui._playlistImage.size(),
                Qt.AspectRatioMode.KeepAspectRatioByExpanding,
                Qt.TransformationMode.SmoothTransformation
            ))
            
            self.ui._playlistImage.setStyleSheet("background-color: transparent;")

        except Exception as e:
            print(f"Error loading image for '{name}': {e}")
            self.ui._playlistImage.setText("No Image")

    # Helper function to create a rounded QPixmap.
    def round_pixmap(self, pixmap, radius):
        
        rounded = QPixmap(pixmap.size())
        rounded.fill(Qt.GlobalColor.transparent)

        painter = QPainter(rounded)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        painter.setBrush(QBrush(pixmap))
        painter.setPen(Qt.PenStyle.NoPen)
        painter.drawRoundedRect(pixmap.rect(), radius, radius)
        painter.end()
        
        return rounded