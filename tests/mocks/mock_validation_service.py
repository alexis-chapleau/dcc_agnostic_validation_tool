from services.validation_service import ValidationService
from utils.validation_result import ValidationResult, ValidationStatus
from validators.name_validator import NameValidator

class MockValidationService(ValidationService):
    def validate_objects(self, objects):
        # Simulate validation results
        for obj in objects:
            # Use the NameValidator to generate a validation result
            validator = NameValidator(obj)
            result = validator.execute()
            self.validation_results[obj.uuid] = [result]
