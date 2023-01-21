from dash import Dash
from . import layout
from . import callbacks
from .. import auth



def init_dashboard(flask_app):
    """Create a Plotly Dash dashboard."""
    dash_app = Dash(
        server=flask_app,
        routes_pathname_prefix='/macrodash/',
        external_stylesheets=[
            '../static/css/bootstrap.min.css',
            '../static/css/style.css'
        ]
    )
    
    with flask_app.test_request_context():
        auth.check_login()
    
    layout.layout(dash_app)
    
    callbacks.init_callbacks(dash_app)

    return dash_app.server