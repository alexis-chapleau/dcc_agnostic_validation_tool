from abc import ABC, abstractmethod
from typing import Optional
from PySide6.QtWidgets import QWidget

class BaseApplication(ABC):
    @abstractmethod
    def get_main_window(self) -> Optional[QWidget]:
        """Return the main window of the DCC application."""
        pass

    @abstractmethod
    def is_standalone(self) -> bool:
        """Return True if running in standalone mode (outside of a DCC)."""
        pass
