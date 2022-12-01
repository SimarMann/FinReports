## Callbacks 
from dash.dependencies import Input, Output
from dash import dcc
from FinReports import plot


def init_callbacks(dash_app):
    @dash_app.callback(
        Output(component_id='search-output', component_property='children'),
        Input(component_id='search-input', component_property='value')
        )
    def update_output_search(input_value):
        if input_value == '':
            return ''
        elif (KeyError, TypeError, ValueError):
            return f'{input_value} not found'
        else:
            return [dcc.Graph(id='search_output', figure=plot.ohlc_chart(input_value))]