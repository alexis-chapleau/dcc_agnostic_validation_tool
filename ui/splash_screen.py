from PySide6.QtWidgets import QSplashScreen
from PySide6.QtGui import QPixmap, Qt

class SplashScreen(QSplashScreen):
    def __init__(self):
        pixmap = QPixmap('ui/resources/splash_image.png')
        super().__init__(pixmap)
        self.showMessage("Loading...", alignment=Qt.AlignBottom | Qt.AlignCenter, color=Qt.white)
