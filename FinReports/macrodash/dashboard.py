from dash import Dash
from . import layout

def init_dashboard(flask_app):
    """Create a Plotly Dash dashboard."""
    dash_app = Dash(
        server=flask_app,
        routes_pathname_prefix='/macrodash/',
        external_stylesheets=[
            '../static/css/style.css',
            '../static/css/bootstrap.min.css'
        ]
    )
    
    layout.layout(dash_app)

    return dash_app.server