from dash import Dash
from . import layout
from . import callbacks



def init_dashboard(flask_app):
    """Create a Plotly Dash dashboard."""
    dash_app = Dash(
        server=flask_app,
        routes_pathname_prefix='/dashboard/',
        external_stylesheets=[
            '../static/css/style.css',
            '../static/css/bootstrap.min.css'
        ]
    )
    
    layout.layout(dash_app)
    
    callbacks.init_callbacks(dash_app)

    return dash_app.server