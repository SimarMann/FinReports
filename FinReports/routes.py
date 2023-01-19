from flask import Blueprint, render_template, redirect, url_for
from flask_login import current_user, login_required, logout_user

home_bp = Blueprint('home_bp', __name__)


@home_bp.route('/', methods=['GET'])
@login_required
def home():
        return render_template('index.html', current_user=current_user)


@home_bp.route("/logout")
@login_required
def logout():
    """User log-out logic."""
    logout_user()
    return redirect(url_for('auth_bp.login'))        

