from abc import ABC
import uuid
from dataclasses import dataclass, field

@dataclass
class SceneObject(ABC):
    name: str
    uuid: str = field(default_factory=lambda: str(uuid.uuid4()))

    def __hash__(self):
        return hash(self.uuid)
