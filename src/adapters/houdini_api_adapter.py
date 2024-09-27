from src.adapters.base_adapter import BaseAdapter
from typing import List

try:
    import hou
except ImportError:
    hou = None  # Handle cases where Houdini is not available

class HoudiniApiAdapter(BaseAdapter):
    def scan_cameras(self) -> List[str]:
        if hou:
            cameras = hou.node('/obj').glob('*cam*')
            return [camera.path() for camera in cameras]
        else:
            return []

    def scan_models(self) -> List[str]:
        if hou:
            models = hou.node('/obj').glob('*geo*')
            return [model.path() for model in models]
        else:
            return []

    # Implement other methods as needed
