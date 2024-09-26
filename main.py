import sys
from PySide6.QtWidgets import QApplication
from ui.main_window import MainWindow
from ui.splash_screen import SplashScreen


def main():
    app = QApplication(sys.argv)
    splash = SplashScreen()
    splash.show()

    window = MainWindow()
    window.show()
    splash.finish(window)
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
