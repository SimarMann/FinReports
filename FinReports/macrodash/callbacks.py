## Callbacks 
from dash.dependencies import Input, Output, State
from dash import html, dcc
from FinReports import plot, openbb


def init_callbacks(dash_app):
    @dash_app.callback(
        Output(component_id='eqfut-output', component_property='children'),
        Input(component_id='eqfut-input', component_property='n_clicks'),
        State('eqfut-output', 'children'),
        prevent_initial_call=True
        )
    
    def eqfut_button(n_clicks, children):
        if (n_clicks % 2) != 0:
            indfuts = openbb.indices_futures()
            NAS100 = indfuts.loc['Nasdaq 100']
            SP500 = indfuts.loc['S&P 500']
            DJIA = indfuts.loc['DJIA'] 
            R2000 = indfuts.loc['Russell 2000']
            VIX = indfuts.loc['VIX']        
            children = html.Div(className='px-3 py-3', children=[
                html.Table(className='table table-hover', children=[
                    html.Tr(dcc.Graph(figure=plot.indicies_indicator(NAS100.name, NAS100['last'], NAS100['prevClose']), className='indicator-data', config = {'displayModeBar': False})),
                    html.Tr(dcc.Graph(figure=plot.indicies_indicator(SP500.name, SP500['last'], SP500['prevClose']), className='indicator-data my-3', config = {'displayModeBar': False})),
                    html.Tr(dcc.Graph(figure=plot.indicies_indicator(DJIA.name, DJIA['last'], DJIA['prevClose']), className='indicator-data mb-3', config = {'displayModeBar': False})),
                    html.Tr(dcc.Graph(figure=plot.indicies_indicator(R2000.name, R2000['last'], R2000['prevClose']), className='indicator-data mb-3', config = {'displayModeBar': False})),
                    html.Tr(dcc.Graph(figure=plot.indicies_indicator(VIX.name, VIX['last'], VIX['prevClose']), className='indicator-data', config = {'displayModeBar': False})),
                ])
            ])
            
        else:            
            children = html.Div(children='')
            
        return children
 