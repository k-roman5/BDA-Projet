import dash
import dash_bootstrap_components as dbc
from dash import html, callback, Output, Input, dcc
from view.question2 import years
from view.question3 import lire_contenu_fichier_sql, view_population_dep_annee, view_population_reg_annee

dash.register_page(__name__, location="sidebar", external_stylesheets=[
    dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)

def layout():
    return html.Div([
        html.Br(),
        html.Br(),
        html.H2("Procédure stockée SQL"),
        html.Br(),
        html.Br(),
        dbc.Card([
            dbc.CardHeader(html.Span("Requête SQL", style={'color': 'black'})),
            dbc.CardBody([
                html.Pre(lire_contenu_fichier_sql('data/sql/procedure_stockee.sql'), className="mb-0", style={'color': 'black', 'overflowY': 'scroll', 'max-height': '500px'}),
            ], style={'padding': '10px'}),
        ], color="light", inverse=True),
        html.Br(),
        html.Br(),
        html.H4("La table pour la population par département"),  
        html.Br(),
        html.Div([
            html.Label("Sélectionnez une année :"),
            dcc.Dropdown(id="year-dropdown3",
                        options=[{'label': str(value), 'value': str(value)} for value in years()['annee_debut'].unique()],
                        value='2020'
                        ),
            html.Div(view_population_dep_annee('2020'), id='view-table3', style={'overflowY': 'scroll', 'height': '400px'})
        ]),
        html.Br(),
        html.Br(),
        html.H4("La table pour la population par région"),  
        html.Br(),
        html.Div([
            html.Label("Sélectionnez une année :"),
            dcc.Dropdown(id="year-dropdown4",
                        options=[{'label': str(value), 'value': str(value)} for value in years()['annee_debut'].unique()],
                        value='2020'
                        ),
            html.Div(view_population_reg_annee('2020'), id='view-table4', style={'overflowY': 'scroll', 'height': '400px'})
        ]),
    ])

@callback(
    Output('view-table3', 'children'),
    Input('year-dropdown3', 'value'),
    prevent_initial_call = True
)
def update_table1(year):
    updated_view = view_population_dep_annee(year)
    return updated_view

@callback(
    Output('view-table4', 'children'),
    Input('year-dropdown4', 'value'),
    prevent_initial_call = True
)
def update_table2(year):
    updated_view = view_population_reg_annee(year)
    return updated_view