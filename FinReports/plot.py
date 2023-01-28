import plotly.graph_objects as go
import plotly.io as pio
from FinReports import openbb
import json

# Create Template
with open('./FinReports/static/css/lux.json', 'r') as f:
    template = json.load(f)
pio.templates['LUX'] = template    
pio.templates.default = 'LUX'

def ohlc_chart(symbol):
    df = openbb.stock_load(symbol)
    fig = go.Figure(data=[go.Ohlc(x=df.index,
                                 open=df['Open'],
                                 high=df['High'],
                                 low=df['Low'],
                                 close=df['Close']
                                 )])
    
    fig.update_layout(title=symbol)
    
    return fig

def yield_linechart():
    df = openbb.usbonds()
    fig = go.Figure(data=go.Scatter(x=df[' '], y=df['Yld (%)']))
    fig.update_layout(title="US Yield Curve", xaxis_title="", yaxis_title="Yield %")
    return fig

def indicies_indicator(name, val, ref):
    
    fig = go.Figure(go.Indicator(
    title= {'align': "center", 'font':{'size': 10}, 'text': name},    
    mode = "number+delta",
    value = val,
    number = {'valueformat': ',.2f', 'font': {'size': 10}}, 
    delta = {'position': "right", 'reference': ref, 'relative': True, 'valueformat': '.2%', 'font': {'size': 10}},
    domain={"x": [0, 1], "y": [0, 1]},
    align= "center"
    ))
    
    
    return fig