from typing import List, Type
from models.scene_object import SceneObject
from models.model import Model
from models.rig import Rig
from models.camera import Camera
from validators.base_validator import BaseValidator
from validators.name_validator import NameValidator
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
