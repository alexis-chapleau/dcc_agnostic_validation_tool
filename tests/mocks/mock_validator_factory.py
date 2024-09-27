from src.validators.base_validator import BaseValidator
from typing import List

class MockValidatorFactory:
    @staticmethod
    def get_validators(obj) -> List[BaseValidator]:
        from src.validators.name_validator import NameValidator
        return [NameValidator(obj)]
