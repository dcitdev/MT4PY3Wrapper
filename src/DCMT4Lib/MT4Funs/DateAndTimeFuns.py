from DCMT4Lib.MT4Funs.MT4FunsBase import *

class DateAndTimeFuns(MT4FunsBase):
    def __init__(self, logger, wHD, Send_Msg_To_MT4):
        super().__init__(logger, wHD, Send_Msg_To_MT4)

    def TimeCurrent(self, dt_struct):
        return self.__TimeHandler(dt_struct, Fun_Enum.TimeCurrent)

    def TimeLocal(self, dt_struct):
        return self.__TimeHandler(dt_struct, Fun_Enum.TimeLocal)

    def TimeGMT(self, dt_struct):
        return self.__TimeHandler(dt_struct, Fun_Enum.TimeGMT)

    def TimeDaylightSavings(self):
        DCMT4Wrapper.Create_Msg(self._wHD, 0)

        msg = self._Send_Msg_To_MT4(Fun_Enum.TimeDaylightSavings)
        savings = msg[1]
        return savings

    def TimeGMTOffset(self):
        DCMT4Wrapper.Create_Msg(self._wHD, 0)

        msg = self._Send_Msg_To_MT4(Fun_Enum.TimeGMTOffset)
        offset = msg[1]
        return offset

    def TimeToStruct(self, date_time, dt_struct):
        DCMT4Wrapper.Create_Msg(self._wHD, 1)
        self._data_assign_helper.Set_Datetime_To_Msg(self._wHD, date_time)

        msg = self._Send_Msg_To_MT4(Fun_Enum.TimeToStruct)
        self._data_assign_helper.Assign_MqlDateTime(msg, 1, dt_struct)

    def StructToTime(self, dt_struct):
        DCMT4Wrapper.Create_Msg(self._wHD, 8)
        self._data_assign_helper.Set_MqlDateTime_To_Msg(self._wHD, dt_struct)

        msg = self._Send_Msg_To_MT4(Fun_Enum.StructToTime)
        date_time = self._data_assign_helper.Get_Datetime_From_Msg(msg[1])
        return date_time

    def Day(self):
        DCMT4Wrapper.Create_Msg(self._wHD, 0)

        msg = self._Send_Msg_To_MT4(Fun_Enum.Day)
        the_day = msg[1]
        return the_day

    def DayOfWeek(self):
        DCMT4Wrapper.Create_Msg(self._wHD, 0)

        msg = self._Send_Msg_To_MT4(Fun_Enum.DayOfWeek)
        day_of_week = msg[1]
        return day_of_week

    def DayOfYear(self):
        DCMT4Wrapper.Create_Msg(self._wHD, 0)

        msg = self._Send_Msg_To_MT4(Fun_Enum.DayOfYear)
        day_of_year = msg[1]
        return day_of_year

    def Hour(self):
        DCMT4Wrapper.Create_Msg(self._wHD, 0)

        msg = self._Send_Msg_To_MT4(Fun_Enum.Hour)
        hour = msg[1]
        return hour

    def Minute(self):
        DCMT4Wrapper.Create_Msg(self._wHD, 0)

        msg = self._Send_Msg_To_MT4(Fun_Enum.Minute)
        minute = msg[1]
        return minute

    def Month(self):
        DCMT4Wrapper.Create_Msg(self._wHD, 0)

        msg = self._Send_Msg_To_MT4(Fun_Enum.Month)
        month = msg[1]
        return month

    def Seconds(self):
        DCMT4Wrapper.Create_Msg(self._wHD, 0)

        msg = self._Send_Msg_To_MT4(Fun_Enum.Seconds)
        seconds = msg[1]
        return seconds

    def Year(self):
        DCMT4Wrapper.Create_Msg(self._wHD, 0)

        msg = self._Send_Msg_To_MT4(Fun_Enum.Year)
        year = msg[1]
        return year

    def __TimeHandler(self, dt_struct, fun_type):
        DCMT4Wrapper.Create_Msg(self._wHD, 1)
        if not None == dt_struct:
            DCMT4Wrapper.Set_Int_To_Msg(self._wHD, 1)
        else:
            DCMT4Wrapper.Set_Int_To_Msg(self._wHD, 0)

        msg = self._Send_Msg_To_MT4(fun_type)
        date_time = self._data_assign_helper.Get_Datetime_From_Msg(msg[1])
        if not None == dt_struct:
            self._data_assign_helper.Assign_MqlDateTime(msg, 2, dt_struct)
        return date_time
