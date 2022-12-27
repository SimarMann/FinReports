## Callbacks 
from dash.dependencies import Input, Output
from dash import dcc
from FinReports import plot


def init_callbacks(dash_app):
    @dash_app.callback(
        Output(component_id='search-output', component_property='children'),
        Output(component_id='indx', component_property='children'),
        Output(component_id='mcap', component_property='children'),
        Output(component_id='anre', component_property='children'),
        Output(component_id='anex', component_property='children'),
        Output(component_id='bs', component_property='children'),
        Input(component_id='search-input', component_property='value'),
        prevent_initial_call = True
        )
    
    def update_output_search(input_value):
        try:
            dict = plot.fa_overview(input_value)
            ann_exp = plot.fa_income(input_value)
            return dcc.Graph(id='search_output', figure=plot.ohlc_chart(input_value)), dict['Exchange'], dict['Market capitalization'], dict['Revenue TTM'], ann_exp, dict['Book value']
        except (KeyError, TypeError, ValueError) as error:
            print(error)
      
            