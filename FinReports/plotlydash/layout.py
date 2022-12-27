from dash import html, dcc
from dash_svg import Svg, Path

def layout(dash_app):
    dash_app.layout = html.Div(className='grid-container body-height', children=[
        html.Nav(className='ms-3 d-flex flex-column flex-shrink-0 p-3 nav-size nav-fixed grid-nav shadow p-3 mt-3 bg-white rounded-pill', children=[
            Svg([
                Path(stroke='none', d='M0 0h24v24H0z', fill='none'),
                Path(d='M4.028 7.82a9 9 0 1 0 12.823 -3.4c-1.636 -1.02 -3.064 -1.02 -4.851 -1.02h-1.647'),
                Path(d='M4.914 9.485c-1.756 -1.569 -.805 -5.38 .109 -6.17c.086 .896 .585 1.208 1.111 1.685c.88 -.275 1.313 -.282 1.867 0c.82 -.91 1.694 -2.354 2.628 -2.093c-1.082 1.741 -.07 3.733 1.371 4.173c-.17 .975 -1.484 1.913 -2.76 2.686c-1.296 .938 -.722 1.85 0 2.234c.949 .506 3.611 -.995 4.545 .354c-1.698 .102 -1.536 3.107 -3.983 2.727c2.523 .957 4.345 .462 5.458 -.34c1.965 -1.52 2.879 -3.542 2.879 -5.557c-.014 -1.398 .194 -2.695 -1.26 -4.75')
                ], width='48', height='48', viewBox='0 0 24 24', stroke='#000', fill='none'),
            html.Hr(className='my-5'),
            html.Ul(className='nav nav-pills flex-column mb-auto', children=[
                html.Li(children=[
                    html.A(href='/', className='nav-link text-center rounded', children=[
                        Svg([
                            Path(d='M8.707 1.5a1 1 0 0 0-1.414 0L.646 8.146a.5.5 0 0 0 .708.708L2 8.207V13.5A1.5 1.5 0 0 0 3.5 15h9a1.5 1.5 0 0 0 1.5-1.5V8.207l.646.647a.5.5 0 0 0 .708-.708L13 5.793V2.5a.5.5 0 0 0-.5-.5h-1a.5.5 0 0 0-.5.5v1.293L8.707 1.5ZM13 7.207V13.5a.5.5 0 0 1-.5.5h-9a.5.5 0 0 1-.5-.5V7.207l5-5 5 5Z')
                        ], width='16', height='16', fill='currentColor', className='bi bi-house', viewBox='0 0 16 16')
                    ])
                ]),
                html.Li(className='mt-3', children=[
                    html.A(href='/stockscreen/', className='dash-link nav-link active text-center rounded', children=[
                        Svg([
                            Path(d='M4 11a1 1 0 1 1 2 0v1a1 1 0 1 1-2 0v-1zm6-4a1 1 0 1 1 2 0v5a1 1 0 1 1-2 0V7zM7 9a1 1 0 0 1 2 0v3a1 1 0 1 1-2 0V9z'),
                            Path(d='M4 1.5H3a2 2 0 0 0-2 2V14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V3.5a2 2 0 0 0-2-2h-1v1h1a1 1 0 0 1 1 1V14a1 1 0 0 1-1 1H3a1 1 0 0 1-1-1V3.5a1 1 0 0 1 1-1h1v-1z'),
                            Path(d='M9.5 1a.5.5 0 0 1 .5.5v1a.5.5 0 0 1-.5.5h-3a.5.5 0 0 1-.5-.5v-1a.5.5 0 0 1 .5-.5h3zm-3-1A1.5 1.5 0 0 0 5 1.5v1A1.5 1.5 0 0 0 6.5 4h3A1.5 1.5 0 0 0 11 2.5v-1A1.5 1.5 0 0 0 9.5 0h-3z')
                        ], width="16", height="16", fill="currentColor", className="bi bi-clipboard-data", viewBox="0 0 16 16")
                    ])
                ])
            ])
        ]),
        html.Div(className='grid-search search-size', children=[
            dcc.Input(id='search-input', className='form-control me-sm-2', placeholder='Search', type='text', debounce=True),
            html.H5(className='mt-3 mb-3 ms-3', children='StockScreen'),
            html.Div(id='search-output'),
            html.Div(className='card bg-secondary mt-4 data-card pt-4 px-4', children=[
                html.H3(className='text-center', children=[
                    Svg([
                        Path(d='M4 6a2 2 0 1 1 0 4 2 2 0 0 1 0-4zm2.625.547a3 3 0 0 0-5.584.953H.5a.5.5 0 0 0 0 1h.541A3 3 0 0 0 7 8a1 1 0 0 1 2 0 3 3 0 0 0 5.959.5h.541a.5.5 0 0 0 0-1h-.541a3 3 0 0 0-5.584-.953A1.993 1.993 0 0 0 8 6c-.532 0-1.016.208-1.375.547zM14 8a2 2 0 1 1-4 0 2 2 0 0 1 4 0z')
                        ], width="40", height="40", fill="black", className="bi bi-eyeglasses", viewBox="0 0 16 16"), 
                    'overview'
                    ]),
                html.Hr(),
                html.Table(className='table table-hover', children=[
                    html.Tr([html.Th('Index'), html.Td(id='indx')]),
                    html.Tr([html.Th('Market Cap'), html.Td(id='mcap')]),
                    html.Tr([html.Th('Annual Revenues'), html.Td(id='anre')]),
                    html.Tr([html.Th('Annual Expenses'), html.Td(id='anex')]),
                    html.Tr([html.Th('Book/Share'), html.Td(id='bs')]),
                    html.Tr([html.Th('Cash/Share'), html.Td('N/A', id='cs')])
                ])
            ])
        ])
    ])