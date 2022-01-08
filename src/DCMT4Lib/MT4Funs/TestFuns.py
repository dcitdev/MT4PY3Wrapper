from DCMT4Lib.MT4Funs.MT4FunsBase import *

class TestFuns(MT4FunsBase):
    def __init__(self, logger, wHD, Send_Msg_To_MT4):
        super().__init__(logger, wHD, Send_Msg_To_MT4)

    def TestCommunication(self):
        DCMT4Wrapper.Create_Msg(self._wHD, 7)
        DCMT4Wrapper.Set_String_To_Msg(self._wHD, "Message from python start")
        DCMT4Wrapper.Set_Int_To_Msg(self._wHD, 1)
        DCMT4Wrapper.Set_Int_To_Msg(self._wHD, 2)
        DCMT4Wrapper.Set_String_To_Msg(self._wHD, "Message from python mid")
        DCMT4Wrapper.Set_Double_To_Msg(self._wHD, 1.1)
        DCMT4Wrapper.Set_Double_To_Msg(self._wHD, 1.2)
        DCMT4Wrapper.Set_String_To_Msg(self._wHD, "Message from python end")

        msg = self._Send_Msg_To_MT4(Fun_Enum.TestCommunication)

        self._logger.info("After TestCommunication")
        self._logger.info(f"""{msg}""")
        str_001 = msg[1]
        int_001 = msg[2]
        int_002 = msg[3]
        str_002 = msg[4]
        double_001 = msg[5]
        double_002 = msg[6]
        str_003 = msg[7]
        self._logger.info(f"""we get: {str_001}""")
        self._logger.info(f"""we get: {int_001}""")
        self._logger.info(f"""we get: {int_002}""")
        self._logger.info(f"""we get: {str_002}""")
        self._logger.info(f"""we get: {double_001}""")
        self._logger.info(f"""we get: {double_002}""")
        self._logger.info(f"""we get: {str_003}""")


    def GetInitParams(self):
        DCMT4Wrapper.Create_Msg(self._wHD, 0)

        msg = self._Send_Msg_To_MT4(Fun_Enum.GetInitParams)

        param_keeper = ParamKeeper()
        self._data_assign_helper.Assign_ParamList(msg, 1, param_keeper)

        return param_keeper
