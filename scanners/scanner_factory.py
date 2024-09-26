from typing import List
from scanners.base_scanner import BaseScanner
from adapters.api_adapter_factory import ApiAdapterFactory
from scanners.camera_scanner import CameraScanner
from utils.dcc_detector import DCCDetector

class ScannerFactory:
    @staticmethod
    def get_scanners() -> List[BaseScanner]:
        dcc = DCCDetector.get_current_dcc()
        api_adapter = ApiAdapterFactory.get_api_adapter()

        scanners: List[BaseScanner] = []

        # Determine which scanners to use based on DCC and object types
        if dcc == 'maya':
            # Example: Use DCC-specific CameraScanner for Maya
            scanners.append(CameraScanner(api_adapter))
            # Add other scanners as needed
        elif dcc == 'houdini':
            scanners.append(CameraScanner(api_adapter))

        else:
            # For unknown DCCs, you might raise an exception or use generic scanners if possible
            raise NotImplementedError(f"No scanners implemented for DCC '{dcc}'")

        return scanners
