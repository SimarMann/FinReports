from flask import Blueprint, render_template, make_response, request, redirect, url_for
from datetime import datetime as dt
from flask import current_app as app
from .models import db, User

home_bp = Blueprint('home_bp', __name__)
register_bp = Blueprint('register_bp', __name__)

@home_bp.route('/', methods=['GET'])
def home():
        return render_template('index.html')

@register_bp.route('/register', methods=['GET'])
def register():
        """Create a user via query string parameters."""
        username = request.args.get('user')
        email = request.args.get('email')
        if username and email:
                existing_user = User.query.filter(
                        User.username == username or User.email == email
                        ).first()
                if existing_user:
                        return make_response(
                                f'{username} ({email}) already created!'
                                )
                new_user = User(
                        username=username,
                        email=email,
                        created=dt.now(),
                        admin=False
                        )
                db.session.add(new_user)  # Adds new User record to database
                db.session.commit()  # Commits all changes
                redirect(url_for('register_bp.register'))
        return render_template(
                'users.html',
                users=User.query.all(),
                title="Show Users"
                )
        