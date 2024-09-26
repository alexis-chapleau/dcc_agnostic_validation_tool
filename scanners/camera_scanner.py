from scanners.base_scanner import BaseScanner
from models.camera import Camera
from typing import List

class CameraScanner(BaseScanner):

    def scan(self) -> List[Camera]:
        camera_names = self.api_adapter.scan_cameras()
        cameras = []
        for name in camera_names:
            # Include any business logic specific to cameras
            cameras.append(Camera(name=name))
        return cameras
