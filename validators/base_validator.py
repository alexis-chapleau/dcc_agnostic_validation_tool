from abc import ABC, abstractmethod
from utils.validation_result import ValidationResult

class BaseValidator(ABC):
    fixable: bool = False

    def __init__(self, obj):
        self.obj = obj
        self._check_fixable()

    def _check_fixable(self):
        self.fixable = hasattr(self, 'fix_it')

    @abstractmethod
    def execute(self) -> ValidationResult:
        pass
