import dash_bootstrap_components as dbc
from dash import html

from data.db_utils import query_to_df

def df_to_table(df):
    return html.Div([
        dbc.Table.from_dataframe(df, striped=True, bordered=True, hover=True, className='table-sm table-md')
    ])
