from abc import ABC, abstractmethod
from typing import List

class BaseAdapter(ABC):
    @abstractmethod
    def scan_cameras(self) -> List[str]:
        pass

    @abstractmethod
    def scan_models(self) -> List[str]:
        pass

    # Add abstract methods for other operations as needed
