from typing import List
from models.scene_object import SceneObject
from models.model import Model
from models.rig import Rig
# Import other models as needed

class ScanningService:
    @staticmethod
    def scan_scene() -> List[SceneObject]:
        # Placeholder for scanning logic
        # In a real implementation, this would interact with DCC via adapters

        # Example scanned objects
        scanned_objects = [
            Model(name="ValidModelName"),
            Model(name="Invalid@ModelName!"),
            Rig(name="ValidRigName"),
            # Add other objects as needed
        ]
        return scanned_objects
