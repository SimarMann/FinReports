from dash import html, dcc, dash_table
from FinReports import plot

def layout(dash_app):
    dash_app.layout = html.Div(children=[
        html.H1(children='Stock Reports'),
        html.Div([
            "Search: ",
            dcc.Input(id='search-input', placeholder='Search', value=False, type='text', debounce=True, required=True)
            ]),
        html.Div(id='search-output'),
        html.Div([
            html.Table([
                html.Tr([html.Td('Index'), html.Td(id='indx')]),
                html.Tr([html.Td('Market Cap'), html.Td(id='mcap')]),
                html.Tr([html.Td('Annual Revenues'), html.Td(id='anre')]),
                html.Tr([html.Td('Annual Expenses'), html.Td(id='anex')]),
                html.Tr([html.Td('Book/Share'), html.Td(id='bs')]),
                html.Tr([html.Td('Cash/Share'), html.Td(id='cs')])
                ]),
            html.Table([
                html.Tr([html.Td('P/E'), html.Td(id='pe')]),
                html.Tr([html.Td('P/S'), html.Td(id='ps')]),
                html.Tr([html.Td('P/B'), html.Td(id='pb')]),
                html.Tr([html.Td('Book Value'), html.Td(id='bv')]),  
                html.Tr([html.Td('D/E'), html.Td(id='dteq')]), 
                html.Tr([html.Td('D/A'), html.Td(id='dtas')])     
                ]),
            html.Table([
                html.Tr([html.Td('EPS'), html.Td(id='eps')]),
                html.Tr([html.Td('EPS Growth 5Y'), html.Td(id='epsg5')]),
                html.Tr([html.Td('Rev Growth 5Y'), html.Td(id='reg5')]),
                html.Tr([html.Td('ROA'), html.Td(id='roa')]),
                html.Tr([html.Td('Net Profit Margin'), html.Td(id='npm')]),
                html.Tr([html.Td('Operating Margin'), html.Td(id='opm')])            
                ]),
            html.Table([
                html.Tr([html.Td('Current Price'), html.Td(id='curpri')]),
                html.Tr([html.Td('Shares Outstanding'), html.Td(id='shout')]),
                html.Tr([html.Td('52W High'), html.Td(id='52wh')]),
                html.Tr([html.Td('52W Low'), html.Td(id='52wl')]),
                html.Tr([html.Td('200 DMA'), html.Td(id='200dma')]),
                html.Tr([html.Td('Dividend/Share'), html.Td(id='ds')])            
                ])                    
            ])
        ])