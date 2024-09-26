import sys
from PySide6.QtWidgets import QApplication
from ui.main_window import MainWindow
from ui.splash_screen import SplashScreen
from utils.dcc_detector import DCCDetector


def main():
    app = QApplication(sys.argv)
    splash = SplashScreen()
    splash.show()

    dcc = DCCDetector.get_current_dcc()
    if dcc == 'standalone':
        # Import mocked services
        from tests.mocks.mock_scanning_service import MockScanningService
        from tests.mocks.mock_validation_service import MockValidationService

        scanning_service = MockScanningService()
        validation_service = MockValidationService()

        window = MainWindow(
            scanning_service=scanning_service,
            validation_service=validation_service
        )
    else:
        # Use real services
        window = MainWindow()

    window.show()
    splash.finish(window)
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
