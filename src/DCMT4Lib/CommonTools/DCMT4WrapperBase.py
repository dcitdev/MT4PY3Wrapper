import logging
import pathlib
import os.path
from datetime import datetime
import DCMT4Wrapper
from DCMT4Lib.CommonTools.DataStructure import *
from DCMT4Lib.MT4Funs.MarketInfoFuns import MarketInfoFuns
from DCMT4Lib.MT4Funs.CheckupFuns import CheckupFuns
from DCMT4Lib.MT4Funs.PredefinedVariablesFuns import PredefinedVariablesFuns
from DCMT4Lib.MT4Funs.ChartOperationsFuns import ChartOperationsFuns
from DCMT4Lib.MT4Funs.TradeFuns import TradeFuns
from DCMT4Lib.MT4Funs.ConversionFuns import ConversionFuns
from DCMT4Lib.MT4Funs.AccountInformationFuns import AccountInformationFuns
from DCMT4Lib.MT4Funs.TechnicalIndicatorsFuns import TechnicalIndicatorsFuns
from DCMT4Lib.MT4Funs.DateAndTimeFuns import DateAndTimeFuns
from DCMT4Lib.MT4Funs.ObjectFuns import ObjectFuns
from DCMT4Lib.MT4Funs.TestFuns import TestFuns
from DCMT4Lib.CommonTools.CommonDefine import *
from DCMT4Lib.CommonTools.EnumDefine import *
from pathlib import Path

def PrepareLogger(isToFile, isToConsole, file_name_with_path):
    # create formatter
    formatter = logging.Formatter("%(asctime)s [%(levelname)s] [%(funcName)s:%(lineno)s:0x%(thread)X] - %(message)s")
    logger = logging.getLogger("DCMT4Wrapper")
    logger.setLevel(logging.DEBUG)

    if isToFile:
        # create file handler
        now = datetime.now()
        curTime = now.strftime("%Y%m%d_%H%M%S")
        log_file_path = os.path.join(pathlib.Path(file_name_with_path).parent.resolve(), "Log_Trace_Msg_" + os.path.splitext(os.path.basename(file_name_with_path))[0] + "_PY")
        Path(log_file_path).mkdir(parents=True, exist_ok=True)
        log_file_name = os.path.join(log_file_path, os.path.basename(file_name_with_path) + "_" + curTime + ".log")

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

class DCMT4WrapperBase(object):
    def __init__(self, file_name_with_path):
        self.__logger_base = PrepareLogger(True, False, file_name_with_path)
        self.__fun_switcher = self.__Get_Fun_Switcher()
        self.__wHD = None
        self.__is_trace_msg = False
        self.__market_info_funs = None
        self.__checkup_funs = None
        self.__predefined_variables_funs = None
        self.__chart_operations_funs = None
        self.__trade_funs = None
        self.__conversion_funs = None
        self.__technical_indicators_funs = None
        self.__account_information_funs = None
        self.__date_and_time_funs = None
        self.__object_funs = None
        self.__test_funs = None
        self._param_keeper = ParamKeeper()

    # override
    def _OnInit(self):
        raise NotImplementedError

    # override
    def _OnDeinit(self, reason):
        raise NotImplementedError

    # override
    def _OnTick(self):
        raise NotImplementedError

    # override
    def _OnTimer(self):
        raise NotImplementedError

    # override
    def _OnTester(self):
        raise NotImplementedError

    # override
    def _OnChartEvent(self, callerID, lparam, dparam, sparam):
        raise NotImplementedError

    def _TestCommunication(self):
        self.__test_funs.TestCommunication()

    # Predefined Variables
    def _Bars(self):
        return self.__predefined_variables_funs.Bars()

    def _Volume(self, index):
        return self.__predefined_variables_funs.Volume(index)

    def _Open(self, index):
        return self.__predefined_variables_funs.Open(index)

    def _Close(self, index):
        return self.__predefined_variables_funs.Close(index)

    def _Ask(self):
        return self.__predefined_variables_funs.Ask()

    def _Bid(self):
        return self.__predefined_variables_funs.Bid()

    def _Time(self, index):
        return self.__predefined_variables_funs.Time(index)

    def _Digits(self):
        return self.__predefined_variables_funs.Digits()

    def _High(self, index):
        return self.__predefined_variables_funs.High(index)

    def _Low(self, index):
        return self.__predefined_variables_funs.Low(index)

    def _Point(self):
        return self.__predefined_variables_funs.Point()

    # Date and Time
    def _TimeCurrent(self, dt_struct = None):
        return self.__date_and_time_funs.TimeCurrent(dt_struct)

    def _TimeLocal(self, dt_struct = None):
        return self.__date_and_time_funs.TimeLocal(dt_struct)

    def _TimeGMT(self, dt_struct = None):
        return self.__date_and_time_funs.TimeGMT(dt_struct)

    def _TimeDaylightSavings(self):
        return self.__date_and_time_funs.TimeDaylightSavings()

    def _TimeGMTOffset(self):
        return self.__date_and_time_funs.TimeGMTOffset()

    def _TimeToStruct(self, date_time, dt_struct):
        self.__date_and_time_funs.TimeToStruct(date_time, dt_struct)

    def _StructToTime(self, dt_struct):
        return self.__date_and_time_funs.StructToTime(dt_struct)

    def _Day(self):
        return self.__date_and_time_funs.Day()

    def _DayOfWeek(self):
        return self.__date_and_time_funs.DayOfWeek()

    def _DayOfYear(self):
        return self.__date_and_time_funs.DayOfYear()

    def _Hour(self):
        return self.__date_and_time_funs.Hour()

    def _Minute(self):
        return self.__date_and_time_funs.Minute()

    def _Month(self):
        return self.__date_and_time_funs.Month()

    def _Seconds(self):
        return self.__date_and_time_funs.Seconds()

    def _Year(self):
        return self.__date_and_time_funs.Year()

    # chart operations
    def _ChartApplyTemplate(self, chart_id, filename):
        return self.__chart_operations_funs.ChartApplyTemplate(chart_id, filename)

    def _ChartSaveTemplate(self, chart_id, filename):
        return self.__chart_operations_funs.ChartSaveTemplate(chart_id, filename)

    def _ChartWindowFind(self, chart_id, indicator_shortname):
        return self.__chart_operations_funs.ChartWindowFind(chart_id, indicator_shortname)

    def _ChartTimePriceToXY(self, chart_id, sub_window, time, price):
        return self.__chart_operations_funs.ChartTimePriceToXY(chart_id, sub_window, time, price)

    def _ChartXYToTimePrice(self, chart_id, x, y):
        return self.__chart_operations_funs.ChartXYToTimePrice(chart_id, x, y)

    def _ChartOpen(self, symbol, period):
        return self.__chart_operations_funs.ChartOpen(symbol, period)

    def _ChartFirst(self):
        return self.__chart_operations_funs.ChartFirst()

    def _ChartNext(self, chart_id):
        return self.__chart_operations_funs.ChartNext(chart_id)

    def _ChartClose(self, chart_id = 0):
        return self.__chart_operations_funs.ChartClose(chart_id)

    def _ChartSymbol(self, chart_id = 0):
        return self.__chart_operations_funs.ChartSymbol(chart_id)

    def _ChartPeriod(self, chart_id = 0):
        return self.__chart_operations_funs.ChartPeriod(chart_id)

    def _ChartRedraw(self, chart_id = 0):
        return self.__chart_operations_funs.ChartRedraw(chart_id)

    def _ChartSetDouble(self, chart_id, prop_id, value):
        return self.__chart_operations_funs.ChartSetDouble(chart_id, prop_id, value)

    def _ChartSetInteger(self, chart_id, prop_id, value, sub_window = -1):
        return self.__chart_operations_funs.ChartSetInteger(chart_id, prop_id, value, sub_window)

    def _ChartSetString(self, chart_id, prop_id, str_value):
        return self.__chart_operations_funs.ChartSetString(chart_id, prop_id, str_value)

    def _ChartGetDouble(self, chart_id, prop_id, sub_window = 0):
        return self.__chart_operations_funs.ChartGetDouble(chart_id, prop_id, sub_window)

    def _ChartGetInteger(self, chart_id, prop_id, sub_window = 0):
        return self.__chart_operations_funs.ChartGetInteger(chart_id, prop_id, sub_window)

    def _ChartGetString(self, chart_id, prop_id):
        return self.__chart_operations_funs.ChartGetString(chart_id, prop_id)

    def _ChartNavigate(self, chart_id, position, shift = 0):
        return self.__chart_operations_funs.ChartNavigate(chart_id, position, shift)

    def _ChartID(self):
        return self.__chart_operations_funs.ChartID()

    def _ChartIndicatorDelete(self, chart_id, sub_window, indicator_shortname):
        return self.__chart_operations_funs.ChartIndicatorDelete(chart_id, sub_window, indicator_shortname)

    def _ChartIndicatorName(self, chart_id, sub_window, index):
        return self.__chart_operations_funs.ChartIndicatorName(chart_id, sub_window, index)

    def _ChartIndicatorsTotal(self, chart_id, sub_window):
        return self.__chart_operations_funs.ChartIndicatorsTotal(chart_id, sub_window)

    def _ChartWindowOnDropped(self):
        return self.__chart_operations_funs.ChartWindowOnDropped()

    def _ChartPriceOnDropped(self):
        return self.__chart_operations_funs.ChartPriceOnDropped()

    def _ChartTimeOnDropped(self):
        return self.__chart_operations_funs.ChartTimeOnDropped()

    def _ChartXOnDropped(self):
        return self.__chart_operations_funs.ChartXOnDropped()

    def _ChartYOnDropped(self):
        return self.__chart_operations_funs.ChartYOnDropped()

    def _ChartSetSymbolPeriod(self, chart_id, symbol, period):
        return self.__chart_operations_funs.ChartSetSymbolPeriod(chart_id, symbol, period)

    def _ChartScreenShot(self, chart_id, filename, width, height, align_mode = ALIGN_Enum.ALIGN_RIGHT):
        return self.__chart_operations_funs.ChartScreenShot(chart_id, filename, width, height, align_mode)

    def _Period(self):
        return self.__chart_operations_funs.Period()

    def _Symbol(self):
        return self.__chart_operations_funs.Symbol()

    def _WindowBarsPerChart(self):
        return self.__chart_operations_funs.WindowBarsPerChart()

    def _WindowExpertName(self):
        return self.__chart_operations_funs.WindowExpertName()

    def _WindowFind(self, name):
        return self.__chart_operations_funs.WindowFind(name)

    def _WindowFirstVisibleBar(self):
        return self.__chart_operations_funs.WindowFirstVisibleBar()

    def _WindowHandle(self, symbol, timeframe):
        return self.__chart_operations_funs.WindowHandle(symbol, timeframe)

    def _WindowIsVisible(self, index):
        return self.__chart_operations_funs.WindowIsVisible(index)

    def _WindowOnDropped(self):
        return self.__chart_operations_funs.WindowOnDropped()

    def _WindowPriceMax(self, index = 0):
        return self.__chart_operations_funs.WindowPriceMax(index)

    def _WindowPriceMin(self, index = 0):
        return self.__chart_operations_funs.WindowPriceMin(index)

    def _WindowPriceOnDropped(self):
        return self.__chart_operations_funs.WindowPriceOnDropped()

    def _WindowRedraw(self):
        return self.__chart_operations_funs.WindowRedraw()

    def _WindowScreenShot(self, filename, size_x, size_y, start_bar = -1, chart_scale = -1, chart_mode = -1):
        return self.__chart_operations_funs.WindowScreenShot(filename, size_x, size_y, start_bar, chart_scale, chart_mode)

    def _WindowTimeOnDropped(self):
        return self.__chart_operations_funs.WindowTimeOnDropped()

    def _WindowsTotal(self):
        return self.__chart_operations_funs.WindowsTotal()

    def _WindowXOnDropped(self):
        return self.__chart_operations_funs.WindowXOnDropped()

    def _WindowYOnDropped(self):
        return self.__chart_operations_funs.WindowYOnDropped()

    # Checkup
    def _GetLastError(self):
        return self.__checkup_funs.GetLastError()

    def _IsStopped(self):
        return self.__checkup_funs.IsStopped()

    def _UninitializeReason(self):
        return self.__checkup_funs.UninitializeReason()

    def _MQLInfo(self, property_id):
        return self.__checkup_funs.MQLInfo(property_id)

    def _MQLSetInteger(self, property_id, property_value):
        return self.__checkup_funs.MQLSetInteger(property_id, property_value)

    def _TerminalInfo(self, property_id):
        return self.__checkup_funs.TerminalInfo(property_id)

    def _Period(self):
        return self.__checkup_funs.Period()

    def _IsConnected(self):
        return self.__checkup_funs.IsConnected()

    def _IsDemo(self):
        return self.__checkup_funs.IsDemo()

    def _IsDllsAllowed(self):
        return self.__checkup_funs.IsDllsAllowed()

    def _IsExpertEnabled(self):
        return self.__checkup_funs.IsExpertEnabled()

    def _IsLibrariesAllowed(self):
        return self.__checkup_funs.IsLibrariesAllowed()

    def _IsOptimization(self):
        return self.__checkup_funs.IsOptimization()

    def _IsTesting(self):
        return self.__checkup_funs.IsTesting()

    def _IsTradeAllowed(self, symbol = "", tested_time = None):
        return self.__checkup_funs.IsTradeAllowed(symbol, tested_time)

    def _IsTradeContextBusy(self):
        return self.__checkup_funs.IsTradeContextBusy()

    def _IsVisualMode(self):
        return self.__checkup_funs.IsVisualMode()

    def _TerminalCompany(self):
        return self.__checkup_funs.TerminalCompany()

    def _TerminalName(self):
        return self.__checkup_funs.TerminalName()

    def _TerminalPath(self):
        return self.__checkup_funs.TerminalPath()

    # Market Info
    def _MarketInfo(self, symbol, mode_enum):
        return self.__market_info_funs.MarketInfo(symbol, mode_enum)

    def _SymbolsTotal(self, selected):
        return self.__market_info_funs.SymbolsTotal(selected)

    def _SymbolName(self, pos, selected):
        return self.__market_info_funs.SymbolName(pos, selected)

    def _SymbolSelect(self, name, select):
        return self.__market_info_funs.SymbolSelect(name, select)

    def _SymbolInfo(self, name, prop_id):
        return self.__market_info_funs.SymbolInfo(name, prop_id)

    def _SymbolInfoTick(self, symbol, tick):
        return self.__market_info_funs.SymbolInfoTick(symbol, tick)

    def _SymbolInfoSessionQuote(self, name, day_of_week, session_index):
        return self.__market_info_funs.SymbolInfoSessionQuote(name, day_of_week, session_index)

    def _SymbolInfoSessionTrade(self, name, day_of_week, session_index):
        return self.__market_info_funs.SymbolInfoSessionTrade(name, day_of_week, session_index)

    # Trade
    def _OrderClose(self, ticket, lots, price, slippage, arrow_color):
        return self.__trade_funs.OrderClose(ticket, lots, price, slippage, arrow_color)

    def _OrderCloseBy(self, ticket, opposite, arrow_color):
        return self.__trade_funs.OrderCloseBy(ticket, opposite, arrow_color)

    def _OrderClosePrice(self):
        return self.__trade_funs.OrderClosePrice()

    def _OrderCloseTime(self):
        return self.__trade_funs.OrderCloseTime()

    def _OrderComment(self):
        return self.__trade_funs.OrderComment()

    def _OrderCommission(self):
        return self.__trade_funs.OrderCommission()

    def _OrderDelete(self, ticket, arrow_color):
        return self.__trade_funs.OrderDelete(ticket, arrow_color)

    def _OrderExpiration(self):
        return self.__trade_funs.OrderExpiration()

    def _OrderLots(self):
        return self.__trade_funs.OrderLots()

    def _OrderMagicNumber(self):
        return self.__trade_funs.OrderMagicNumber()

    def _OrderModify(self, ticket, price, stoploss, takeprofit, expiration, arrow_color):
        return self.__trade_funs.OrderModify(ticket, price, stoploss, takeprofit, expiration, arrow_color)

    def _OrderOpenPrice(self):
        return self.__trade_funs.OrderOpenPrice()

    def _OrderOpenTime(self):
        return self.__trade_funs.OrderOpenTime()

    def _OrderPrint(self):
        return self.__trade_funs.OrderPrint()

    def _OrderProfit(self):
        return self.__trade_funs.OrderProfit()

    def _OrderSelect(self, index, select, pool = MODE_Enum.MODE_TRADES):
        return self.__trade_funs.OrderSelect(index, select, pool)

    def _OrderSend(self, symbol, cmd, volume, price, slippage, stoploss, takeprofit, comment = "", magic = 0, expiration = None, arrow_color = ""):
        return self.__trade_funs.OrderSend(symbol, cmd, volume, price, slippage, stoploss, takeprofit, comment, magic, expiration, arrow_color)

    def _OrdersHistoryTotal(self):
        return self.__trade_funs.OrdersHistoryTotal()

    def _OrderStopLoss(self):
        return self.__trade_funs.OrderStopLoss()

    def _OrdersTotal(self):
        return self.__trade_funs.OrdersTotal()

    def _OrderSwap(self):
        return self.__trade_funs.OrderSwap()

    def _OrderSymbol(self):
        return self.__trade_funs.OrderSymbol()

    def _OrderTakeProfit(self):
        return self.__trade_funs.OrderTakeProfit()

    def _OrderTicket(self):
        return self.__trade_funs.OrderTicket()

    def _OrderType(self):
        return self.__trade_funs.OrderType()

    # Conversion
    def _NormalizeDouble(self, value, digits):
        return self.__conversion_funs.NormalizeDouble(value, digits)

    # Accouont Information
    def _AccountInfo(self, account_enum):
        return self.__account_information_funs.AccountInfo(account_enum)

    def _AccountBalance(self):
        return self.__account_information_funs.AccountBalance()

    def _AccountCredit(self):
        return self.__account_information_funs.AccountCredit()

    def _AccountCompany(self):
        return self.__account_information_funs.AccountCompany()

    def _AccountCurrency(self):
        return self.__account_information_funs.AccountCurrency()

    def _AccountEquity(self):
        return self.__account_information_funs.AccountEquity()

    def _AccountFreeMargin(self):
        return self.__account_information_funs.AccountFreeMargin()

    def _AccountFreeMarginCheck(self, symbol, cmd, volume):
        return self.__account_information_funs.AccountFreeMarginCheck(symbol, cmd, volume)

    def _AccountFreeMarginMode(self):
        return self.__account_information_funs.AccountFreeMarginMode()

    def _AccountLeverage(self):
        return self.__account_information_funs.AccountLeverage()

    def _AccountMargin(self):
        return self.__account_information_funs.AccountMargin()

    def _AccountName(self):
        return self.__account_information_funs.AccountName()

    def _AccountNumber(self):
        return self.__account_information_funs.AccountNumber()

    def _AccountProfit(self):
        return self.__account_information_funs.AccountProfit()

    def _AccountServer(self):
        return self.__account_information_funs.AccountServer()

    def _AccountStopoutLevel(self):
        return self.__account_information_funs.AccountStopoutLevel()

    def _AccountStopoutMode(self):
        return self.__account_information_funs.AccountStopoutMode()

    def _AccountEnumCheck(self):
        return self.__account_information_funs.AccountEnumCheck()

    # Object Funs
    def _ObjectCreate(self, object_name, object_type, sub_window, time1, price1, time2=0, price2=0, time3=0, price3=0):
        return self.__object_funs.ObjectCreate(object_name, object_type, sub_window, time1, price1, time2, price2, time3, price3)

    def _ObjectName(self, object_index):
        return self.__object_funs.ObjectName(object_index)

    def _ObjectDelete(self, object_name, chart_id = -1):
        return self.__object_funs.ObjectDelete(object_name, chart_id)

    def _ObjectsDeleteAll(self, chart_id = -1, sub_window = -1, object_type = OBJ_Enum.OBJ_EMPTY, prefix = ""):
        return self.__object_funs.ObjectsDeleteAll(chart_id, sub_window, object_type, prefix)

    def _ObjectFind(self, object_name, chart_id = -1):
        return self.__object_funs.ObjectFind(object_name, chart_id)

    def _ObjectGetTimeByValue(self, chart_id, object_name, value, line_id = 0):
        return self.__object_funs.ObjectGetTimeByValue(chart_id, object_name, value, line_id)

    def _ObjectGetValueByTime(self, chart_id, object_name, time, line_id = 0):
        return self.__object_funs.ObjectGetValueByTime(chart_id, object_name, time, line_id)

    def _ObjectMove(self, object_name, point_index, time, price):
        return self.__object_funs.ObjectMove(object_name, point_index, time, price)

    def _ObjectsTotal(self, chart_id = -1, sub_window = -1, obj_type = OBJ_Enum.OBJ_EMPTY):
        return self.__object_funs.ObjectsTotal(chart_id, sub_window, obj_type)

    def _ObjectGetDouble(self, chart_id, object_name, prop_id, prop_modifier = OBJ_Enum.OBJ_EMPTY):
        return self.__object_funs.ObjectGetDouble(chart_id, object_name, prop_id, prop_modifier)

    def _ObjectGetInteger(self, chart_id, object_name, prop_id, prop_modifier = OBJ_Enum.OBJ_EMPTY):
        return self.__object_funs.ObjectGetInteger(chart_id, object_name, prop_id, prop_modifier)

    def _ObjectGetString(self, chart_id, object_name, prop_id, prop_modifier = OBJ_Enum.OBJ_EMPTY):
        return self.__object_funs.ObjectGetString(chart_id, object_name, prop_id, prop_modifier)

    def _ObjectSetDouble(self, chart_id, object_name, prop_id, prop_value, prop_modifier = OBJ_Enum.OBJ_EMPTY):
        return self.__object_funs.ObjectSetDouble(chart_id, object_name, prop_id, prop_value, prop_modifier)

    def _ObjectSetInteger(self, chart_id, object_name, prop_id, prop_value, prop_modifier = OBJ_Enum.OBJ_EMPTY):
        return self.__object_funs.ObjectSetInteger(chart_id, object_name, prop_id, prop_value, prop_modifier)

    def _ObjectSetString(self, chart_id, object_name, prop_id, prop_value, prop_modifier = OBJ_Enum.OBJ_EMPTY):
        return self.__object_funs.ObjectSetString(chart_id, object_name, prop_id, prop_value, prop_modifier)

    def _TextSetFont(self, name, size, flags = FW_Enum.FW_DONTCARE, orientation = 0):
        return self.__object_funs.TextSetFont(name, size, flags, orientation)

    def _TextOut(self, text, x, y, anchor, width, height, color, color_format):
        return self.__object_funs.TextOut(text, x, y, anchor, width, height, color, color_format)

    def _TextGetSize(self, text):
        return self.__object_funs.TextGetSize(text)

    def _ObjectDescription(self, object_name):
        return self.__object_funs.ObjectDescription(object_name)

    def _ObjectGet(self, object_name, index):
        return self.__object_funs.ObjectGet(object_name, index)

    def _ObjectGetFiboDescription(self, object_name, index):
        return self.__object_funs.ObjectGetFiboDescription(object_name, index)

    def _ObjectGetShiftByValue(self, object_name, value):
        return self.__object_funs.ObjectGetShiftByValue(object_name, value)

    def _ObjectGetValueByShift(self, object_name, shift):
        return self.__object_funs.ObjectGetValueByShift(object_name, shift)

    def _ObjectSet(self, object_name, index, value):
        return self.__object_funs.ObjectSet(object_name, index, value)

    def _ObjectSetFiboDescription(self, object_name, index, text):
        return self.__object_funs.ObjectSetFiboDescription(object_name, index, text)

    def _ObjectSetText(self, object_name, text, font_size = 0, font_name = "", text_color = ""):
        return self.__object_funs.ObjectSetText(object_name, text, font_size, font_name, text_color)

    def _ObjectType(self, object_name):
        return self.__object_funs.ObjectType(object_name)

    # Technical Indicators
    def _iMA(self, symbol, timeframe, ma_period, ma_shift, ma_method, applied_price, shift):
        return self.__technical_indicators_funs.iMA(symbol, timeframe, ma_period, ma_shift, ma_method, applied_price, shift)

    def __OnInit(self, msg):
        self._param_keeper = self.__test_funs.GetInitParams()

        ret = self._OnInit()

        DCMT4Wrapper.Create_Msg(self.__wHD, 1)
        DCMT4Wrapper.Set_Int_To_Msg(self.__wHD, ret.value)

        return ret

    def __OnDeinit(self, msg):
        self._OnDeinit(msg[1])

    def __OnTick(self, msg):
        self._OnTick()

    def __OnTimer(self, msg):
        self._OnTimer()

    def __OnTester(self, msg):
        return self._OnTester()

    def __OnChartEvent(self, msg):
        lparam = msg[2] << 32
        lparam = lparam | msg[3]
        self._OnChartEvent(msg[1], lparam, msg[4], msg[5])

    def __EndPY(self):
        pass

    def __Send_Msg_To_MT4(self, function_in_action):
        msg = None

        next_action = Fun_Enum.EndPY
        while Fun_Enum.OnDeinit != next_action:
            self.__is_trace_msg: self.__logger_base.info(f"""sending action: {function_in_action}""")
            msg = DCMT4Wrapper.Send_Msg_To_MT4(self.__wHD, function_in_action.value)
            next_action = Fun_Enum(msg[0])
            self.__is_trace_msg: self.__logger_base.info(f"""receiving action: {next_action}""")
            if Fun_Enum.EndPY == next_action:
                break

            func = self.__fun_switcher.get(next_action.value, lambda: self.__EndPY)
            func(msg)
            function_in_action = Fun_Enum.EndMT4

        if Fun_Enum.OnDeinit == next_action:
            self.__is_trace_msg: self.__logger_base.info(f"""sending action: {function_in_action}""")
            msg = DCMT4Wrapper.Send_Msg_To_MT4_No_Wait(self.__wHD, function_in_action.value)

        return msg

    def __Get_Fun_Switcher(self):
        return {
            1: self.__OnInit
            , 2: self.__OnTick
            , 3: self.__OnTester
            , 4: self.__OnChartEvent
            , 5: self.__OnTimer
            , 6: self.__OnDeinit
            , 999999: self.__EndPY
            }

    def Run(self, childFileName):
        self.__wHD = DCMT4Wrapper.Get_Handler()
        self.__market_info_funs = MarketInfoFuns(self.__logger_base, self.__wHD, self.__Send_Msg_To_MT4)
        self.__checkup_funs = CheckupFuns(self.__logger_base, self.__wHD, self.__Send_Msg_To_MT4)
        self.__predefined_variables_funs = PredefinedVariablesFuns(self.__logger_base, self.__wHD, self.__Send_Msg_To_MT4)
        self.__chart_operations_funs = ChartOperationsFuns(self.__logger_base, self.__wHD, self.__Send_Msg_To_MT4)
        self.__trade_funs = TradeFuns(self.__logger_base, self.__wHD, self.__Send_Msg_To_MT4)
        self.__conversion_funs = ConversionFuns(self.__logger_base, self.__wHD, self.__Send_Msg_To_MT4)
        self.__technical_indicators_funs = TechnicalIndicatorsFuns(self.__logger_base, self.__wHD, self.__Send_Msg_To_MT4)
        self.__account_information_funs = AccountInformationFuns(self.__logger_base, self.__wHD, self.__Send_Msg_To_MT4)
        self.__date_and_time_funs = DateAndTimeFuns(self.__logger_base, self.__wHD, self.__Send_Msg_To_MT4)
        self.__object_funs = ObjectFuns(self.__logger_base, self.__wHD, self.__Send_Msg_To_MT4)
        self.__test_funs = TestFuns(self.__logger_base, self.__wHD, self.__Send_Msg_To_MT4)
        self.__is_trace_msg = DCMT4Wrapper.Is_Trace_Msg(self.__wHD)
        self.__Send_Msg_To_MT4(Fun_Enum.OnInit)
