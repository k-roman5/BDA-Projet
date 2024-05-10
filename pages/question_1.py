import configparser
import dash
import dash_bootstrap_components as dbc
from dash import html, callback, Output, Input, dcc

from view.question1 import df_to_table
from data.db_utils import query_to_df

dash.register_page(__name__, location="sidebar", external_stylesheets=[
    dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)

config = configparser.ConfigParser()
config.read('data\queries_sql.ini', encoding='utf-8')

def layout():
    return html.Div([
        html.H1("Résultats des requêtes SQL"),
        html.Br(),
        dcc.Dropdown(id="select_query",
                        options=[{'label': config.get('TITLE', 'title'+i), 'value': i} for i in ['1', '2', '3', '4']],
                        value='1'
            ),
        html.Div([
            update_query('1'),
        ], id="show_query"),
    ])

@callback(Output("show_query", "children"), 
          [Input("select_query", "value")],
          prevent_initial_call=True)
def update_query(value):
    return html.Div([
        html.H2(config.get('TITLE', 'title'+value)),
        dbc.Card([
                dbc.CardHeader(html.Span("Requête SQL", style={'color': 'black'})),
                dbc.CardBody([
                    html.Pre([
                        html.Code(config.get('QUERY', 'query'+value), style={'color': 'black'}),
                    ], className="mb-0", style={'margin': 0, 'background-color': '#dcdcdc', 'padding': '10px', 'border-radius': '5px'}),
                ], style={'padding': '10px'}),
            ], color="light", inverse=True),
        df_to_table(query_to_df(config.get('QUERY', 'query'+value))),
    ])