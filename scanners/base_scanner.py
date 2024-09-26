from abc import ABC, abstractmethod
from typing import List
from models.scene_object import SceneObject
from adapters.base_adapter import BaseAdapter


class BaseScanner(ABC):

    def __init__(self, api_adapter: BaseAdapter):
        self.api_adapter = api_adapter
    @abstractmethod
    def scan(self) -> List[SceneObject]:
        pass
