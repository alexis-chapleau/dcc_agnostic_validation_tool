from adapters.base_adapter import BaseAdapter
from typing import List

try:
    import maya.cmds as cmds
except ImportError:
    cmds = None  # Handle cases where Maya is not available

class MayaApiAdapter(BaseAdapter):
    def scan_cameras(self) -> List[str]:
        if cmds:
            return cmds.ls(type='camera', long=True)
        else:
            return []

    def scan_models(self) -> List[str]:
        if cmds:
            return cmds.ls(geometry=True, long=True)
        else:
            return []

    # Implement other methods as needed
