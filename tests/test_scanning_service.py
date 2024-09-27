import unittest
from unittest.mock import patch
from src.services.scanning_service import ScanningService
from src.models.scene_object import SceneObject
from tests.mocks.mock_scanner_factory import MockScannerFactory

class TestScanningService(unittest.TestCase):
    @patch('src.services.scanning_service.ScannerFactory', new=MockScannerFactory)
    def test_scan_scene(self):
        # Act
        scanned_objects = ScanningService.scan_scene()

        # Assert
        self.assertIsInstance(scanned_objects, list)
        self.assertGreater(len(scanned_objects), 0)
        for obj in scanned_objects:
            self.assertIsInstance(obj, SceneObject)
            self.assertIsNotNone(obj.name)

if __name__ == '__main__':
    unittest.main()
