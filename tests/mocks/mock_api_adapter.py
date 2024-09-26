from adapters.base_adapter import BaseAdapter

class MockApiAdapter(BaseAdapter):
    def scan_cameras(self):
        # Simulated camera names
        return ['Camera1', 'Camera2', 'Camera_Special']

    def scan_models(self):
        # Simulated model names
        return ['Model1', 'Model@Invalid']

    # Implement other methods as needed
