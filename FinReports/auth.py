"""Routes for user authentication."""
from flask import Blueprint, redirect, render_template, flash, request, session, url_for, current_app, jsonify
from flask_login import login_required, logout_user, current_user, login_user
from FinReports.forms import LoginForm, SignupForm
from FinReports.models import db, User
from FinReports import login_manager
from dash import page_registry


# Blueprint Configuration
auth_bp = Blueprint('auth_bp', __name__)


@auth_bp.route('/login', methods=['GET', 'POST'])
def login(): 
    """
    Log-in page for registered users.
    GET requests serve Log-in page.
    POST requests validate and redirect user to dashboard.
    """
    # Redirect if user is logged in
    if current_user.is_authenticated:
        return redirect(url_for('home_bp.home'))

    form = LoginForm()
    
    # Validate login attempt
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(password=form.password.data):
            login_user(user)
            next_page = request.args.get('next')
            return redirect(next_page or url_for('home_bp.home'))
        flash('Invalid username/password combination')
        return redirect(url_for('auth_bp.login'))
    return render_template('login.html', form=form)    
    


@auth_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    """ 
    User sign-up page.
    GET requests serve sign-up page.
    POST requests validate form & user creation.
    """
    
    # Redirect if user is logged in
    if current_user.is_authenticated:
        return redirect(url_for('home_bp.home'))
    
    form = SignupForm()
    
    if form.validate_on_submit():
        existing_user = User.query.filter_by(email=form.email.data).first()
        if existing_user is None:
            user = User(
                name=form.name.data,
                email=form.email.data
                )
            user.set_password(form.password.data)
            db.session.add(user)
            db.session.commit()  # Create new user
            login_user(user)  # Log in as newly created user
            return redirect(url_for('home_bp.home'))
        flash('A user already exists with that email address.')        
    return render_template(
        'signup.html', form=form)

@login_manager.user_loader
def load_user(user_id):
    """Check if user is logged-in on every page load."""
    if user_id is not None:
        return User.query.get(user_id)
    return None


@login_manager.unauthorized_handler
def unauthorized():
    """Redirect unauthorized users to Login page."""
    flash('You must be logged in to view that page.')
    return redirect(url_for('auth_bp.login'))

@current_app.before_request
def check_login():
         if request.method == 'GET':
             if current_user:
                 if request.url in ['http://127.0.0.1:5000/login', 'http://127.0.0.1:5000/signup', 'http://127.0.0.1:5000/logout']:
                     return
                 if 'Referer' in request.headers:
                     if request.headers['Referer'] in ['http://127.0.0.1:5000/login', 'http://127.0.0.1:5000/signup', 'http://127.0.0.1:5000/logout']:
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
                 if current_user.is_authenticated or request.path in ['/login', '/signup']:
                     return
             if (request.headers['Referer'] in ['http://127.0.0.1:5000/login', 'http://127.0.0.1:5000/signup', 'http://127.0.0.1:5000/logout'] 
                 and (request.path in ['/_dash-layout', '/_dash-dependencies'] or
                      (request.json['changedPropIds'] == ["_pages_location.pathname", "_pages_location.search"]
                        or request.json['changedPropIds'] == ['{"index":"redirectLogin","type":"redirect"}.n_intervals']))):
                 return
             return jsonify({'status':'401', 'statusText':'unauthorized access'})    