import dash_html_components as html
import dash_core_components as dcc
import dash_table
import pandas as pd
import numpy as np
from ..utils import *

def get_data():
    filepath = os.path.join(APP_STATIC, 'data.csv')
    return pd.read_csv(filepath)

def get_basic_table(df):
    return dash_table.DataTable(
        id='chart-data',
        columns=[{'name': i, 'id': i} for i in df.columns],
        data=df.to_dict('rows'),
        sorting=True,
    )

def Get_Chart_Children():
    df = get_data()
    children = []
    children += [get_basic_table(df)]
    return children
