from validators.name_validator import NameValidator
from models.model import Model


class ValidatorFactory:
    @staticmethod
    def get_validators(obj):
        validators = []
        if isinstance(obj, Model):
            validators.append(NameValidator(obj))
            # Add more validators as needed
        return validators
