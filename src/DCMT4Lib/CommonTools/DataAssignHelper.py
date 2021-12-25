import DCMT4Wrapper
from DCMT4Lib.CommonTools.DataStructure import *
import logging
import pathlib
import os.path
from datetime import datetime
import time
from pathlib import Path
import matplotlib

class DataAssignHelper(object):
    def __init__(self, logger):
        self.__logger = logger
        self.__temp_var_list = list() # We need to keep the variable on python side for auto memory management

    def Assign_MqlTick(self, msg, index, tick):
        tick.time = self.Get_Datetime_From_Msg(msg[index])
        tick.bid = msg[index + 1]
        tick.ask = msg[index + 2]
        tick.last = msg[index + 3]
        tick.volume = self.Get_Int64_From_Msg(msg, index + 4, index + 5)

    def Assign_MqlDateTime(self, msg, index, date_time):
        date_time.year = msg[index]
        date_time.mon = msg[index + 1]
        date_time.day = msg[index + 2]
        date_time.hour = msg[index + 3]
        date_time.min = msg[index + 4]
        date_time.sec = msg[index + 5]
        date_time.day_of_week = msg[index + 6]
        date_time.day_of_year = msg[index + 7]

    def Assign_ParamList(self, msg, index, param_keeper):
        # handle int
        for i in range(10):
            temp_int = msg[index]
            param_keeper.int_list.append(temp_int)
            index += 1

        # handle double
        for i in range(10):
            temp_double = msg[index]
            param_keeper.double_list.append(temp_double)
            index += 1

        # handle datetime
        for i in range(10):
            temp_date = self.Get_Datetime_From_Msg(msg[index])
            param_keeper.date_list.append(temp_date)
            index += 1

        # handle string
        for i in range(10):
            temp_string = msg[index]
            param_keeper.string_list.append(temp_string)
            index += 1

    def Set_Color_To_Msg(self, wHD, color):
        if "" == color:
            DCMT4Wrapper.Set_Int_To_Msg(wHD, -1)
        else:
            DCMT4Wrapper.Set_Int_To_Msg(wHD, int(matplotlib.colors.cnames[color][1::], 16)) # remove the # from the string first, example #FF0000 -> FF0000

    def Set_Datetime_To_Msg(self, wHD, date_time):
        self.__temp_var_list = list()
        self.__temp_var_list.append(self.__Get_Double_From_Datetime(date_time))
        DCMT4Wrapper.Set_Double_To_Msg(wHD, self.__temp_var_list[0])

    def Set_MqlDateTime_To_Msg(self, wHD, date_time):
        DCMT4Wrapper.Set_Int_To_Msg(wHD, date_time.year)
        DCMT4Wrapper.Set_Int_To_Msg(wHD, date_time.mon)
        DCMT4Wrapper.Set_Int_To_Msg(wHD, date_time.day)
        DCMT4Wrapper.Set_Int_To_Msg(wHD, date_time.hour)
        DCMT4Wrapper.Set_Int_To_Msg(wHD, date_time.min)
        DCMT4Wrapper.Set_Int_To_Msg(wHD, date_time.sec)
        DCMT4Wrapper.Set_Int_To_Msg(wHD, date_time.day_of_week)
        DCMT4Wrapper.Set_Int_To_Msg(wHD, date_time.day_of_year)

    def Get_Int64_From_Msg(self, msg, hi_index, low_index):
        result = msg[hi_index] << 32
        result = result | msg[low_index]
        return result

    def Get_Datetime_From_Msg(self, serial):
        return datetime.utcfromtimestamp(serial)

    def __Get_Double_From_Datetime(self, date_time):
        return time.mktime(date_time.timetuple())
