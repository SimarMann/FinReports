from dash import Dash, page_registry
from . import layout
from . import callbacks
from flask_login import current_user
from flask import request, session, redirect, jsonify, flash


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
    
    @flask_app.before_request
    def check_login():
         if request.method == 'GET':
             if current_user:
                 if request.url in ['http://127.0.0.1:5000/login', 'http://127.0.0.1:5000/logout']:
                     return
                 if 'Referer' in request.headers:
                     if request.headers['Referer'] in ['http://127.0.0.1:5000/login', 'http://127.0.0.1:5000/logout']:
                         return 
                 if current_user.is_authenticated:
                     return
                 else:
                     for pg in page_registry:
                         if request.path == page_registry[pg]['path']:
                             session['url'] = request.url
             flash('You must be logged in to view that page.')                
             return redirect('http://127.0.0.1:5000/login')                
                             
         else:
             if current_user:
                 if current_user.is_authenticated or request.path == '/login':
                     return
             if (request.headers['Referer'] in ['http://127.0.0.1:5000/login', 'http://127.0.0.1:5000/logout'] 
                 and (request.path in ['/_dash-layout', '/_dash-dependencies'] or
                      (request.json['changedPropIds'] == ["_pages_location.pathname", "_pages_location.search"]
                        or request.json['changedPropIds'] == ['{"index":"redirectLogin","type":"redirect"}.n_intervals']))):
                 return
             return jsonify({'status':'401', 'statusText':'unauthorized access'})

    layout.layout(dash_app)
    
    callbacks.init_callbacks(dash_app)

    return dash_app.server