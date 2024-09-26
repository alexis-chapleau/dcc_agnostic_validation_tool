import os

class DCCDetector:
    @staticmethod
    def get_current_dcc():
        # Check environment variables or try importing DCC-specific modules
        if 'MAYA_EXEC' in os.environ:
            return 'maya'
        elif 'HOUDINI_PATH' in os.environ:
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
        # Return 'standalone' if no DCC is detected
        return 'standalone'
