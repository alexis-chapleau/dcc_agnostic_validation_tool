from scanners.base_scanner import BaseScanner
from scanners.camera_scanner import CameraScanner
from adapters.base_adapter import BaseAdapter
from typing import List

class MockScannerFactory:
    @staticmethod
    def get_scanners() -> List[BaseScanner]:
        # Use the MockApiAdapter
        from tests.mocks.mock_api_adapter import MockApiAdapter
        api_adapter = MockApiAdapter()
        # Return the scanners you want to test
        scanners = [
            CameraScanner(api_adapter),
            # Add other scanners as needed
        ]
        return scanners
