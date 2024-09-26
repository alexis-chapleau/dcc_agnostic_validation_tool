import unittest
from unittest.mock import patch
from services.validation_service import ValidationService
from models.model import Model
from models.camera import Camera
from utils.validation_result import ValidationStatus
from tests.mocks.mock_validator_factory import MockValidatorFactory

class TestValidationService(unittest.TestCase):
    @patch('services.validation_service.ValidatorFactory', new=MockValidatorFactory)
    def test_validate_objects(self):
        # Arrange
        validation_service = ValidationService()
        objects = [
            Model(name='ValidModel'),
            Model(name='Invalid@Model'),
            Camera(name='ValidCamera'),
            Camera(name='Camera#1'),
        ]

        # Act
        validation_service.validate_objects(objects)

        # Assert
        for obj in objects:
            obj_results = validation_service.validation_results.get(obj.uuid, [])
            self.assertGreater(len(obj_results), 0)
            for result in obj_results:
                if '@' in obj.name or '#' in obj.name:
                    self.assertEqual(result.status, ValidationStatus.ERROR)
                else:
                    self.assertEqual(result.status, ValidationStatus.GOOD)

if __name__ == '__main__':
    unittest.main()
