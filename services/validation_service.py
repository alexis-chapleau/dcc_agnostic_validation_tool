from typing import Dict, List
from models.scene_object import SceneObject
from utils.validation_result import ValidationResult
from validators.validator_factory import ValidatorFactory

class ValidationService:
    def __init__(self):
        self.validation_results: Dict[str, List[ValidationResult]] = {}

    def validate_objects(self, objects: List[SceneObject]) -> None:
        for obj in objects:
            validators = ValidatorFactory.get_validators(obj)
            obj_results = []
            for validator in validators:
                result = validator.execute()
                obj_results.append(result)
            self.validation_results[obj.uuid] = obj_results
