from enum import Enum

class Fun_Enum(Enum):
    OnInit = 1
    OnTick = 2
    OnTester = 3
    OnChartEvent = 4
    OnTimer = 5
    OnDeinit = 6
    MarketInfo = 1001
    SymbolsTotal = 1002
    SymbolName = 1003
    SymbolSelect = 1004
    SymbolInfo = 1005
    SymbolInfoTick = 1008
    SymbolInfoSessionQuote = 1009
    SymbolInfoSessionTrade = 1010
    GetLastError = 2001
    IsStopped = 2002
    UninitializeReason = 2003
    MQLInfo = 2004
    MQLSetInteger = 2006
    TerminalInfo = 2007
    Period = 4031
    IsConnected = 2014
    IsDemo = 2015
    IsDllsAllowed = 2016
    IsExpertEnabled = 2017
    IsLibrariesAllowed = 2018
    IsOptimization = 2019
    IsTesting = 2020
    IsTradeAllowed = 2021
    IsTradeContextBusy = 2022
    IsVisualMode = 2023
    TerminalCompany = 2024
    TerminalName = 2025
    TerminalPath = 2026
    Bars = 3001
    Volume = 3002
    Open = 3003
    Close = 3004
    Ask = 3005
    Bid = 3006
    Time = 3007
    Digits = 3008
    High = 3009
    Low = 3010
    Point = 3011
    ChartApplyTemplate = 4001
    ChartSaveTemplate = 4002
    ChartWindowFind = 4003
    ChartTimePriceToXY = 4004
    ChartXYToTimePrice = 4005
    ChartOpen = 4006
    ChartFirst = 4007
    ChartNext = 4008
    ChartClose = 4009
    ChartSymbol = 4010
    ChartPeriod = 4011
    ChartRedraw = 4012
    ChartSetDouble = 4013
    ChartSetInteger = 4014
    ChartSetString = 4015
    ChartGetDouble = 4016
    ChartGetInteger = 4017
    ChartGetString = 4018
    ChartNavigate = 4019
    ChartID = 4020
    ChartIndicatorDelete = 4021
    ChartIndicatorName = 4022
    ChartIndicatorsTotal = 4023
    ChartWindowOnDropped = 4024
    ChartPriceOnDropped = 4025
    ChartTimeOnDropped = 4026
    ChartXOnDropped = 4027
    ChartYOnDropped = 4028
    ChartSetSymbolPeriod = 4029
    ChartScreenShot = 4030
    Symbol = 4032
    WindowBarsPerChart = 4033
    WindowExpertName = 4034
    WindowFind = 4035
    WindowFirstVisibleBar = 4036
    WindowHandle = 4037
    WindowIsVisible = 4038
    WindowOnDropped = 4039
    WindowPriceMax = 4040
    WindowPriceMin = 4041
    WindowPriceOnDropped = 4042
    WindowRedraw = 4043
    WindowScreenShot = 4044
    WindowTimeOnDropped = 4045
    WindowsTotal = 4046
    WindowXOnDropped = 4047
    WindowYOnDropped = 4048
    OrderClose = 5001
    OrderCloseBy = 5002
    OrderClosePrice = 5003
    OrderCloseTime = 5004
    OrderComment = 5005
    OrderCommission = 5006
    OrderDelete = 5007
    OrderExpiration = 5008
    OrderLots = 5009
    OrderMagicNumber = 5010
    OrderModify = 5011
    OrderOpenPrice = 5012
    OrderOpenTime = 5013
    OrderPrint = 5014
    OrderProfit = 5015
    OrderSelect = 5016
    OrderSend = 5017
    OrdersHistoryTotal = 5018
    OrderStopLoss = 5019
    OrdersTotal = 5020
    OrderSwap = 5021
    OrderSymbol = 5022
    OrderTakeProfit = 5023
    OrderTicket = 5024
    OrderType = 5025
    iAC = 6001
    iAD = 6002
    iADX = 6003
    iAlligator = 6004
    iAO = 6005
    iATR = 6006
    iBearsPower = 6007
    iBands = 6008
    iBandsOnArray = 6009
    iBullsPower = 6010
    iCCI = 6011
    iCCIOnArray = 6012
    iCustom = 6013
    iDeMarker = 6014
    iEnvelopes = 6015
    iEnvelopesOnArray = 6016
    iForce = 6017
    iFractals = 6018
    iGator = 6019
    iIchimoku = 6020
    iBWMFI = 6021
    iMomentum = 6022
    iMomentumOnArray = 6023
    iMFI = 6024
    iMA = 6025
    iMAOnArray = 6026
    iOsMA = 6027
    iMACD = 6028
    iOBV = 6029
    iSAR = 6030
    iRSI = 6031
    iRSIOnArray = 6032
    iRVI = 6033
    iStdDev = 6034
    iStdDevOnArray = 6035
    iStochastic = 6036
    iWPR = 6037
    NormalizeDouble = 7001
    AccountInfo = 8002
    AccountBalance = 8005
    AccountCredit = 8006
    AccountCompany = 8007
    AccountCurrency = 8008
    AccountEquity = 8009
    AccountFreeMargin = 8010
    AccountFreeMarginCheck = 8011
    AccountFreeMarginMode = 8012
    AccountLeverage = 8013
    AccountMargin = 8014
    AccountName = 8015
    AccountNumber = 8016
    AccountProfit = 8017
    AccountServer = 8018
    AccountStopoutLevel = 8019
    AccountStopoutMode = 8020
    AccountEnumCheck = 8101
    TimeCurrent = 9001
    TimeLocal = 9002
    TimeGMT = 9003
    TimeDaylightSavings = 9004
    TimeGMTOffset = 9005
    TimeToStruct = 9006
    StructToTime = 9007
    Day = 9008
    DayOfWeek = 9009
    DayOfYear = 9010
    Hour = 9011
    Minute = 9012
    Month = 9013
    Seconds = 9014
    TimeDay = 9015
    TimeDayOfWeek = 9016
    TimeDayOfYear = 9017
    TimeHour = 9018
    TimeMinute = 9019
    TimeMonth = 9020
    TimeSeconds = 9021
    TimeYear = 9022
    Year = 9023
    ObjectCreate = 10001
    ObjectName = 10002
    ObjectDelete = 10003
    ObjectsDeleteAll = 10004
    ObjectFind = 10005
    ObjectGetTimeByValue = 10006
    ObjectGetValueByTime = 10007
    ObjectMove = 10008
    ObjectsTotal = 10009
    ObjectGetDouble = 10010
    ObjectGetInteger = 10011
    ObjectGetString = 10012
    ObjectSetDouble = 10013
    ObjectSetInteger = 10014
    ObjectSetString = 10015
    TextSetFont = 10016
    TextOut = 10017
    TextGetSize = 10018
    ObjectDescription = 10019
    ObjectGet = 10020
    ObjectGetFiboDescription = 10021
    ObjectGetShiftByValue = 10022
    ObjectGetValueByShift = 10023
    ObjectSet = 10024
    ObjectSetFiboDescription = 10025
    ObjectSetText = 10026
    ObjectType = 10027
    GetInitParams = 999995
    TestCommunication = 999996
    TimeOut = 999997
    EndMT4 = 999998
    EndPY = 999999
