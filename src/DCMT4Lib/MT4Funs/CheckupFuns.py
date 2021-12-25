from DCMT4Lib.MT4Funs.MT4FunsBase import *

class CheckupFuns(MT4FunsBase):
    def __init__(self, logger, wHD, Send_Msg_To_MT4):
        super().__init__(logger, wHD, Send_Msg_To_MT4)

    def GetLastError(self):
        return self._Single_Return_Fun(Fun_Enum.GetLastError)

    def IsStopped(self):
        return bool(self._Single_Return_Fun(Fun_Enum.IsStopped))

    def UninitializeReason(self):
        return self._Single_Return_Fun(Fun_Enum.UninitializeReason)

    def MQLInfo(self, property_id):
        DCMT4Wrapper.Create_Msg(self._wHD, 1)
        DCMT4Wrapper.Set_Int_To_Msg(self._wHD, property_id.value)

        msg = self._Send_Msg_To_MT4(Fun_Enum.MQLInfo)
        value = msg[1]
        return value

    def MQLSetInteger(self, property_id, property_value):
        DCMT4Wrapper.Create_Msg(self._wHD, 2)
        DCMT4Wrapper.Set_Int_To_Msg(self._wHD, property_id.value)
        DCMT4Wrapper.Set_Int_To_Msg(self._wHD, property_value.value)

        msg = self._Send_Msg_To_MT4(Fun_Enum.MQLSetInteger)

    def TerminalInfo(self, property_id):
        DCMT4Wrapper.Create_Msg(self._wHD, 1)
        DCMT4Wrapper.Set_Int_To_Msg(self._wHD, property_id.value)

        msg = self._Send_Msg_To_MT4(Fun_Enum.TerminalInfo)
        value = msg[1]
        return value

    def Period(self):
        return self._Single_Return_Fun(Fun_Enum.Period)

    def IsConnected(self):
        return bool(self._Single_Return_Fun(Fun_Enum.Digits))

    def IsDemo(self):
        return bool(self._Single_Return_Fun(Fun_Enum.IsDemo))

    def IsDllsAllowed(self):
        return bool(self._Single_Return_Fun(Fun_Enum.IsDllsAllowed))

    def IsExpertEnabled(self):
        return bool(self._Single_Return_Fun(Fun_Enum.IsExpertEnabled))

    def IsLibrariesAllowed(self):
        return bool(self._Single_Return_Fun(Fun_Enum.IsLibrariesAllowed))

    def IsOptimization(self):
        return bool(self._Single_Return_Fun(Fun_Enum.IsOptimization))

    def IsTesting(self):
        return bool(self._Single_Return_Fun(Fun_Enum.IsTesting))

    def IsTradeAllowed(self, symbol, tested_time):
        if not None == tested_time:
            DCMT4Wrapper.Create_Msg(self._wHD, 2)
            DCMT4Wrapper.Set_String_To_Msg(self._wHD, symbol)
            self._data_assign_helper.Set_Datetime_To_Msg(self._wHD, tested_time)
        else:
            DCMT4Wrapper.Create_Msg(self._wHD, 1)
            DCMT4Wrapper.Set_String_To_Msg(self._wHD, symbol)

        msg = self._Send_Msg_To_MT4(Fun_Enum.IsTradeAllowed)
        ret = msg[1]
        return bool(ret)

    def IsTradeContextBusy(self):
        return bool(self._Single_Return_Fun(Fun_Enum.IsTradeContextBusy))

    def IsVisualMode(self):
        return bool(self._Single_Return_Fun(Fun_Enum.IsVisualMode))

    def TerminalCompany(self):
        return self._Single_Return_Fun(Fun_Enum.TerminalCompany)

    def TerminalName(self):
        return self._Single_Return_Fun(Fun_Enum.TerminalName)

    def TerminalPath(self):
        return self._Single_Return_Fun(Fun_Enum.TerminalPath)
