## Callbacks 
from dash.dependencies import Input, Output
from dash import dcc
from FinReports import plot


def init_callbacks(dash_app):
    @dash_app.callback(
        Output(component_id='search-output', component_property='children'),
        Output(component_id='mcap', component_property='children'),
        Output(component_id='ebitda', component_property='children'),
        Output(component_id='eps', component_property='children'),
        Output(component_id='pe', component_property='children'),
        Output(component_id='peg', component_property='children'),
        Output(component_id='pb', component_property='children'),
        Output(component_id='roe', component_property='children'),
        Output(component_id='ps', component_property='children'),
        Input(component_id='search-input', component_property='value')
        )
    def update_output_search(input_value):
        if input_value is False or None:
            print(bool(input_value))
        else:
            try:
                dict = plot.data_table(input_value)
                return [dcc.Graph(id='search_output', figure=plot.ohlc_chart(input_value))], dict['Market capitalization'], dict['EBITDA'], dict['EPS'], dict['PE ratio'], dict['PEG ratio'], dict['Price to book ratio'], dict['Return on equity TTM'], dict['Price to sales ratio TTM']
            except (KeyError, TypeError, ValueError) as error:
                print(error)
         
            