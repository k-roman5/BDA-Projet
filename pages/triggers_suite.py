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
    ])