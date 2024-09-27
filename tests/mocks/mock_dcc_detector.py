from src.utils.dcc_detector import DCCDetector

class MockDCCDetector(DCCDetector):
    @staticmethod
    def get_current_dcc():
        return 'test_dcc'  # A placeholder DCC for testing
