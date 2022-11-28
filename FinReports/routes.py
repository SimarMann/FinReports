from flask import Blueprint, render_template
from openbb_terminal.sdk import openbb

home_bp = Blueprint('home_bp', __name__)

@home_bp.route('/', methods=('GET', 'POST'))
def home():    
    return render_template('index.html')