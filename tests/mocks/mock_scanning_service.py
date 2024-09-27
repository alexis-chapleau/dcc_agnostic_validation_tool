from src.services.scanning_service import ScanningService
from src.models.model import Model
from src.models.camera import Camera

class MockScanningService(ScanningService):
    @staticmethod
    def scan_scene():
        return [
            Model(name='MockModel1'),
            Model(name='MockModel@Invalid'),
            Camera(name='MockCamera1'),
            Camera(name='Camera#Invalid')
        ]
