"""Routes for core Flask app."""
import os
from flask import Blueprint, render_template
from flask_assets import Environment, Bundle
from .auth import login_required

bp = Blueprint('main', __name__,
                    template_folder='templates',
                    static_folder='static')

@bp.route('/')
@login_required
def home():
    return render_template('home.html', template='home-template')
