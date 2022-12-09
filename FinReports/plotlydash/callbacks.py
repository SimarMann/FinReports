## Callbacks 
from dash.dependencies import Input, Output
from dash import dcc
from FinReports import plot
import re

def init_callbacks(dash_app):
    @dash_app.callback(
        Output(component_id='search-output', component_property='children'),
        Output(component_id='indx', component_property='children'),
        Output(component_id='mcap', component_property='children'),
        Output(component_id='anre', component_property='children'),
        Output(component_id='anex', component_property='children'),
        Output(component_id='bs', component_property='children'),
        Output(component_id='cs', component_property='children'),
        Output(component_id='pe', component_property='children'),
        Output(component_id='ps', component_property='children'),
        Output(component_id='pb', component_property='children'),
        Output(component_id='bv', component_property='children'),
        Output(component_id='dteq', component_property='children'),
        Output(component_id='dtas', component_property='children'),
        Output(component_id='eps', component_property='children'),
        Output(component_id='epsg5', component_property='children'),
        Output(component_id='reg5', component_property='children'),
        Output(component_id='roa', component_property='children'),
        Output(component_id='npm', component_property='children'),
        Output(component_id='opm', component_property='children'),
        Output(component_id='curpri', component_property='children'),
        Output(component_id='shout', component_property='children'),
        Output(component_id='52wh', component_property='children'),
        Output(component_id='52wl', component_property='children'),
        Output(component_id='200dma', component_property='children'),
        Output(component_id='ds', component_property='children'),
        Input(component_id='search-input', component_property='value')
        )
    
    def update_output_search(input_value):
        if input_value is False or None:
            print(bool(input_value))
        else:
            try:
                dict = plot.fa_overview(input_value)
                dict_two = plot.fa_growth(input_value)
                dict_three = plot.stocks_quote(input_value)
                dict_four = plot.fa_metrics(input_value)
                ann_exp = plot.fa_income(input_value)
                return [dcc.Graph(id='search_output', figure=plot.ohlc_chart(input_value))], dict['Exchange'], dict['Market capitalization'], dict['Revenue TTM'], ann_exp, dict['Book value'], dict_four['Cash per share'], dict['PE ratio'], dict['Price to sales ratio TTM'], dict['Price to book ratio'], dict['Book total'], dict_four['Debt to equity'], dict_four['Debt to assets'], dict['EPS'], dict_two['Five y net income growth per share'], dict_two['Five y revenue growth per share'], dict['Return on assets TTM'], dict['Profit margin'], dict['Operating margin TTM'], dict_three['Price'], dict['Shares outstanding'], dict['52 week high'], dict['52 week low'], dict['200 day moving average'], dict['Dividend per share'] 
            except (KeyError, TypeError, ValueError) as error:
                print(error)
         
            