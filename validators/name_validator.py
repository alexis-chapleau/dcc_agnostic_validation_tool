import re
from validators.base_validator import BaseValidator
from utils.validation_result import ValidationResult, ValidationStatus

class NameValidator(BaseValidator):
    fixable = True  # Since we implement fix_it

    def execute(self) -> ValidationResult:
        if re.search(r'[^a-zA-Z0-9_]', self.obj.name):
            return ValidationResult(
                status=ValidationStatus.ERROR,
                message="Name contains special characters."
            )
        return ValidationResult(status=ValidationStatus.GOOD)

    def fix_it(self):
        # Remove special characters from name
        #TODO: use adapter to clean name
        import re
        clean_name = re.sub(r'[^a-zA-Z0-9_]', '', self.obj.name)
        self.obj.name = clean_name
