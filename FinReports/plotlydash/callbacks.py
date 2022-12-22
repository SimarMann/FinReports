## Callbacks 
from dash.dependencies import Input, Output
from dash import dcc
from FinReports import plot


def init_callbacks(dash_app):
    @dash_app.callback(
        Output(component_id='search-output', component_property='children'),
        Input(component_id='search-input', component_property='value'),
        prevent_initial_call = True
        )
    
    def update_output_search(input_value):
        try:
            return dcc.Graph(id='search_output', figure=plot.ohlc_chart(input_value))
        except (KeyError, TypeError, ValueError) as error:
            print(error)
      
            