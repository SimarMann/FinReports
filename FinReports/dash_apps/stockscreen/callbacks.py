## Callbacks 
from dash.dependencies import Input, Output
from dash import dcc
from FinReports import plot, openbb


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
        Output(component_id='price', component_property='children'),
        Output(component_id='shout', component_property='children'),
        Output(component_id='52wh', component_property='children'),
        Output(component_id='52wl', component_property='children'),
        Output(component_id='200dma', component_property='children'),
        Output(component_id='ds', component_property='children'),
        Input(component_id='search-input', component_property='value'),
        prevent_initial_call = True
        )
    
    def update_output_search(input_value):
        try:
            dict = openbb.fa_overview(input_value)
            ann_exp = openbb.fa_income(input_value)
            fa_met = openbb.fa_metrics(input_value)
            fa_growth = openbb.fa_growth(input_value)
            fa_quote = openbb.stocks_quote(input_value)
            price = fa_quote['Price']
            name = fa_quote['Name']
            
            return dcc.Graph(id='search_output', figure=plot.ohlc_chart(input_value, name), config={'displaylogo': False}), dict['Exchange'], dict['Market capitalization'], dict['Revenue TTM'], ann_exp, dict['Book value'], fa_met['Cash per share'], dict['PE ratio'], dict['Price to sales ratio TTM'], dict['Price to book ratio'], dict['Book total'], fa_met['Debt to equity'], fa_met['Debt to assets'], dict['EPS'], fa_growth['Five y net income growth per share'], fa_growth['Five y revenue growth per share'], dict['Return on assets TTM'], dict['Profit margin'], dict['Operating margin TTM'], price, dict['Shares outstanding'], dict['52 week high'], dict['52 week low'], dict['200 day moving average'], dict['Dividend per share'] 
        except (KeyError, TypeError, ValueError) as error:
            print(error)
      
            