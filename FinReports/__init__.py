from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_app():
    """Initialize the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')
    
    # Initialize Plugins
    db.init_app(app)
    
    with app.app_context():
        
         # Include our Routes
        from FinReports import routes
        
        # Register Blueprints
        app.register_blueprint(routes.home_bp)
        app.register_blueprint(routes.register_bp)
        
        # Create sql tables for our data models
        db.create_all()
        
        # Import & Initalize stockscreen dashboard
        from .stockscreen.dashboard import init_dashboard
        app = init_dashboard(app)
        
        # Import & Initalize macrodash dashboard
        from .macrodash.dashboard import init_dashboard
        app = init_dashboard(app)    
        
        return app