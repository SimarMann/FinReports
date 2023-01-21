from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()

def init_app():
    """Initialize the core application."""
    app = Flask(__name__, instance_relative_config=False)
    
    # Application Configuration
    app.config.from_object('config.Config')
    
    # Initialize Plugins
    db.init_app(app)
    login_manager.init_app(app)
    
    with app.app_context():
        
         # Include our Routes
        from FinReports import routes
        from FinReports import auth
        
        # Register Blueprints
        app.register_blueprint(routes.home_bp)
        app.register_blueprint(auth.auth_bp)
        
        # Create database models
        db.create_all()
        
        # Import & Initalize macrodash dashboard
        from .dash_apps.macrodash.dashboard import init_dashboard
        app = init_dashboard(app)
        
        # Import & Initalize stockscreen dashboard
        from .dash_apps.stockscreen.dashboard import init_dashboard
        app = init_dashboard(app)    
        
        return app