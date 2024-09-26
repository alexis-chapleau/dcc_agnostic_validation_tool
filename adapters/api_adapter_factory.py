from adapters.base_adapter import BaseAdapter
from adapters.maya_api_adapter import MayaApiAdapter
from adapters.houdini_api_adapter import HoudiniApiAdapter
from utils.dcc_detector import DCCDetector

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
