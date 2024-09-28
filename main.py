import sys
from PySide6.QtWidgets import QApplication
from src.ui.main_window import MainWindow
from src.dcc.dcc_factory import DCCFactory


def main():
    # Use existing QApplication instance or create one
    app = QApplication.instance()
    if not app:
        app = QApplication(sys.argv)

    # Get the DCC application instance
    dcc_app = DCCFactory.get_dcc_application()

    # Determine if running in standalone mode
    if dcc_app.is_standalone():
        # Import mocked services for standalone mode
        from tests.mocks.mock_scanning_service import MockScanningService
        from tests.mocks.mock_validation_service import MockValidationService

        scanning_service = MockScanningService()
        validation_service = MockValidationService()
    else:
        # Use real services inside the DCC
        scanning_service = None
        validation_service = None

    # Create the main window with the DCC's main window as parent
    window = MainWindow(
        scanning_service=scanning_service,
        validation_service=validation_service,
        parent=dcc_app.get_main_window()
    )

    window.show()
    # Do not call app.exec() if running inside a DCC
    if dcc_app.is_standalone():
        sys.exit(app.exec())

if __name__ == "__main__":
    main()
