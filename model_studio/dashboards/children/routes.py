import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objects as go
import dash_table
import pandas as pd
import numpy as np
from ...utils import APP_STATIC
import os

def get_data():
    filepath = os.path.join(APP_STATIC, 'data.csv')
    return pd.read_csv(filepath)

def get_basic_table(df):
    return dash_table.DataTable(
        id='data',
        columns=[{'name': i, 'id': i} for i in df.columns],
        data=df.to_dict('rows'),
        sorting=True,
    )

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


def Get_Routes_Children():
    df = get_data()
    children = []
    children += [get_basic_chart(df), get_basic_table(df)]
    return children
