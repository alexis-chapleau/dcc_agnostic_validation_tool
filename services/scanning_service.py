from models.model import Model

class ScanningService:
    @staticmethod
    def scan_scene():
        # Placeholder for scanning logic
        # In real implementation, interact with DCC via adapters
        return [
            Model(name="ValidName", long_name='long|name|ValidName'),
            Model(name="Invalid@Name!", long_name='long|name|Invalid@Name!')
        ]
