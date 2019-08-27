from flask import session
from dash.dependencies import Input, Output, State
import dash_html_components as html
import pandas as pd
import numpy as np

from ..children import geo as children

from ...utils import url_for

def init_callbacks(dash_app):
    @dash_app.callback(
        Output('geo-parent', 'children'),
        [Input('test', 'values')])
    def index(p):
        user_id = session.get('user_id')
        if user_id:
            return children.get_children()
        else:
            return html.A(
                'Authentication required', href=url_for('auth.login'))
