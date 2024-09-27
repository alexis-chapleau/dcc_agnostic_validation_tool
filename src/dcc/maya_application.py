from src.dcc.base_application import BaseApplication
from typing import Optional
from PySide6.QtWidgets import QWidget, QMainWindow

class MayaApplication(BaseApplication):
    def get_main_window(self) -> Optional[QWidget]:
        import maya.OpenMayaUI as OpenMayaUI
        from shiboken6 import wrapInstance

        ptr = OpenMayaUI.MQtUtil.mainWindow()
        if ptr is not None:
            return wrapInstance(int(ptr), QMainWindow)
        else:
            return None

    def is_standalone(self) -> bool:
        return False
