from DCMT4Lib.MT4Funs.MT4FunsBase import *

class MarketInfoFuns(MT4FunsBase):
    def __init__(self, logger, wHD, Send_Msg_To_MT4):
        super().__init__(logger, wHD, Send_Msg_To_MT4)

    def MarketInfo(self, symbol, mode_enum):
        DCMT4Wrapper.Create_Msg(self._wHD, 2)
        DCMT4Wrapper.Set_String_To_Msg(self._wHD, symbol)
        DCMT4Wrapper.Set_Int_To_Msg(self._wHD, mode_enum.value)

        msg = self._Send_Msg_To_MT4(Fun_Enum.MarketInfo)
        if Mode_Enum.MODE_TIME == mode_enum or Mode_Enum.MODE_STARTING == mode_enum or Mode_Enum.MODE_EXPIRATION == mode_enum:
            date_time = self._data_assign_helper.Get_Datetime_From_Msg(msg[1])
            return date_time
        else:
            value = msg[1]
            return value

    def SymbolsTotal(self, selected):
        DCMT4Wrapper.Create_Msg(self._wHD, 1)
        DCMT4Wrapper.Set_Int_To_Msg(self._wHD, int(selected))

        msg = self._Send_Msg_To_MT4(Fun_Enum.SymbolsTotal)
        value = msg[1]
        return value

    def SymbolName(self, pos, selected):
        DCMT4Wrapper.Create_Msg(self._wHD, 2)
        DCMT4Wrapper.Set_Int_To_Msg(self._wHD, pos)
        DCMT4Wrapper.Set_Int_To_Msg(self._wHD, int(selected))

        msg = self._Send_Msg_To_MT4(Fun_Enum.SymbolName)
        value = msg[1]
        return value

    def SymbolSelect(self, name, select):
        DCMT4Wrapper.Create_Msg(self._wHD, 2)
        DCMT4Wrapper.Set_String_To_Msg(self._wHD, name)
        DCMT4Wrapper.Set_Int_To_Msg(self._wHD, int(select))

        msg = self._Send_Msg_To_MT4(Fun_Enum.SymbolSelect)
        value = msg[1]
        return bool(value)

    def SymbolInfo(self, name, prop_id):
        DCMT4Wrapper.Create_Msg(self._wHD, 2)
        DCMT4Wrapper.Set_String_To_Msg(self._wHD, name)
        DCMT4Wrapper.Set_Int_To_Msg(self._wHD, prop_id.value)

        msg = self._Send_Msg_To_MT4(Fun_Enum.SymbolInfo)
        ret = msg[1]
        if Symbol_Info_Enum.SYMBOL_TIME == prop_id or Symbol_Info_Enum.SYMBOL_START_TIME == prop_id or Symbol_Info_Enum.SYMBOL_EXPIRATION_TIME == prop_id:
            value = self._data_assign_helper.Get_Datetime_From_Msg(msg[2])
            return (bool(ret), value)
        else:
            value = msg[2]
            return (bool(ret), value)

    def SymbolInfoTick(self, symbol, tick):
        DCMT4Wrapper.Create_Msg(self._wHD, 1)
        DCMT4Wrapper.Set_String_To_Msg(self._wHD, symbol)

        msg = self._Send_Msg_To_MT4(Fun_Enum.SymbolInfoTick)
        self._data_assign_helper.Assign_MqlTick(msg, 1, tick)
        ret = msg[7]
        return bool(ret)

    def SymbolInfoSessionQuote(self, name, day_of_week, session_index):
        DCMT4Wrapper.Create_Msg(self._wHD, 3)
        DCMT4Wrapper.Set_String_To_Msg(self._wHD, name)
        DCMT4Wrapper.Set_Int_To_Msg(self._wHD, day_of_week.value)
        DCMT4Wrapper.Set_Int_To_Msg(self._wHD, session_index)

        msg = self._Send_Msg_To_MT4(Fun_Enum.SymbolInfoSessionQuote)
        ret = msg[1]
        from_date = self._data_assign_helper.Get_Datetime_From_Msg(msg[2])
        to_date = self._data_assign_helper.Get_Datetime_From_Msg(msg[3])
        return (bool(ret), from_date, to_date)

    def SymbolInfoSessionTrade(self, name, day_of_week, session_index):
        DCMT4Wrapper.Create_Msg(self._wHD, 3)
        DCMT4Wrapper.Set_String_To_Msg(self._wHD, name)
        DCMT4Wrapper.Set_Int_To_Msg(self._wHD, day_of_week.value)
        DCMT4Wrapper.Set_Int_To_Msg(self._wHD, session_index)

        msg = self._Send_Msg_To_MT4(Fun_Enum.SymbolInfoSessionTrade)
        ret = msg[1]
        from_date = self._data_assign_helper.Get_Datetime_From_Msg(msg[2])
        to_date = self._data_assign_helper.Get_Datetime_From_Msg(msg[3])
        return (bool(ret), from_date, to_date)
