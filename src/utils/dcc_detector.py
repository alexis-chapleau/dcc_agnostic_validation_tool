import os

class DCCDetector:
    @staticmethod
    def get_current_dcc():
        if 'MAYA_LOCATION' in os.environ:
            return 'maya'
        elif 'HFS' in os.environ:
            return 'houdini'
        else:
            # Try importing DCC-specific modules
            try:
                import maya.cmds
                return 'maya'
            except ImportError:
                pass
            try:
                import hou
                return 'houdini'
            except ImportError:
                pass
            # Default to 'standalone'
            return 'standalone'
