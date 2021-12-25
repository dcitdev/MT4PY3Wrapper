from DCMT4Lib.MT4Funs.MT4FunsBase import *

class PredefinedVariablesFuns(MT4FunsBase):
    def __init__(self, logger, wHD, Send_Msg_To_MT4):
        super().__init__(logger, wHD, Send_Msg_To_MT4)

    def Bars(self):
        DCMT4Wrapper.Create_Msg(self._wHD, 0)

        msg = self._Send_Msg_To_MT4(Fun_Enum.Bars)
        bars = msg[1]
        return bars

    def Volume(self, index):
        DCMT4Wrapper.Create_Msg(self._wHD, 1)
        DCMT4Wrapper.Set_Int_To_Msg(self._wHD, index)

        msg = self._Send_Msg_To_MT4(Fun_Enum.Volume)
        volume = self._data_assign_helper.Get_Int64_From_Msg(msg, 1, 2)
        return volume

    def Open(self, index):
        DCMT4Wrapper.Create_Msg(self._wHD, 1)
        DCMT4Wrapper.Set_Int_To_Msg(self._wHD, index)

        msg = self._Send_Msg_To_MT4(Fun_Enum.Open)
        open_val = msg[1]
        return open_val

    def Close(self, index):
        DCMT4Wrapper.Create_Msg(self._wHD, 1)
        DCMT4Wrapper.Set_Int_To_Msg(self._wHD, index)

        msg = self._Send_Msg_To_MT4(Fun_Enum.Close)
        close_val = msg[1]
        return close_val

    def Ask(self):
        DCMT4Wrapper.Create_Msg(self._wHD, 0)

        msg = self._Send_Msg_To_MT4(Fun_Enum.Ask)
        ask = msg[1]
        return ask

    def Bid(self):
        DCMT4Wrapper.Create_Msg(self._wHD, 0)

        msg = self._Send_Msg_To_MT4(Fun_Enum.Bid)
        bid = msg[1]
        return bid

    def Time(self, index):
        DCMT4Wrapper.Create_Msg(self._wHD, 1)
        DCMT4Wrapper.Set_Int_To_Msg(self._wHD, index)

        msg = self._Send_Msg_To_MT4(Fun_Enum.Time)
        date_time = self._data_assign_helper.Get_Datetime_From_Msg(msg[1])
        return date_time

    def Digits(self):
        DCMT4Wrapper.Create_Msg(self._wHD, 0)

        msg = self._Send_Msg_To_MT4(Fun_Enum.Digits)
        digits = msg[1]
        return digits

    def High(self, index):
        DCMT4Wrapper.Create_Msg(self._wHD, 1)
        DCMT4Wrapper.Set_Int_To_Msg(self._wHD, index)

        msg = self._Send_Msg_To_MT4(Fun_Enum.High)
        high_val = msg[1]
        return high_val

    def Low(self, index):
        DCMT4Wrapper.Create_Msg(self._wHD, 1)
        DCMT4Wrapper.Set_Int_To_Msg(self._wHD, index)

        msg = self._Send_Msg_To_MT4(Fun_Enum.Low)
        low_val = msg[1]
        return low_val

    def Point(self):
        DCMT4Wrapper.Create_Msg(self._wHD, 0)

        msg = self._Send_Msg_To_MT4(Fun_Enum.Point)
        point = msg[1]
        return point
