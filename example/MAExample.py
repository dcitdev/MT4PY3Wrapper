import pathlib
import os.path
from datetime import datetime
import sys
sys.stderr = open(os.path.join(pathlib.Path(__file__).parent.resolve(), os.path.basename(__file__) + "_" + datetime.now().strftime("%Y%m%d_%H%M%S") + "_stderr" + ".log"), "w")
import pandas as pd
import matplotlib
import logging
from DCMT4Lib.CommonTools.DCMT4WrapperBase import DCMT4WrapperBase
from DCMT4Lib.CommonTools.DataStructure import *
from DCMT4Lib.CommonTools.EnumDefine import *

def PrepareLogger_Client(isToFile, isToConsole, file_name_with_path):
    # create formatter
    formatter = logging.Formatter("%(asctime)s [%(levelname)s] [%(funcName)s:%(lineno)s:0x%(thread)X] - %(message)s")
    logger = logging.getLogger("ClientLogger")
    logger.setLevel(logging.DEBUG)

    if isToFile:
        # create file handler
        now = datetime.now()
        curTime = now.strftime("%Y%m%d_%H%M%S")
        log_file_name = os.path.join(pathlib.Path(file_name_with_path).parent.resolve(), os.path.basename(file_name_with_path) + "_" + curTime + ".log")

        fh = logging.FileHandler(log_file_name)
        fh.setLevel(logging.INFO)
        fh.setFormatter(formatter)
        # add the handlers to logger
        logger.addHandler(fh)

    if isToConsole:
        # create console handler
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(formatter)
        # add the handlers to logger
        logger.addHandler(ch)

    return logger

class MAExample(DCMT4WrapperBase):
    def __init__(self):
        super().__init__(__file__)
        self.__MAGICMA = 20131111
        self.__lots = 0.1
        self.__maximum_risk = 0.02
        self.__decrease_factor = 3
        self.__moving_period = 12
        self.__moving_shift = 6
        self.__logger = PrepareLogger_Client(True, False, __file__)
        self.__m_isFirst_OnTimer = True

    # override
    def _OnInit(self):
        self.__logger.info(f"""param: {self._param_keeper}""")
        self.__lots = self._param_keeper.double_list[0]
        self.__maximum_risk = self._param_keeper.double_list[1]
        self.__decrease_factor = self._param_keeper.int_list[0]
        self.__moving_period = self._param_keeper.int_list[1]
        self.__moving_shift = self._param_keeper.int_list[2]
        return Init_Enum.INIT_SUCCEEDED

    # override
    def _OnDeinit(self, reason):
        pass

    # override
    def _OnTick(self):
        # check for history and trading
        if self._Bars() < 100 or self._IsTradeAllowed() == False:
            return
        # calculate open orders by current symbol
        if self.__CalculateCurrentOrders(self._Symbol()) == 0:
            self.__CheckForOpen()
        else:
            self.__CheckForClose()

    # override
    def _OnTimer(self):
        if self.__m_isFirst_OnTimer:
            self.__logger.info("user debug")
            self.__m_isFirst_OnTimer = False

    # override
    def _OnTester(self):
        return 0.0

    # override
    def _OnChartEvent(self, callerID, lparam, dparam, sparam):
        pass

    def __CalculateCurrentOrders(self, symbol):
        buys = 0
        sells = 0

        for i in range(self._OrdersTotal()):
            if self._OrderSelect(i, SELECT_Enum.SELECT_BY_POS, MODE_Enum.MODE_TRADES) == False:
                break
            if self._OrderSymbol() == symbol and self._OrderMagicNumber() == self.__MAGICMA:
                order_type = self._OrderType()
                if order_type == OP_Enum.OP_BUY:
                    buys += 1
                elif order_type == OP_Enum.OP_SELL:
                    sells += 1

        return buys if buys > 0 else -sells

    def __CheckForOpen(self):
        ma = 0.0
        res = 0

        # go trading only for first tiks of new bar
        if self._Volume(0) > 1:
            return
        # get Moving Average
        ma = self._iMA("", PERIOD_Enum.PERIOD_CURRENT, self.__moving_period, self.__moving_shift, iMA_Enum.MODE_SMA, PRICE_Enum.PRICE_CLOSE, 0)
        # sell conditions
        if self._Open(1) > ma and self._Close(1) < ma:
            res = self._OrderSend(self._Symbol(), OP_Enum.OP_SELL, self.__LotsOptimized(), self._Bid(), 3, 0, 0, "", self.__MAGICMA, 0, "red")
            return
        # buy conditions
        if self._Open(1) < ma and self._Close(1) > ma:
            res = self._OrderSend(self._Symbol(), OP_Enum.OP_BUY, self.__LotsOptimized(), self._Ask(), 3, 0, 0, "", self.__MAGICMA, 0, "blue")
            return

    def __CheckForClose(self):
        ma = 0.0

        # go trading only for first tiks of new bar
        if self._Volume(0) > 1:
            return
        # get Moving Average
        ma = self._iMA("", PERIOD_Enum.PERIOD_CURRENT, self.__moving_period, self.__moving_shift, iMA_Enum.MODE_SMA, PRICE_Enum.PRICE_CLOSE, 0)

        for i in range(self._OrdersTotal()):
            if self._OrderSelect(i, SELECT_Enum.SELECT_BY_POS, MODE_Enum.MODE_TRADES) == False:
                break
            if not self._OrderMagicNumber() == self.__MAGICMA or not self._OrderSymbol() == self._Symbol():
                continue
            if self._OrderType() == OP_Enum.OP_BUY:
                if self._Open(1) > ma and self._Close(1) < ma:
                    if not self._OrderClose(self._OrderTicket(), self._OrderLots(), self._Bid(), 3, "white"):
                        self.__logger.error(f"""OrderClose error {self._GetLastError()}""")

                break
            if self._OrderType() == OP_Enum.OP_SELL:
                if self._Open(1) < ma and self._Close(1) > ma:
                    if not self._OrderClose(self._OrderTicket(), self._OrderLots(), self._Ask(), 3, "white"):
                        self.__logger.error(f"""OrderClose error {self._GetLastError()}""")

                break

    def __LotsOptimized(self):
        lot = self.__lots
        orders = self._OrdersHistoryTotal()
        losses = 0

        lot = self._NormalizeDouble(self._AccountFreeMargin() * self.__maximum_risk / 1000.0, 1)
        if self.__decrease_factor > 0:
            for i in range(orders - 1):
                if self._OrderSelect(i, SELECT_Enum.SELECT_BY_POS, MODE_Enum.MODE_HISTORY) == False:
                    self.__logger.error("Error in history")
                    break
                if not self._OrderSymbol() == self._Symbol() or self._OrderType() == OP_Enum.OP_SELL:
                    continue
                if self._OrderProfit() > 0:
                    break
                if self._OrderProfit() < 0:
                    losses += 1

            if losses > 1:
                lot = self._NormalizeDouble(lot - lot * losses / self.__decrease_factor, 1)

        return 0.1 if lot < 0.1 else lot

if __name__ == "__main__":
    algo = MAExample()
    algo.Run(__file__)
