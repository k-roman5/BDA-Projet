import dash
import dash_bootstrap_components as dbc
from dash import html, callback, Output, Input, dcc

from view.fonctions import years, lire_contenu_fichier_sql, view_population_dep_annee, view_population_reg_annee

dash.register_page(__name__, location="sidebar", external_stylesheets=[
    dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)

def layout():
    return html.Div([
        html.Br(),
        html.Br(),
        html.H2("Triggers suite SQL"),
        html.Br(),
        dbc.Card([
            dbc.CardHeader(html.Span("Requête SQL", style={'color': 'black'})),
            dbc.CardBody([
                html.Pre(lire_contenu_fichier_sql('data/sql/triggers_suite.sql'), className="mb-0", style={'color': 'black', 'overflowY': 'scroll', 'max-height': '500px'}),
            ], style={'padding': '10px'}),
        ], color="light", inverse=True),
        html.Br(),
        html.Br(),
    ])