import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objects as go
import dash_table

import pandas as pd
import os

from ... import db
from ...utils import APP_STATIC, url_for

def geocode():
    """query shipments table geocoded and return as df"""
    script = ''
    dirpath = os.path.join(APP_STATIC, 'sql')
    with open(os.path.join(dirpath, 'geocode.sql')) as f:
        script = f.read()
    return pd.read_sql(script, con=db.engine)

#### plotting

def get_basic_table(df):
    return html.Div([
        dash_table.DataTable(
            id='data',
            data=df.to_dict('records'),
            columns=[{'id': c, 'name': c} for c in df.columns],
            style_table={'overflowX': 'scroll'},
        ),
        html.A('Download', href=url_for('main.download'))])

def get_basic_chart(df):
    fig = go.Figure()
    sizeref = 2.* max(df.demand) / (100**2)
    fig.add_trace(
            go.Scattergeo(
                locationmode = 'USA-states',
                lat=df.dest_lat,
                lon=df.dest_lon,
                hoverinfo='text',
                text=df.stop_id,
                name='destinations',
                mode='markers',
                marker=dict(
                    size=df.demand,
                    line_width=1.5,
                    line_color='black',
                    sizemode='area',
                    sizeref=sizeref
                )))
    fig.update_layout(
    title_text='',
    showlegend=False,
    legend=dict(x=-.1, y=0.8),
    geo=go.layout.Geo(
        scope='usa',
        projection_type='albers usa',
        showland=True,
        landcolor='rgb(224, 224, 224)',
        countrycolor='rgb(204, 204, 204)'
        ))

    return dcc.Graph(figure=fig, id='map')


def get_children():
    df = geocode()
    children = [html.A('Log Out', href=url_for('auth.logout'))]
    children += [get_basic_chart(df), get_basic_table(df)]
    return children
