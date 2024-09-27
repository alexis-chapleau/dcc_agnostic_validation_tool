from typing import List, Type
from src.models.scene_object import SceneObject
from src.models.model import Model
from src.models.rig import Rig
from src.models.camera import Camera
from src.validators.base_validator import BaseValidator
from src.validators.name_validator import NameValidator
# Import other validators as they are implemented

class ValidatorFactory:
    _validator_mapping = {
        Model: [NameValidator],  # List of validator classes applicable to Model
        Rig: [NameValidator],
        Camera: [NameValidator],
        # Add other mappings as needed
    }

    @staticmethod
    def get_validator_classes(obj: SceneObject) -> List[Type[BaseValidator]]:
        validators = []
        for cls, validator_classes in ValidatorFactory._validator_mapping.items():
            if isinstance(obj, cls):
                validators.extend(validator_classes)
        return validators

    @staticmethod
    def get_validators(obj: SceneObject) -> List[BaseValidator]:
        validator_classes = ValidatorFactory.get_validator_classes(obj)
        return [validator_class(obj) for validator_class in validator_classes]
