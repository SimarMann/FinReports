from flask import Blueprint

home_bp = Blueprint('home_bp', __name__)

@home_bp.route('/', methods=('GET', 'POST'))
def home():
    return "Hello, World!"