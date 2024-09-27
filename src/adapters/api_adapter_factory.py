from src.adapters.base_adapter import BaseAdapter
from src.adapters.maya_api_adapter import MayaApiAdapter
from src.adapters.houdini_api_adapter import HoudiniApiAdapter
from src.utils.dcc_detector import DCCDetector

class ApiAdapterFactory:
    @staticmethod
    def get_api_adapter() -> BaseAdapter:
        dcc = DCCDetector.get_current_dcc()
        if dcc == 'maya':
            return MayaApiAdapter()
        elif dcc == 'houdini':
            return HoudiniApiAdapter()
        else:
            raise NotImplementedError(f"No ApiAdapter implemented for DCC '{dcc}'")
