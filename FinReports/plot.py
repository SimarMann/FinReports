import plotly.graph_objects as go
from openbb_terminal.sdk import openbb
import pandas as pd
from datetime import datetime
import re
    
def ohlc_chart(symbol):
    df = openbb.stocks.load(
        symbol = symbol,
        start_date = '2022-06-01',
        end_date = '2022-11-01',
        interval = 1440,
        prepost = False,
        source = 'YahooFinance',
        weekly = False,
        monthly = True
        )
    fig = go.Figure(data=go.Ohlc(x=df.index,
                                 open=df['Open'],
                                 high=df['High'],
                                 low=df['Low'],
                                 close=df['Close']
                                 ))
    
    return fig

def fa_overview(symbol):
    df = openbb.stocks.fa.overview(symbol)
    df = df.to_dict()
    df = df[0]
    df['Book total']= hum_format(float(df['Book value'])*(num_format(df['Shares outstanding'])))
    return df

## Requires API_KEY_FINANCIALMODELINGPREP
def fa_metrics(symbol):
    df = openbb.stocks.fa.metrics(symbol, 1, False)
    df = df.to_dict()
    df = df[0]
    return df

## Convert from scientific notation to float
def fa_income(symbol):
    df = openbb.stocks.fa.income(symbol, False, False, "YahooFinance", 1)
    print(df)
    return df

## Requires API_KEY_FINANCIALMODELINGPREP
def fa_growth(symbol):
    df = openbb.stocks.fa.growth(symbol, 1, False)
    df = df.to_dict()
    df = df[0]
    return df

def hum_format(num):
    num = float('{:.3g}'.format(num))
    magnitude = 0
    while abs(num) >= 1000:
        magnitude += 1
        num /= 1000.0
    return '{}{}'.format('{:f}'.format(num).rstrip('0').rstrip('.'), ['', 'K', 'M', 'B', 'T'][magnitude])
    
def num_format(num):
    if type(num) == float or type(num) == int:
        return num
    if 'K' in num:
        if len(num) > 1:
            return float(num.replace('K', '')) * 1000
        return 1000.0
    if 'M' in num:
        if len(num) > 1:
            return float(num.replace('M', '')) * 1000000
        return 1000000.0
    if 'B' in num:
        return float(num.replace('B', '')) * 1000000000
    return 0.0