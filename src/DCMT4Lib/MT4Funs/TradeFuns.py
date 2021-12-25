from DCMT4Lib.MT4Funs.MT4FunsBase import *

# https://docs.mql4.com/trading
class TradeFuns(MT4FunsBase):
    def __init__(self, logger, wHD, Send_Msg_To_MT4):
        super().__init__(logger, wHD, Send_Msg_To_MT4)

    def OrderClose(self, ticket, lots, price, slippage, arrow_color):
        DCMT4Wrapper.Create_Msg(self._wHD, 5)
        DCMT4Wrapper.Set_Int_To_Msg(self._wHD, ticket)
        DCMT4Wrapper.Set_Double_To_Msg(self._wHD, lots)
        DCMT4Wrapper.Set_Double_To_Msg(self._wHD, price)
        DCMT4Wrapper.Set_Int_To_Msg(self._wHD, slippage)
        self._data_assign_helper.Set_Color_To_Msg(self._wHD, arrow_color)

        msg = self._Send_Msg_To_MT4(Fun_Enum.OrderClose)
        ret = msg[1]
        return bool(ret)

    def OrderCloseBy(self, ticket, opposite, arrow_color):
        DCMT4Wrapper.Create_Msg(self._wHD, 3)
        DCMT4Wrapper.Set_Int_To_Msg(self._wHD, ticket)
        DCMT4Wrapper.Set_Int_To_Msg(self._wHD, opposite)
        self._data_assign_helper.Set_Color_To_Msg(self._wHD, arrow_color)

        msg = self._Send_Msg_To_MT4(Fun_Enum.OrderCloseBy)
        ret = msg[1]
        return bool(ret)

    def OrderClosePrice(self):
        return self._Single_Return_Fun(Fun_Enum.OrderClosePrice)

    def OrderCloseTime(self):
        return self._data_assign_helper.Get_Datetime_From_Msg(self._Single_Return_Fun(Fun_Enum.OrderCloseTime))

    def OrderComment(self):
        return self._Single_Return_Fun(Fun_Enum.OrderComment)

    def OrderCommission(self):
        return self._Single_Return_Fun(Fun_Enum.OrderCommission)

    def OrderDelete(self, ticket, arrow_color):
        DCMT4Wrapper.Create_Msg(self._wHD, 2)
        DCMT4Wrapper.Set_Int_To_Msg(self._wHD, ticket)
        self._data_assign_helper.Set_Color_To_Msg(self._wHD, arrow_color)

        msg = self._Send_Msg_To_MT4(Fun_Enum.OrderCloseBy)
        ret = msg[1]
        return bool(ret)

    def OrderExpiration(self):
        return self._Single_Return_Fun(Fun_Enum.OrderExpiration)

    def OrderLots(self):
        return self._Single_Return_Fun(Fun_Enum.OrderLots)

    def OrderMagicNumber(self):
        return self._Single_Return_Fun(Fun_Enum.OrderMagicNumber)

    def OrderModify(self, ticket, price, stoploss, takeprofit, expiration, arrow_color):
        DCMT4Wrapper.Create_Msg(self._wHD, 6)
        DCMT4Wrapper.Set_Int_To_Msg(self._wHD, ticket)
        DCMT4Wrapper.Set_Double_To_Msg(self._wHD, price)
        DCMT4Wrapper.Set_Double_To_Msg(self._wHD, stoploss)
        DCMT4Wrapper.Set_Double_To_Msg(self._wHD, takeprofit)
        self._data_assign_helper.Set_Datetime_To_Msg(self._wHD, expiration)
        self._data_assign_helper.Set_Color_To_Msg(self._wHD, arrow_color)

        msg = self._Send_Msg_To_MT4(Fun_Enum.OrderModify)
        ret = msg[1]
        return bool(ret)

    def OrderOpenPrice(self):
        return self._Single_Return_Fun(Fun_Enum.OrderOpenPrice)

    def OrderOpenTime(self):
        return self._data_assign_helper.Get_Datetime_From_Msg(self._Single_Return_Fun(Fun_Enum.OrderOpenTime))

    def OrderPrint(self):
        DCMT4Wrapper.Create_Msg(self._wHD, 0)

        msg = self._Send_Msg_To_MT4(Fun_Enum.OrderPrint)

    def OrderProfit(self):
        return self._Single_Return_Fun(Fun_Enum.OrderProfit)

    def OrderSelect(self, index, select, pool):
        DCMT4Wrapper.Create_Msg(self._wHD, 3)
        DCMT4Wrapper.Set_Int_To_Msg(self._wHD, index)
        DCMT4Wrapper.Set_Int_To_Msg(self._wHD, select.value)
        DCMT4Wrapper.Set_Int_To_Msg(self._wHD, pool.value)

        msg = self._Send_Msg_To_MT4(Fun_Enum.OrderSelect)
        ret = msg[1]
        return bool(ret)

    def OrderSend(self, symbol, cmd, volume, price, slippage, stoploss, takeprofit, comment, magic, expiration, arrow_color):
        DCMT4Wrapper.Create_Msg(self._wHD, 11)
        DCMT4Wrapper.Set_String_To_Msg(self._wHD, symbol)
        DCMT4Wrapper.Set_Int_To_Msg(self._wHD, cmd.value)
        DCMT4Wrapper.Set_Double_To_Msg(self._wHD, volume)
        DCMT4Wrapper.Set_Double_To_Msg(self._wHD, price)
        DCMT4Wrapper.Set_Int_To_Msg(self._wHD, slippage)
        DCMT4Wrapper.Set_Double_To_Msg(self._wHD, stoploss)
        DCMT4Wrapper.Set_Double_To_Msg(self._wHD, takeprofit)
        DCMT4Wrapper.Set_String_To_Msg(self._wHD, comment)
        DCMT4Wrapper.Set_Int_To_Msg(self._wHD, magic)
        if None == expiration or 0 == expiration:
            DCMT4Wrapper.Set_Double_To_Msg(self._wHD, 0)
        else:
            self._data_assign_helper.Set_Datetime_To_Msg(self._wHD, expiration)
        self._data_assign_helper.Set_Color_To_Msg(self._wHD, arrow_color)

        msg = self._Send_Msg_To_MT4(Fun_Enum.OrderSend)
        ret = msg[1]
        return ret

    def OrdersHistoryTotal(self):
        return self._Single_Return_Fun(Fun_Enum.OrdersHistoryTotal)

    def OrderStopLoss(self):
        return self._Single_Return_Fun(Fun_Enum.OrderStopLoss)

    def OrdersTotal(self):
        return self._Single_Return_Fun(Fun_Enum.OrdersTotal)

    def OrderSwap(self):
        return self._Single_Return_Fun(Fun_Enum.OrderSwap)

    def OrderSymbol(self):
        return self._Single_Return_Fun(Fun_Enum.OrderSymbol)

    def OrderTakeProfit(self):
        return self._Single_Return_Fun(Fun_Enum.OrderTakeProfit)

    def OrderTicket(self):
        return self._Single_Return_Fun(Fun_Enum.OrderTicket)

    def OrderType(self):
        return OP_Enum(self._Single_Return_Fun(Fun_Enum.OrderType))
