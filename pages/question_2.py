import dash
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
from dash import html, callback, Output, Input


dash.register_page(__name__, location="sidebar", external_stylesheets=[
    dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)

def layout():

    return html.Div([
        html.H1("Vues des requêtes SQL"),
        html.Br()
    ])