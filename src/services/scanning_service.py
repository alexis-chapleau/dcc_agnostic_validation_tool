from typing import List
from src.models.scene_object import SceneObject
from src.scanners.scanner_factory import ScannerFactory

class ScanningService:
    @staticmethod
    def scan_scene() -> List[SceneObject]:
        scanned_objects: List[SceneObject] = []

        scanners = ScannerFactory.get_scanners()

        for scanner in scanners:
            objects = scanner.scan()
            scanned_objects.extend(objects)

        return scanned_objects
