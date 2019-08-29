from numpy import cos, sin, arcsin, sqrt
from math import radians
from flask import session
import dash
from dash.dependencies import Input, Output, State
import dash_html_components as html
import pandas as pd
from haversine import haversine, Unit
import os

from ... import db
from ...utils import APP_STATIC, url_for
from ..children import geo as children

def geocode():
    """query shipments table geocoded and return as df"""
    script = ''
    dirpath = os.path.join(APP_STATIC, 'sql')
    with open(os.path.join(dirpath, 'geocode.sql')) as f:
        script = f.read()
    return pd.read_sql(script, con=db.engine)

def process_haversine(df):
    df['distance'] = df.apply(lambda row : haversine(
            (row['origin_lat'], row['origin_lon']),
            (row['dest_lat'], row['dest_lon']), unit=Unit.MILES),
            axis=1)
    df.distance = df.distance.round(4)
    df.to_sql('shipments', if_exists='replace', con=db.engine,
        index=False)
    return df

def get_ctx():
    ctx = dash.callback_context
    triggered = None
    if ctx.triggered:
        triggered = ctx.triggered[0]['prop_id'].split('.')[0]

    return triggered

def init_callbacks(dash_app):
    @dash_app.callback(
        Output('geo-parent', 'children'),
        [Input('test', 'values')])
    def index(p):
        user_id = session.get('user_id')
        if user_id:
            df = geocode()
            df = process_haversine(df)
            return children.get_children(df)
        else:
            return html.A(
                'Authentication required', href=url_for('auth.login'))
