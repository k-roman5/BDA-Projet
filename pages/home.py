import dash
from dash import html
import dash_bootstrap_components as dbc

dash.register_page(__name__, path='/', location="sidebar", external_stylesheets=[
                   dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)

card_style = {
    'padding': '20px',
    'border': '2px solid #D3D3D3',
    'border-radius': '10px',
    'margin': '20px',
    'background-color': '#F8F9FA',
}


layout = html.Div(style={'color': 'black', 'min-height': '100vh'}, children=[
    html.Div([
        html.H1('Home', style={'textAlign': 'center',
                'color': '#670907', 'font-size': '2.5em'}),
    ], style=card_style),
    html.Br(),
    html.H2("Bienvenue sur la page d'accueil !",
            style={'textAlign': 'center', 'fontSize': '3.0em'})
])