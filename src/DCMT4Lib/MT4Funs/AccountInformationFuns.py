from DCMT4Lib.MT4Funs.MT4FunsBase import *

# https://docs.mql4.com/account
class AccountInformationFuns(MT4FunsBase):
    def __init__(self, logger, wHD, Send_Msg_To_MT4):
        super().__init__(logger, wHD, Send_Msg_To_MT4)

    def AccountInfo(self, account_enum):
        DCMT4Wrapper.Create_Msg(self._wHD, 1)
        DCMT4Wrapper.Set_Int_To_Msg(self._wHD, account_enum.value)

        msg = self._Send_Msg_To_MT4(Fun_Enum.AccountInfo)
        account_info = msg[1]
        return account_info

    def AccountBalance(self):
        DCMT4Wrapper.Create_Msg(self._wHD, 0)

        msg = self._Send_Msg_To_MT4(Fun_Enum.AccountBalance)
        balance = msg[1]
        return balance

    def AccountCredit(self):
        DCMT4Wrapper.Create_Msg(self._wHD, 0)

        msg = self._Send_Msg_To_MT4(Fun_Enum.AccountCredit)
        credit = msg[1]
        return credit

    def AccountCompany(self):
        DCMT4Wrapper.Create_Msg(self._wHD, 0)

        msg = self._Send_Msg_To_MT4(Fun_Enum.AccountCompany)
        company = msg[1]
        return company

    def AccountCurrency(self):
        DCMT4Wrapper.Create_Msg(self._wHD, 0)

        msg = self._Send_Msg_To_MT4(Fun_Enum.AccountCurrency)
        currency = msg[1]
        return currency

    def AccountEquity(self):
        DCMT4Wrapper.Create_Msg(self._wHD, 0)

        msg = self._Send_Msg_To_MT4(Fun_Enum.AccountEquity)
        equity = msg[1]
        return equity

    def AccountFreeMargin(self):
        DCMT4Wrapper.Create_Msg(self._wHD, 0)

        msg = self._Send_Msg_To_MT4(Fun_Enum.AccountFreeMargin)
        margin = msg[1]
        return margin

    def AccountFreeMarginCheck(self, symbol, cmd, volume):
        DCMT4Wrapper.Create_Msg(self._wHD, 3)
        DCMT4Wrapper.Set_String_To_Msg(self._wHD, symbol)
        DCMT4Wrapper.Set_Int_To_Msg(self._wHD, cmd.value)
        DCMT4Wrapper.Set_Double_To_Msg(self._wHD, volume)

        msg = self._Send_Msg_To_MT4(Fun_Enum.AccountFreeMarginCheck)
        check = msg[1]
        return check

    def AccountFreeMarginMode(self):
        DCMT4Wrapper.Create_Msg(self._wHD, 0)

        msg = self._Send_Msg_To_MT4(Fun_Enum.AccountFreeMarginMode)
        value = msg[1]
        return value

    def AccountLeverage(self):
        DCMT4Wrapper.Create_Msg(self._wHD, 0)

        msg = self._Send_Msg_To_MT4(Fun_Enum.AccountLeverage)
        value = msg[1]
        return value

    def AccountMargin(self):
        DCMT4Wrapper.Create_Msg(self._wHD, 0)

        msg = self._Send_Msg_To_MT4(Fun_Enum.AccountMargin)
        value = msg[1]
        return value

    def AccountName(self):
        DCMT4Wrapper.Create_Msg(self._wHD, 0)

        msg = self._Send_Msg_To_MT4(Fun_Enum.AccountName)
        value = msg[1]
        return value

    def AccountNumber(self):
        DCMT4Wrapper.Create_Msg(self._wHD, 0)

        msg = self._Send_Msg_To_MT4(Fun_Enum.AccountNumber)
        value = msg[1]
        return value

    def AccountProfit(self):
        DCMT4Wrapper.Create_Msg(self._wHD, 0)

        msg = self._Send_Msg_To_MT4(Fun_Enum.AccountProfit)
        value = msg[1]
        return value

    def AccountServer(self):
        DCMT4Wrapper.Create_Msg(self._wHD, 0)

        msg = self._Send_Msg_To_MT4(Fun_Enum.AccountServer)
        value = msg[1]
        return value

    def AccountStopoutLevel(self):
        DCMT4Wrapper.Create_Msg(self._wHD, 0)

        msg = self._Send_Msg_To_MT4(Fun_Enum.AccountStopoutLevel)
        value = msg[1]
        return value

    def AccountStopoutMode(self):
        DCMT4Wrapper.Create_Msg(self._wHD, 0)

        msg = self._Send_Msg_To_MT4(Fun_Enum.AccountStopoutMode)
        value = msg[1]
        return value

    def AccountEnumCheck(self):
        DCMT4Wrapper.Create_Msg(self._wHD, 0)

        msg = self._Send_Msg_To_MT4(Fun_Enum.AccountEnumCheck)
        enum_list = list()
        for i in range(30):
            temp_enum = msg[i+1]
            enum_list.append(temp_enum)
        return enum_list
