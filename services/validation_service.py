from validators.validator_factory import ValidatorFactory

class ValidationService:
    def validate_objects(self, objects):
        results = {}
        for obj in objects:
            validators = ValidatorFactory.get_validators(obj)
            obj_results = []
            for validator in validators:
                result = validator.execute()
                obj_results.append((validator, result))
            results[obj] = obj_results
        return results
