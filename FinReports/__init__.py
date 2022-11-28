from flask import Flask

def init_app():
    """Initialize the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')
    
    with app.app_context():
        
        from FinReports import routes
        from .plotlydash.dashboard import init_dashboard
        
        app.register_blueprint(routes.home_bp)
        app = init_dashboard(app)
        
        return app