from src.dcc.base_application import BaseApplication
from typing import Optional
from PySide6.QtWidgets import QWidget, QMainWindow

class HoudiniApplication(BaseApplication):
    def get_main_window(self) -> Optional[QWidget]:
        import hou
        from shiboken6 import wrapInstance

        ptr = hou.ui.mainQtWindow()
        if ptr is not None:
            return wrapInstance(int(ptr), QMainWindow)
        else:
            return None

    def is_standalone(self) -> bool:
        return False
