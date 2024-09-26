from enum import Enum, auto

class ValidationStatus(Enum):
    GOOD = auto()
    WARNING = auto()
    ERROR = auto()

class ValidationResult:
    def __init__(self, status: ValidationStatus, message: str = ""):
        self.status = status
        self.message = message
