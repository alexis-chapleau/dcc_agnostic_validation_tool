from src.dcc.base_application import BaseApplication
from src.dcc.maya_application import MayaApplication
from src.dcc.houdini_appliation import HoudiniApplication
from src.dcc.standalone_application import StandaloneApplication
from src.utils.dcc_detector import DCCDetector

class DCCFactory:
    @staticmethod
    def get_dcc_application() -> BaseApplication:
        dcc = DCCDetector.get_current_dcc()
        if dcc == 'maya':
            return MayaApplication()
        elif dcc == 'houdini':
            return HoudiniApplication()
        else:
            return StandaloneApplication()
