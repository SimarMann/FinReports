import plotly.graph_objects as go
import plotly.io as pio
from FinReports import openbb
from datetime import datetime
from dateutil.relativedelta import relativedelta  
import json

# Create Template
with open('./FinReports/static/css/lux.json', 'r') as f:
    template = json.load(f)
pio.templates['LUX'] = template    
pio.templates.default = 'LUX'

def ohlc_chart(symbol):
    
    end_date = datetime.now().date()
    start_date = end_date - relativedelta(years = 1)
    start_date = start_date.strftime('%Y-%m-%d')
    
    df = openbb.openbb.stocks.load(
        symbol = symbol, 
        start_date = start_date, 
        interval = 1440, 
        end_date =  end_date, 
        prepost = False, 
        source = "YahooFinance", 
        iexrange = "ytd", 
        weekly = True, 
        monthly = False, 
        verbose = True
        ) 
    fig = go.Figure(data=[go.Ohlc(x=df.index,
                                 open=df['Open'],
                                 high=df['High'],
                                 low=df['Low'],
                                 close=df['Close']
                                 )])

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