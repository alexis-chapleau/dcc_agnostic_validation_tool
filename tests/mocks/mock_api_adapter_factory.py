from src.adapters.api_adapter_factory import ApiAdapterFactory
from tests.mocks.mock_api_adapter import MockApiAdapter

class MockApiAdapterFactory(ApiAdapterFactory):
    @staticmethod
    def get_api_adapter():
        return MockApiAdapter()
