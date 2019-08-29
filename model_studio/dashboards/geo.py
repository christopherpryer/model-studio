"""Create a Dash app within a Flask app."""
from pathlib import Path
from dash import Dash, callback_context
import dash_html_components as html

from .layout import html_layout
from .callbacks import geo as callbacks

from ..auth import login_required
from ..utils import url_for


EXTERNAL_STYLESHEETS = ['/static/dist/css/load.css',
                        '/static/dist/css/styles.css',
                        'https://fonts.googleapis.com/css?family=Lato',
                        'https://use.fontawesome.com/releases/v5.8.1/css/all.css',
                        '/static/dist/css/bWLwgP.css',
                        '/static/dist/css/stylesheet-oil-and-gas.css',
                        '/static/dist/css/styles.css']
EXTERNAL_SCRIPTS = ['/static/dist/js/includes/jquery.min.js',
                        '/static/dist/js/main.js']

def init_app(server):
    """Create a Dash app."""
    dash_app = Dash(server=server,
                    external_stylesheets=EXTERNAL_STYLESHEETS,
                    external_scripts=EXTERNAL_SCRIPTS,
                    routes_pathname_prefix='/geo/')

    dash_app.index_string = html_layout
    dash_app.config['suppress_callback_exceptions'] = True

    dash_app.layout = html.Div(
        children=[html.P('Test', hidden=True, id='test'), html.Div(
            html.Div(
                [], className='container-fluid', id='geo-parent',
                style={'width': '100%'}
            ),
            className='content-wrapper')],
        id='dash-container'
    )

    callbacks.init_callbacks(dash_app)

    return dash_app.server
