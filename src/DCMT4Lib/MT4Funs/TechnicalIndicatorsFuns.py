from DCMT4Lib.MT4Funs.MT4FunsBase import *

class TechnicalIndicatorsFuns(MT4FunsBase):
    def __init__(self, logger, wHD, Send_Msg_To_MT4):
        super().__init__(logger, wHD, Send_Msg_To_MT4)

    def iAC(self, symbol, timeframe, shift):
        pass

    def iAD(self, symbol, timeframe, shift):
        pass

    def iADX(self, symbol, timeframe, period, applied_price, mode, shift):
        pass

    def iAlligator(self, symbol, timeframe, jaw_period, jaw_shift, teeth_period, teeth_shift, lips_period, lips_shift, ma_method, applied_price, mode, shift):
        pass

    def iAO(self, symbol, timeframe, shift):
        pass

    def iATR(self, symbol, timeframe, period, shfit):
        pass

    def iBearsPower(self, symbol, timeframe, period, applied_price, shift):
        pass

    def iBands(self, symbol, timeframe, period, deviation, bands_shift, applied_price, mode, shift):
        pass

    def iBandsOnArray(self, double_array, total, period, deviation, bands_shift, mode, shift):
        pass

    def iBullsPower(self, symbol, timeframe, period, applied_price, shift):
        pass

    def iCCI(self, symbol, timeframe, period, applied_price, shift):
        pass

    def iCCIOnArray(self, double_array, total, period, shift):
        pass

    def iCustom(self, symbol, timeframe, name, mode, shift, custom_fields):
        pass

    def iDeMarker(self, symbol, timeframe, period, shift):
        pass

    def iEnvelopes(self, symbol, timeframe, ma_period, ma_method, ma_shfit, applied_price, deviation, mode, shift):
        pass

    def iEnvelopesOnArray(self, double_array, total, ma_period, ma_method, ma_shift, deviation, mode, shfit):
        pass

    def iForce(self, symbol, timeframe, period, ma_method, applied_price, shift):
        pass

    def iFractals(self, symbol, timeframe, mode, shift):
        pass

    def iGator(self, symbol, timeframe, jaw_period, jaw_shift, teeth_period, teeth_shift, lips_period, lips_shift, ma_method, applied_price, mode, shift):
        pass

    def iIchimoku(self, symbol, timeframe, tenkan_sen, kijun_sen, senkou_span_b, mode, shift):
        pass

    def iBWMFI(self, symbol, timeframe, shift):
        pass

    def iMomentum(self, symbol, timeframe, period, applied_price, shfit):
        pass

    def iMomentumOnArray(self, double_array, total, period, shift):
        pass

    def iMFI(self, symbol, timeframe, period, shift):
        pass

    def iMA(self, symbol, timeframe, ma_period, ma_shift, ma_method, applied_price, shift):
        DCMT4Wrapper.Create_Msg(self._wHD, 7)
        DCMT4Wrapper.Set_String_To_Msg(self._wHD, symbol)
        DCMT4Wrapper.Set_Int_To_Msg(self._wHD, timeframe.value)
        DCMT4Wrapper.Set_Int_To_Msg(self._wHD, ma_period)
        DCMT4Wrapper.Set_Int_To_Msg(self._wHD, ma_shift)
        DCMT4Wrapper.Set_Int_To_Msg(self._wHD, ma_method.value)
        DCMT4Wrapper.Set_Int_To_Msg(self._wHD, applied_price.value)
        DCMT4Wrapper.Set_Int_To_Msg(self._wHD, shift)

        msg = self._Send_Msg_To_MT4(Fun_Enum.iMA)
        ma = msg[1]
        return ma

    def iMAOnArray(self, double_array, total, ma_period, ma_shift, ma_method, shift):
        pass

    def iOsMA(self, symbol, timeframe, fast_ema_period, slow_ema_period, signal_period, applied_price, shift):
        pass

    def iMACD(self, symbol, timeframe, fast_ema_period, slow_ema_period, signal_period, applied_price, mode, shift):
        pass

    def iOBV(self, symbol, timeframe, applied_price, shift):
        pass

    def iSAR(self, symbol, timeframe, step, maximum, shift):
        pass

    def iRSI(self, symbol, timeframe, period, applied_price, shift):
        pass

    def iRSIOnArray(self, double_array, total, period, shift):
        pass

    def iRVI(self, symbol, timeframe, period, mode, shift):
        pass

    def iStdDev(self, symbol, timeframe, ma_period, ma_shift, ma_method, applied_price, shift):
        pass

    def iStdDevOnArray(self, double_array, total, ma_period, ma_shift, ma_method, shift):
        pass

    def iStochastic(self, symbol, timeframe, Kperiod, Dperiod, slowing, method, price_field, mode, shift):
        pass

    def iWPR(self, symbol, timeframe, period, shift):
        pass
