import plotly.graph_objects as go
from openbb_terminal.sdk import openbb
import pandas as pd
from datetime import datetime
    
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
    