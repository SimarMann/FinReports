from dash import Dash, html, dcc, dash_table
import pandas as pd
from openbb_terminal.sdk import openbb
import plotly.graph_objects as go
from datetime import datetime

def init_dashboard(flask_app):
    """Create a Plotly Dash dashboard."""
    dash_app = Dash(
        server=flask_app,
        routes_pathname_prefix='/dashboard/',
        external_stylesheets=[
            '../static/style.css',
        ]
    )
    
    df = openbb.stocks.load(
        symbol = 'SPY',
        start_date = '2022-06-01',
        end_date = '2022-11-01',
        interval = 1440,
        prepost = False,
        source = 'YahooFinance',
        weekly = False,
        monthly = True,
        )
    
    print(df)
    fig = go.Figure(data=go.Ohlc(x=df.index,
                    open=df['Open'],
                    high=df['High'],
                    low=df['Low'],
                    close=df['Close']
                    ))
    
    # Create Dash Layout
    dash_app.layout = html.Div(children=[
        html.H1(children='Hello Dash'),
        html.Div(children='''dash dash dash'''),
        dcc.Graph(figure=fig)
        ])

    return dash_app.server