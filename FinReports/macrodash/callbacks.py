## Callbacks 
from dash.dependencies import Input, Output, State
from dash import html, dcc
from FinReports import plot, openbb
import asyncio


def init_callbacks(dash_app):
    @dash_app.callback(
        Output(component_id='eqfut-output', component_property='children'),
        Input(component_id='eqfut-input', component_property='n_clicks'),
        State('eqfut-output', 'children'),
        prevent_initial_call=True
        )
    def eqfut_button(n_clicks, children):
        if (n_clicks % 2) != 0:
            NAS100 = openbb.load_futures("NQ")
            SP500 = openbb.load_futures("ES")
            R2000 = openbb.load_futures("RTY")    
            children = html.Div(className='px-3 py-3', children=[
                html.Table(className='table table-hover', children=[
                    html.Tr(dcc.Graph(figure=plot.indicies_indicator('Nasdaq 100', NAS100[1], NAS100[0]), className='indicator-data', config = {'displayModeBar': False})),
                    html.Tr(dcc.Graph(figure=plot.indicies_indicator('S&P 500', SP500[1], SP500[0]), className='indicator-data my-3', config = {'displayModeBar': False})),
                    html.Tr(dcc.Graph(figure=plot.indicies_indicator('Russell 2000', R2000[1], R2000[0]), className='indicator-data mb-3', config = {'displayModeBar': False}))
                ])
            ])
        else:            
            children = html.Div(children='')
        
        return children
    
    
    @dash_app.callback(
        Output(component_id='crypto-output', component_property='children'),
        Input(component_id='crypto-input', component_property='n_clicks'),
        State('crypto-output', 'children'),
        prevent_initial_call=True
        )
    
    def crypto_button(n, child):
        if (n % 2) != 0:
            BTC = openbb.crypto_1mdelta('btc')
            ETH = openbb.crypto_1mdelta('eth')
            child = html.Div(className='px-3 py-3', children=[
                html.Table(className='table table-hover', children=[
                    html.Tr(dcc.Graph(figure=plot.indicies_indicator('BTC', BTC.iloc[1]['Adj Close'], BTC.iloc[0]['Adj Close']), className='indicator-data mb-3', config = {'displayModeBar': False})),
                    html.Tr(dcc.Graph(figure=plot.indicies_indicator('ETH', ETH.iloc[1]['Adj Close'], ETH.iloc[0]['Adj Close']), className='indicator-data', config = {'displayModeBar': False}))                                        
                ])
            ])

            
        else:
            child = html.Div(children='')
        
        return child 
    
    
    @dash_app.callback(
        Output(component_id='commod-output', component_property='children'),
        Input(component_id='commod-input', component_property='n_clicks'),
        State('commod-output', 'children'),
        prevent_initial_call=True
        )
    
    def commod_button(n, child):
        if (n % 2) != 0:
            GOLD = openbb.load_futures("GC")
            SILV = openbb.load_futures("SI")
            COP = openbb.load_futures("HG")
            OIL = openbb.load_futures("CL")
            NATG = openbb.load_futures("NG")
            WHEA = openbb.load_futures("KE") 
            child = html.Div(className='px-3 py-3', children=[
                html.Table(className='table table-hover', children=[
                    html.Tr(dcc.Graph(figure=plot.indicies_indicator('Gold', GOLD[1], GOLD[0]), className='indicator-data mb-3', config = {'displayModeBar': False})),
                    html.Tr(dcc.Graph(figure=plot.indicies_indicator('Silver', SILV[1], SILV[0]), className='indicator-data mb-3', config = {'displayModeBar': False})),
                    html.Tr(dcc.Graph(figure=plot.indicies_indicator('Copper', COP[1], COP[0]), className='indicator-data mb-3', config = {'displayModeBar': False})),
                    html.Tr(dcc.Graph(figure=plot.indicies_indicator('Oil', OIL[1], OIL[0]), className='indicator-data mb-3', config = {'displayModeBar': False})),
                    html.Tr(dcc.Graph(figure=plot.indicies_indicator('Nat Gas', NATG[1], NATG[0]), className='indicator-data mb-3', config = {'displayModeBar': False})),
                    html.Tr(dcc.Graph(figure=plot.indicies_indicator('Wheat', WHEA[1], WHEA[0]), className='indicator-data mb-3', config = {'displayModeBar': False}))                                        
                ])
            ])

            
        else:
            child = html.Div(children='')
        
        return child     
 