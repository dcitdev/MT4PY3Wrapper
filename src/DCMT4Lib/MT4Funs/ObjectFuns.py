from DCMT4Lib.MT4Funs.MT4FunsBase import *

class ObjectFuns(MT4FunsBase):
    def __init__(self, logger, wHD, Send_Msg_To_MT4):
        super().__init__(logger, wHD, Send_Msg_To_MT4)

    def ObjectCreate(self, object_name, object_type, sub_window, time1, price1, time2=0, price2=0, time3=0, price3=0):
        DCMT4Wrapper.Create_Msg(self._wHD, 9)
        DCMT4Wrapper.Set_String_To_Msg(self._wHD, object_name)
        DCMT4Wrapper.Set_Int_To_Msg(self._wHD, object_type.value)
        DCMT4Wrapper.Set_Int_To_Msg(self._wHD, sub_window)
        self._data_assign_helper.Set_Datetime_To_Msg(self._wHD, time1)
        DCMT4Wrapper.Set_Double_To_Msg(self._wHD, price1)
        if 0 == time2:
            DCMT4Wrapper.Set_Double_To_Msg(self._wHD, 0)
        else:
            self._data_assign_helper.Set_Datetime_To_Msg(self._wHD, time2)
        DCMT4Wrapper.Set_Double_To_Msg(self._wHD, price2)
        if 0 == time3:
            DCMT4Wrapper.Set_Double_To_Msg(self._wHD, 0)
        else:
            self._data_assign_helper.Set_Datetime_To_Msg(self._wHD, time3)
        DCMT4Wrapper.Set_Double_To_Msg(self._wHD, price3)

        msg = self._Send_Msg_To_MT4(Fun_Enum.ObjectCreate)
        value = msg[1]
        return bool(value)

    def ObjectName(self, object_index):
        DCMT4Wrapper.Create_Msg(self._wHD, 1)
        DCMT4Wrapper.Set_Int_To_Msg(self._wHD, object_index)

        msg = self._Send_Msg_To_MT4(Fun_Enum.ObjectName)
        value = msg[1]
        return value

    def ObjectDelete(self, object_name, chart_id = -1):
        DCMT4Wrapper.Create_Msg(self._wHD, 2)
        DCMT4Wrapper.Set_Int_To_Msg(self._wHD, chart_id)
        DCMT4Wrapper.Set_String_To_Msg(self._wHD, object_name)

        msg = self._Send_Msg_To_MT4(Fun_Enum.ObjectDelete)
        value = msg[1]
        return bool(value)

    def ObjectsDeleteAll(self, chart_id = -1, sub_window = -1, object_type = OBJ_Enum.OBJ_EMPTY, prefix = ""):
        DCMT4Wrapper.Create_Msg(self._wHD, 4)
        DCMT4Wrapper.Set_Int_To_Msg(self._wHD, chart_id)
        DCMT4Wrapper.Set_Int_To_Msg(self._wHD, sub_window)
        DCMT4Wrapper.Set_Int_To_Msg(self._wHD, object_type.value)
        DCMT4Wrapper.Set_String_To_Msg(self._wHD, prefix)

        msg = self._Send_Msg_To_MT4(Fun_Enum.ObjectsDeleteAll)
        value = msg[1]
        return value

    def ObjectFind(self, object_name, chart_id = -1):
        DCMT4Wrapper.Create_Msg(self._wHD, 2)
        DCMT4Wrapper.Set_Int_To_Msg(self._wHD, chart_id)
        DCMT4Wrapper.Set_String_To_Msg(self._wHD, object_name)

        msg = self._Send_Msg_To_MT4(Fun_Enum.ObjectFind)
        value = msg[1]
        return value

    def ObjectGetTimeByValue(self, chart_id, object_name, value, line_id = 0):
        DCMT4Wrapper.Create_Msg(self._wHD, 4)
        DCMT4Wrapper.Set_Int_To_Msg(self._wHD, chart_id)
        DCMT4Wrapper.Set_String_To_Msg(self._wHD, object_name)
        DCMT4Wrapper.Set_Double_To_Msg(self._wHD, value)
        DCMT4Wrapper.Set_Int_To_Msg(self._wHD, line_id)

        msg = self._Send_Msg_To_MT4(Fun_Enum.ObjectGetTimeByValue)
        value = self._data_assign_helper.Get_Datetime_From_Msg(msg[1])
        return value

    def ObjectGetValueByTime(self, chart_id, object_name, time, line_id = 0):
        DCMT4Wrapper.Create_Msg(self._wHD, 4)
        DCMT4Wrapper.Set_Int_To_Msg(self._wHD, chart_id)
        DCMT4Wrapper.Set_String_To_Msg(self._wHD, object_name)
        self._data_assign_helper.Set_Datetime_To_Msg(self._wHD, time)
        DCMT4Wrapper.Set_Int_To_Msg(self._wHD, line_id)

        msg = self._Send_Msg_To_MT4(Fun_Enum.ObjectGetValueByTime)
        value = msg[1]
        return value

    def ObjectMove(self, object_name, point_index, time, price):
        DCMT4Wrapper.Create_Msg(self._wHD, 4)
        DCMT4Wrapper.Set_String_To_Msg(self._wHD, object_name)
        DCMT4Wrapper.Set_Int_To_Msg(self._wHD, point_index)
        self._data_assign_helper.Set_Datetime_To_Msg(self._wHD, time)
        DCMT4Wrapper.Set_Double_To_Msg(self._wHD, price)

        msg = self._Send_Msg_To_MT4(Fun_Enum.ObjectMove)
        value = msg[1]
        return bool(value)

    def ObjectsTotal(self, chart_id = -1, sub_window = -1, obj_type = OBJ_Enum.OBJ_EMPTY):
        DCMT4Wrapper.Create_Msg(self._wHD, 3)
        DCMT4Wrapper.Set_Int_To_Msg(self._wHD, chart_id)
        DCMT4Wrapper.Set_Int_To_Msg(self._wHD, sub_window)
        DCMT4Wrapper.Set_Int_To_Msg(self._wHD, obj_type.value)

        msg = self._Send_Msg_To_MT4(Fun_Enum.ObjectsTotal)
        value = msg[1]
        return value

    def ObjectGetDouble(self, chart_id, object_name, prop_id, prop_modifier = OBJ_Enum.OBJ_EMPTY):
        return self.__ObjectGet(chart_id, object_name, prop_id, prop_modifier, Fun_Enum.ObjectGetDouble)

    def ObjectGetInteger(self, chart_id, object_name, prop_id, prop_modifier = OBJ_Enum.OBJ_EMPTY):
        return self.__ObjectGet(chart_id, object_name, prop_id, prop_modifier, Fun_Enum.ObjectGetInteger)

    def ObjectGetString(self, chart_id, object_name, prop_id, prop_modifier = OBJ_Enum.OBJ_EMPTY):
        return self.__ObjectGet(chart_id, object_name, prop_id, prop_modifier, Fun_Enum.ObjectGetString)

    def __ObjectGet(self, chart_id, object_name, prop_id, prop_modifier, fun_enum):
        DCMT4Wrapper.Create_Msg(self._wHD, 4)
        DCMT4Wrapper.Set_Int_To_Msg(self._wHD, chart_id)
        DCMT4Wrapper.Set_String_To_Msg(self._wHD, object_name)
        DCMT4Wrapper.Set_Int_To_Msg(self._wHD, prop_id.value)
        DCMT4Wrapper.Set_Int_To_Msg(self._wHD, prop_modifier.value)

        msg = self._Send_Msg_To_MT4(fun_enum)
        ret = msg[1]
        value = msg[2]
        return (bool(ret), value)

    def ObjectSetDouble(self, chart_id, object_name, prop_id, prop_value, prop_modifier = OBJ_Enum.OBJ_EMPTY):
        DCMT4Wrapper.Create_Msg(self._wHD, 5)
        DCMT4Wrapper.Set_Int_To_Msg(self._wHD, chart_id)
        DCMT4Wrapper.Set_String_To_Msg(self._wHD, object_name)
        DCMT4Wrapper.Set_Int_To_Msg(self._wHD, prop_id.value)
        DCMT4Wrapper.Set_Int_To_Msg(self._wHD, prop_modifier.value)
        DCMT4Wrapper.Set_Double_To_Msg(self._wHD, prop_value)

        msg = self._Send_Msg_To_MT4(Fun_Enum.ObjectSetDouble)
        ret = msg[1]
        return bool(ret)

    def ObjectSetInteger(self, chart_id, object_name, prop_id, prop_value, prop_modifier = OBJ_Enum.OBJ_EMPTY):
        DCMT4Wrapper.Create_Msg(self._wHD, 5)
        DCMT4Wrapper.Set_Int_To_Msg(self._wHD, chart_id)
        DCMT4Wrapper.Set_String_To_Msg(self._wHD, object_name)
        DCMT4Wrapper.Set_Int_To_Msg(self._wHD, prop_id.value)
        DCMT4Wrapper.Set_Int_To_Msg(self._wHD, prop_modifier.value)
        DCMT4Wrapper.Set_Int_To_Msg(self._wHD, prop_value)

        msg = self._Send_Msg_To_MT4(Fun_Enum.ObjectSetInteger)
        ret = msg[1]
        return bool(ret)

    def ObjectSetString(self, chart_id, object_name, prop_id, prop_value, prop_modifier = OBJ_Enum.OBJ_EMPTY):
        DCMT4Wrapper.Create_Msg(self._wHD, 5)
        DCMT4Wrapper.Set_Int_To_Msg(self._wHD, chart_id)
        DCMT4Wrapper.Set_String_To_Msg(self._wHD, object_name)
        DCMT4Wrapper.Set_Int_To_Msg(self._wHD, prop_id.value)
        DCMT4Wrapper.Set_Int_To_Msg(self._wHD, prop_modifier.value)
        DCMT4Wrapper.Set_String_To_Msg(self._wHD, prop_value)

        msg = self._Send_Msg_To_MT4(Fun_Enum.ObjectSetString)
        ret = msg[1]
        return bool(ret)

    def TextSetFont(self, name, size, flags = FW_Enum.FW_DONTCARE, orientation = 0):
        DCMT4Wrapper.Create_Msg(self._wHD, 4)
        DCMT4Wrapper.Set_String_To_Msg(self._wHD, name)
        DCMT4Wrapper.Set_Int_To_Msg(self._wHD, size)
        DCMT4Wrapper.Set_Int_To_Msg(self._wHD, flags.value)
        DCMT4Wrapper.Set_Int_To_Msg(self._wHD, orientation)

        msg = self._Send_Msg_To_MT4(Fun_Enum.TextSetFont)
        ret = msg[1]
        return bool(ret)

    def TextOut(self, text, x, y, anchor, width, height, color, color_format):
        DCMT4Wrapper.Create_Msg(self._wHD, 8)
        DCMT4Wrapper.Set_String_To_Msg(self._wHD, text)
        DCMT4Wrapper.Set_Int_To_Msg(self._wHD, x)
        DCMT4Wrapper.Set_Int_To_Msg(self._wHD, y)
        DCMT4Wrapper.Set_Int_To_Msg(self._wHD, anchor)
        DCMT4Wrapper.Set_Int_To_Msg(self._wHD, width)
        DCMT4Wrapper.Set_Int_To_Msg(self._wHD, height)
        self._data_assign_helper.Set_Color_To_Msg(self._wHD, color)
        DCMT4Wrapper.Set_Int_To_Msg(self._wHD, color_format.value)

        msg = self._Send_Msg_To_MT4(Fun_Enum.TextOut)
        ret = msg[1]
        return bool(ret)

    def TextGetSize(self, text):
        DCMT4Wrapper.Create_Msg(self._wHD, 1)
        DCMT4Wrapper.Set_String_To_Msg(self._wHD, text)

        msg = self._Send_Msg_To_MT4(Fun_Enum.TextGetSize)
        ret = msg[1]
        width = msg[2]
        height = msg[3]
        return (bool(ret), width, height)

    def ObjectDescription(self, object_name):
        DCMT4Wrapper.Create_Msg(self._wHD, 1)
        DCMT4Wrapper.Set_String_To_Msg(self._wHD, object_name)

        msg = self._Send_Msg_To_MT4(Fun_Enum.ObjectDescription)
        value = msg[1]
        return value

    def ObjectGet(self, object_name, index):
        DCMT4Wrapper.Create_Msg(self._wHD, 2)
        DCMT4Wrapper.Set_String_To_Msg(self._wHD, object_name)
        DCMT4Wrapper.Set_Int_To_Msg(self._wHD, index)

        msg = self._Send_Msg_To_MT4(Fun_Enum.ObjectGet)
        value = msg[1]
        return value

    def ObjectGetFiboDescription(self, object_name, index):
        DCMT4Wrapper.Create_Msg(self._wHD, 2)
        DCMT4Wrapper.Set_String_To_Msg(self._wHD, object_name)
        DCMT4Wrapper.Set_Int_To_Msg(self._wHD, index)

        msg = self._Send_Msg_To_MT4(Fun_Enum.ObjectGetFiboDescription)
        value = msg[1]
        return value

    def ObjectGetShiftByValue(self, object_name, value):
        DCMT4Wrapper.Create_Msg(self._wHD, 2)
        DCMT4Wrapper.Set_String_To_Msg(self._wHD, object_name)
        DCMT4Wrapper.Set_Double_To_Msg(self._wHD, value)

        msg = self._Send_Msg_To_MT4(Fun_Enum.ObjectGetShiftByValue)
        value = msg[1]
        return value

    def ObjectGetValueByShift(self, object_name, shift):
        DCMT4Wrapper.Create_Msg(self._wHD, 2)
        DCMT4Wrapper.Set_String_To_Msg(self._wHD, object_name)
        DCMT4Wrapper.Set_Int_To_Msg(self._wHD, shift)

        msg = self._Send_Msg_To_MT4(Fun_Enum.ObjectGetValueByShift)
        value = msg[1]
        return value

    def ObjectSet(self, object_name, index, value):
        DCMT4Wrapper.Create_Msg(self._wHD, 3)
        DCMT4Wrapper.Set_String_To_Msg(self._wHD, object_name)
        DCMT4Wrapper.Set_Int_To_Msg(self._wHD, index)
        DCMT4Wrapper.Set_Double_To_Msg(self._wHD, value)

        msg = self._Send_Msg_To_MT4(Fun_Enum.ObjectSet)
        value = msg[1]
        return bool(value)

    def ObjectSetFiboDescription(self, object_name, index, text):
        DCMT4Wrapper.Create_Msg(self._wHD, 3)
        DCMT4Wrapper.Set_String_To_Msg(self._wHD, object_name)
        DCMT4Wrapper.Set_Int_To_Msg(self._wHD, index)
        DCMT4Wrapper.Set_String_To_Msg(self._wHD, text)

        msg = self._Send_Msg_To_MT4(Fun_Enum.ObjectSetFiboDescription)
        value = msg[1]
        return bool(value)

    def ObjectSetText(self, object_name, text, font_size = 0, font_name = "", text_color = ""):
        DCMT4Wrapper.Create_Msg(self._wHD, 5)
        DCMT4Wrapper.Set_String_To_Msg(self._wHD, object_name)
        DCMT4Wrapper.Set_String_To_Msg(self._wHD, text)
        DCMT4Wrapper.Set_Int_To_Msg(self._wHD, font_size)
        DCMT4Wrapper.Set_String_To_Msg(self._wHD, font_name)
        self._data_assign_helper.Set_Color_To_Msg(self._wHD, text_color)

        msg = self._Send_Msg_To_MT4(Fun_Enum.ObjectSetText)
        value = msg[1]
        return bool(value)

    def ObjectType(self, object_name):
        DCMT4Wrapper.Create_Msg(self._wHD, 1)
        DCMT4Wrapper.Set_String_To_Msg(self._wHD, object_name)

        msg = self._Send_Msg_To_MT4(Fun_Enum.ObjectType)
        value = msg[1]
        return value
