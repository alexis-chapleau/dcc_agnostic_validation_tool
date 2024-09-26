import unittest
from validators.name_validator import NameValidator
from models.scene_object import SceneObject
from utils.validation_result import ValidationStatus

class MockSceneObject(SceneObject):
    pass

class TestNameValidator(unittest.TestCase):
    def test_valid_name(self):
        # Arrange
        obj = MockSceneObject(name='ValidName')
        validator = NameValidator(obj)

        # Act
        result = validator.execute()

        # Assert
        self.assertEqual(result.status, ValidationStatus.GOOD)

    def test_invalid_name(self):
        # Arrange
        obj = MockSceneObject(name='Invalid@Name!')
        validator = NameValidator(obj)

        # Act
        result = validator.execute()

        # Assert
        self.assertEqual(result.status, ValidationStatus.ERROR)
        self.assertIn('special characters', result.message)

if __name__ == '__main__':
    unittest.main()
