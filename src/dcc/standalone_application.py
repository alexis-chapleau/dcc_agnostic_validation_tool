from src.dcc.base_application import BaseApplication
from typing import Optional
from PySide6.QtWidgets import QWidget

class StandaloneApplication(BaseApplication):
    def get_main_window(self) -> Optional[QWidget]:
        return None  # No parent window in standalone mode

    def is_standalone(self) -> bool:
        return True
