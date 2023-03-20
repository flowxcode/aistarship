import pandas as pd
import numpy as np

def calculate_rsi(data, period=14):
    delta = data['close'].diff()
    up = delta.where(delta > 0, 0)
    down = -delta.where(delta < 0, 0)
    ema_up = up.ewm(com=period - 1, min_periods=period).mean()
    ema_down = down.ewm(com=period - 1, min_periods=period).mean()
    rs = ema_up / ema_down
    rsi = 100 - (100 / (1 + rs))
    return rsi
