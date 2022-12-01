from dash import html, dcc
from FinReports import plot

def layout(dash_app):
    dash_app.layout = html.Div(children=[
        html.H1(children='Stock Reports'),
        html.Div([
            "Search: ",
            dcc.Input(id='search-input', placeholder='Search', value='', type='text', debounce=True, required=True)
            ]),
        html.Div(id='search-output')
        ])