from DCMT4Lib.MT4Funs.MT4FunsBase import *

# https://docs.mql4.com/convert
class ConversionFuns(MT4FunsBase):
    def __init__(self, logger, wHD, Send_Msg_To_MT4):
        super().__init__(logger, wHD, Send_Msg_To_MT4)

    def NormalizeDouble(self, value, digits):
        DCMT4Wrapper.Create_Msg(self._wHD, 2)
        DCMT4Wrapper.Set_Double_To_Msg(self._wHD, value)
        DCMT4Wrapper.Set_Int_To_Msg(self._wHD, digits)

        msg = self._Send_Msg_To_MT4(Fun_Enum.NormalizeDouble)
        normalized_double = msg[1]
        return normalized_double
