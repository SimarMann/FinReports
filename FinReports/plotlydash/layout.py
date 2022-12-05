from dash import html, dcc
from FinReports import plot

def layout(dash_app):
    dash_app.layout = html.Div(children=[
        html.H1(children='Stock Reports'),
        html.Div([
            "Search: ",
            dcc.Input(id='search-input', placeholder='Search', value=False, type='text', debounce=True, required=True)
            ]),
        html.Div(id='search-output'),
        html.Table([
            html.Tr([html.Td('Market Cap'), html.Td(id='mcap')]),
            html.Tr([html.Td('EBITDA'), html.Td(id='ebitda')]),
            html.Tr([html.Td('EPS'), html.Td(id='eps')]),
            html.Tr([html.Td('P/E'), html.Td(id='pe')]),
            html.Tr([html.Td('P/EG'), html.Td(id='peg')]),
            html.Tr([html.Td('P/B'), html.Td(id='pb')]),
            html.Tr([html.Td('ROE'), html.Td(id='roe')]),
            html.Tr([html.Td('P/S'), html.Td(id='ps')]),
            ]),
        ])