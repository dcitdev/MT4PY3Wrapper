from DCMT4Lib.MT4Funs.MT4FunsBase import *

class ChartOperationsFuns(MT4FunsBase):
    def __init__(self, logger, wHD, Send_Msg_To_MT4):
        super().__init__(logger, wHD, Send_Msg_To_MT4)

    def ChartApplyTemplate(self, chart_id, filename):
        DCMT4Wrapper.Create_Msg(self._wHD, 2)
        DCMT4Wrapper.Set_Int_To_Msg(self._wHD, chart_id)
        DCMT4Wrapper.Set_String_To_Msg(self._wHD, filename)

        msg = self._Send_Msg_To_MT4(Fun_Enum.ChartApplyTemplate)
        value = msg[1]
        return bool(value)

    def ChartSaveTemplate(self, chart_id, filename):
        DCMT4Wrapper.Create_Msg(self._wHD, 2)
        DCMT4Wrapper.Set_Int_To_Msg(self._wHD, chart_id)
        DCMT4Wrapper.Set_String_To_Msg(self._wHD, filename)

        msg = self._Send_Msg_To_MT4(Fun_Enum.ChartSaveTemplate)
        value = msg[1]
        return bool(value)

    def ChartWindowFind(self, chart_id, indicator_shortname):
        DCMT4Wrapper.Create_Msg(self._wHD, 2)
        DCMT4Wrapper.Set_Int_To_Msg(self._wHD, chart_id)
        DCMT4Wrapper.Set_String_To_Msg(self._wHD, indicator_shortname)

        msg = self._Send_Msg_To_MT4(Fun_Enum.ChartWindowFind)
        value = msg[1]
        return value

    def ChartTimePriceToXY(self, chart_id, sub_window, time, price):
        DCMT4Wrapper.Create_Msg(self._wHD, 4)
        DCMT4Wrapper.Set_Int_To_Msg(self._wHD, chart_id)
        DCMT4Wrapper.Set_Int_To_Msg(self._wHD, sub_window)
        self._data_assign_helper.Set_Datetime_To_Msg(self._wHD, time)
        DCMT4Wrapper.Set_Double_To_Msg(self._wHD, price)

        msg = self._Send_Msg_To_MT4(Fun_Enum.ChartTimePriceToXY)
        ret = msg[1]
        x = msg[2]
        y = msg[3]
        return (bool(ret), x, y)

    def ChartXYToTimePrice(self, chart_id, x, y):
        DCMT4Wrapper.Create_Msg(self._wHD, 3)
        DCMT4Wrapper.Set_Int_To_Msg(self._wHD, chart_id)
        DCMT4Wrapper.Set_Int_To_Msg(self._wHD, x)
        DCMT4Wrapper.Set_Int_To_Msg(self._wHD, y)

        msg = self._Send_Msg_To_MT4(Fun_Enum.ChartXYToTimePrice)
        ret = msg[1]
        sub_window = msg[2]
        time = self._data_assign_helper.Get_Datetime_From_Msg(msg[3])
        price = msg[4]
        return (bool(ret), sub_window, time, price)

    def ChartOpen(self, symbol, period):
        DCMT4Wrapper.Create_Msg(self._wHD, 2)
        DCMT4Wrapper.Set_String_To_Msg(self._wHD, symbol)
        DCMT4Wrapper.Set_Int_To_Msg(self._wHD, period.value)

        msg = self._Send_Msg_To_MT4(Fun_Enum.ChartOpen)
        value = msg[1]
        return value

    def ChartFirst(self):
        return self._Single_Return_Fun(Fun_Enum.ChartFirst)

    def ChartNext(self, chart_id):
        return self.__ChartAction(chart_id, Fun_Enum.ChartNext)

    def ChartClose(self, chart_id = 0):
        return self.__ChartAction(chart_id, Fun_Enum.ChartClose)

    def ChartSymbol(self, chart_id = 0):
        return self.__ChartAction(chart_id, Fun_Enum.ChartSymbol)

    def ChartPeriod(self, chart_id = 0):
        return PERIOD_Enum(self.__ChartAction(chart_id, Fun_Enum.ChartPeriod))

    def ChartRedraw(self, chart_id = 0):
        DCMT4Wrapper.Create_Msg(self._wHD, 0)

        msg = self._Send_Msg_To_MT4(Fun_Enum.ChartRedraw)

    def ChartSetDouble(self, chart_id, prop_id, value):
        DCMT4Wrapper.Create_Msg(self._wHD, 3)
        DCMT4Wrapper.Set_Int_To_Msg(self._wHD, chart_id)
        DCMT4Wrapper.Set_Int_To_Msg(self._wHD, prop_id.value)
        DCMT4Wrapper.Set_Double_To_Msg(self._wHD, value)

        msg = self._Send_Msg_To_MT4(Fun_Enum.ChartSetDouble)
        value = msg[1]
        return bool(value)

    def ChartSetInteger(self, chart_id, prop_id, value, sub_window = -1):
        number_fields = 3
        if sub_window == -1:
            DCMT4Wrapper.Create_Msg(self._wHD, 4)
            DCMT4Wrapper.Set_Int_To_Msg(self._wHD, number_fields)
            DCMT4Wrapper.Set_Int_To_Msg(self._wHD, chart_id)
            DCMT4Wrapper.Set_Int_To_Msg(self._wHD, prop_id.value)
            DCMT4Wrapper.Set_Int_To_Msg(self._wHD, value)
        else:
            number_fields = 4
            DCMT4Wrapper.Create_Msg(self._wHD, 5)
            DCMT4Wrapper.Set_Int_To_Msg(self._wHD, number_fields)
            DCMT4Wrapper.Set_Int_To_Msg(self._wHD, chart_id)
            DCMT4Wrapper.Set_Int_To_Msg(self._wHD, prop_id.value)
            DCMT4Wrapper.Set_Int_To_Msg(self._wHD, value)
            DCMT4Wrapper.Set_Int_To_Msg(self._wHD, sub_window)

        msg = self._Send_Msg_To_MT4(Fun_Enum.ChartSetInteger)
        value = msg[1]
        return bool(value)

    def ChartSetString(self, chart_id, prop_id, str_value):
        DCMT4Wrapper.Create_Msg(self._wHD, 3)
        DCMT4Wrapper.Set_Int_To_Msg(self._wHD, chart_id)
        DCMT4Wrapper.Set_Int_To_Msg(self._wHD, prop_id.value)
        DCMT4Wrapper.Set_String_To_Msg(self._wHD, str_value)

        msg = self._Send_Msg_To_MT4(Fun_Enum.ChartSetString)
        value = msg[1]
        return bool(value)

    def ChartGetDouble(self, chart_id, prop_id, sub_window = 0):
        return self.__ChartGet(chart_id, prop_id, sub_window, Fun_Enum.ChartGetDouble)

    def ChartGetInteger(self, chart_id, prop_id, sub_window = 0):
        return self.__ChartGet(chart_id, prop_id, sub_window, Fun_Enum.ChartGetInteger)

    def ChartGetString(self, chart_id, prop_id):
        return self.__ChartGet(chart_id, prop_id, 0, Fun_Enum.ChartGetString)

    def ChartNavigate(self, chart_id, position, shift = 0):
        DCMT4Wrapper.Create_Msg(self._wHD, 3)
        DCMT4Wrapper.Set_Int_To_Msg(self._wHD, chart_id)
        DCMT4Wrapper.Set_Int_To_Msg(self._wHD, position)
        DCMT4Wrapper.Set_Int_To_Msg(self._wHD, shift)

        msg = self._Send_Msg_To_MT4(Fun_Enum.ChartNavigate)
        ret = msg[1]
        return bool(ret)

    def ChartID(self):
        return self._Single_Return_Fun(Fun_Enum.ChartID)

    def ChartIndicatorDelete(self, chart_id, sub_window, indicator_shortname):
        DCMT4Wrapper.Create_Msg(self._wHD, 3)
        DCMT4Wrapper.Set_Int_To_Msg(self._wHD, chart_id)
        DCMT4Wrapper.Set_Int_To_Msg(self._wHD, sub_window)
        DCMT4Wrapper.Set_String_To_Msg(self._wHD, indicator_shortname)

        msg = self._Send_Msg_To_MT4(Fun_Enum.ChartIndicatorDelete)
        ret = msg[1]
        return bool(ret)

    def ChartIndicatorName(self, chart_id, sub_window, index):
        DCMT4Wrapper.Create_Msg(self._wHD, 3)
        DCMT4Wrapper.Set_Int_To_Msg(self._wHD, chart_id)
        DCMT4Wrapper.Set_Int_To_Msg(self._wHD, sub_window)
        DCMT4Wrapper.Set_Int_To_Msg(self._wHD, index)

        msg = self._Send_Msg_To_MT4(Fun_Enum.ChartIndicatorName)
        value = msg[1]
        return value

    def ChartIndicatorsTotal(self, chart_id, sub_window):
        DCMT4Wrapper.Create_Msg(self._wHD, 2)
        DCMT4Wrapper.Set_Int_To_Msg(self._wHD, chart_id)
        DCMT4Wrapper.Set_Int_To_Msg(self._wHD, sub_window)

        msg = self._Send_Msg_To_MT4(Fun_Enum.ChartIndicatorName)
        value = msg[1]
        return value

    def ChartWindowOnDropped(self):
        return self._Single_Return_Fun(Fun_Enum.ChartWindowOnDropped)

    def ChartPriceOnDropped(self):
        return self._Single_Return_Fun(Fun_Enum.ChartPriceOnDropped)

    def ChartTimeOnDropped(self):
        return self._Single_Return_Fun(Fun_Enum.ChartTimeOnDropped)

    def ChartXOnDropped(self):
        return self._Single_Return_Fun(Fun_Enum.ChartXOnDropped)

    def ChartYOnDropped(self):
        return self._Single_Return_Fun(Fun_Enum.ChartYOnDropped)

    def ChartSetSymbolPeriod(self, chart_id, symbol, period):
        DCMT4Wrapper.Create_Msg(self._wHD, 3)
        DCMT4Wrapper.Set_Int_To_Msg(self._wHD, chart_id)
        DCMT4Wrapper.Set_Int_To_Msg(self._wHD, symbol)
        DCMT4Wrapper.Set_Int_To_Msg(self._wHD, period.value)

        msg = self._Send_Msg_To_MT4(Fun_Enum.ChartSetSymbolPeriod)
        ret = msg[1]
        return bool(ret)

    def ChartScreenShot(self, chart_id, filename, width, height, align_mode = ALIGN_Enum.ALIGN_RIGHT):
        DCMT4Wrapper.Create_Msg(self._wHD, 5)
        DCMT4Wrapper.Set_Int_To_Msg(self._wHD, chart_id)
        DCMT4Wrapper.Set_String_To_Msg(self._wHD, filename)
        DCMT4Wrapper.Set_Int_To_Msg(self._wHD, width)
        DCMT4Wrapper.Set_Int_To_Msg(self._wHD, height)
        DCMT4Wrapper.Set_Int_To_Msg(self._wHD, align_mode.value)

        msg = self._Send_Msg_To_MT4(Fun_Enum.ChartSetSymbolPeriod)
        ret = msg[1]
        return bool(ret)

    def Period(self):
        return self._Single_Return_Fun(Fun_Enum.Period)

    def Symbol(self):
        return self._Single_Return_Fun(Fun_Enum.Symbol)

    def WindowBarsPerChart(self):
        return self._Single_Return_Fun(Fun_Enum.WindowBarsPerChart)

    def WindowExpertName(self):
        return self._Single_Return_Fun(Fun_Enum.WindowExpertName)

    def WindowFind(self, name):
        DCMT4Wrapper.Create_Msg(self._wHD, 1)
        DCMT4Wrapper.Set_String_To_Msg(self._wHD, name)

        msg = self._Send_Msg_To_MT4(Fun_Enum.WindowFind)
        value = msg[1]
        return value

    def WindowFirstVisibleBar(self):
        return self._Single_Return_Fun(Fun_Enum.WindowFirstVisibleBar)

    def WindowHandle(self, symbol, timeframe):
        DCMT4Wrapper.Create_Msg(self._wHD, 2)
        DCMT4Wrapper.Set_String_To_Msg(self._wHD, symbol)
        DCMT4Wrapper.Set_Int_To_Msg(self._wHD, timeframe.value)

        msg = self._Send_Msg_To_MT4(Fun_Enum.WindowHandle)
        value = msg[1]
        return value

    def WindowIsVisible(self, index):
        DCMT4Wrapper.Create_Msg(self._wHD, 1)
        DCMT4Wrapper.Set_Int_To_Msg(self._wHD, index)

        msg = self._Send_Msg_To_MT4(Fun_Enum.WindowIsVisible)
        value = msg[1]
        return value

    def WindowOnDropped(self):
        return self._Single_Return_Fun(Fun_Enum.WindowOnDropped)

    def WindowPriceMax(self, index = 0):
        DCMT4Wrapper.Create_Msg(self._wHD, 1)
        DCMT4Wrapper.Set_Int_To_Msg(self._wHD, index)

        msg = self._Send_Msg_To_MT4(Fun_Enum.WindowPriceMax)
        value = msg[1]
        return value

    def WindowPriceMin(self, index = 0):
        DCMT4Wrapper.Create_Msg(self._wHD, 1)
        DCMT4Wrapper.Set_Int_To_Msg(self._wHD, index)

        msg = self._Send_Msg_To_MT4(Fun_Enum.WindowPriceMin)
        value = msg[1]
        return value

    def WindowPriceOnDropped(self):
        return self._Single_Return_Fun(Fun_Enum.WindowPriceOnDropped)

    def WindowRedraw(self):
        DCMT4Wrapper.Create_Msg(self._wHD, 0)

        msg = self._Send_Msg_To_MT4(Fun_Enum.WindowRedraw)

    def WindowScreenShot(self, filename, size_x, size_y, start_bar = -1, chart_scale = -1, chart_mode = -1):
        DCMT4Wrapper.Create_Msg(self._wHD, 6)
        DCMT4Wrapper.Set_String_To_Msg(self._wHD, filename)
        DCMT4Wrapper.Set_Int_To_Msg(self._wHD, size_x)
        DCMT4Wrapper.Set_Int_To_Msg(self._wHD, size_y)
        DCMT4Wrapper.Set_Int_To_Msg(self._wHD, start_bar)
        DCMT4Wrapper.Set_Int_To_Msg(self._wHD, chart_scale)
        DCMT4Wrapper.Set_Int_To_Msg(self._wHD, chart_mode)

        msg = self._Send_Msg_To_MT4(Fun_Enum.WindowScreenShot)
        ret = msg[1]
        return bool(ret)

    def WindowTimeOnDropped(self):
        return self._data_assign_helper.Get_Datetime_From_Msg(self._Single_Return_Fun(Fun_Enum.WindowTimeOnDropped))

    def WindowsTotal(self):
        return self._Single_Return_Fun(Fun_Enum.WindowsTotal)

    def WindowXOnDropped(self):
        return self._Single_Return_Fun(Fun_Enum.WindowXOnDropped)

    def WindowYOnDropped(self):
        return self._Single_Return_Fun(Fun_Enum.WindowYOnDropped)

    def __ChartAction(self, chart_id, fun_enum):
        DCMT4Wrapper.Create_Msg(self._wHD, 1)
        DCMT4Wrapper.Set_Int_To_Msg(self._wHD, chart_id)

        msg = self._Send_Msg_To_MT4(fun_enum)
        value = msg[1]
        return value

    def __ChartGet(self, chart_id, prop_id, sub_window, fun_enum):
        DCMT4Wrapper.Create_Msg(self._wHD, 3)
        DCMT4Wrapper.Set_Int_To_Msg(self._wHD, chart_id)
        DCMT4Wrapper.Set_Int_To_Msg(self._wHD, prop_id.value)
        DCMT4Wrapper.Set_Int_To_Msg(self._wHD, sub_window)

        msg = self._Send_Msg_To_MT4(fun_enum)
        ret = msg[1]
        value = msg[2]
        return (bool(ret), value)
