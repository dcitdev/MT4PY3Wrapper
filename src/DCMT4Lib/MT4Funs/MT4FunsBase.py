import DCMT4Wrapper
from DCMT4Lib.CommonTools.DataStructure import *
from DCMT4Lib.CommonTools.DataAssignHelper import DataAssignHelper
from DCMT4Lib.CommonTools.CommonDefine import *
from DCMT4Lib.CommonTools.EnumDefine import *

class MT4FunsBase(object):
    def __init__(self, logger, wHD, Send_Msg_To_MT4):
        self._logger = logger
        self._wHD = wHD
        self._Send_Msg_To_MT4 = Send_Msg_To_MT4
        self._data_assign_helper = DataAssignHelper(self._logger)

    def _Single_Return_Fun(self, fun_enum):
        DCMT4Wrapper.Create_Msg(self._wHD, 0)

        msg = self._Send_Msg_To_MT4(fun_enum)
        value = msg[1]
        return value
