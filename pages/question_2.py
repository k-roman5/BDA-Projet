import dash
import dash_bootstrap_components as dbc
from dash import html, callback, Output, Input, dcc
from view.question2 import view_of_the_view1, view_of_the_view2, years

dash.register_page(__name__, location="sidebar", external_stylesheets=[
    dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)

query1 = """
CREATE OR REPLACE VIEW population_departements AS 
    SELECT d.nom AS nom_departement, d.code_dep AS code_departement, p.annee_debut, SUM(p.valeur_stat) AS populations
    FROM departements d
    JOIN communes c ON d.code_dep = c.code_dep
    JOIN populations p ON c.code_com = p.code_com
    WHERE p.type_stat = 'population'
    GROUP BY d.nom, d.code_dep, p.annee_debut, p.annee_fin;
"""

query2 = """
CREATE OR REPLACE VIEW population_regions AS 
    SELECT r.nom AS nom_regions, r.code_reg AS code_regions, p.annee_debut, SUM(p.valeur_stat) AS populations
    FROM regions r
    JOIN departements d ON r.code_reg = d.code_reg
    JOIN communes c ON d.code_dep = c.code_dep
    JOIN populations p ON c.code_com = p.code_com
    WHERE p.type_stat = 'population'
    GROUP BY r.nom, r.code_reg, p.annee_debut, p.annee_fin;
"""

def layout():
    return html.Div([
        html.Br(),
        html.Br(),
        html.H2("Vues des requêtes SQL"),
        html.Br(),
        html.H4("La vue pour la population par département"),  
        html.Br(),
        dbc.Card([
            dbc.CardHeader(html.Span("Requête SQL", style={'color': 'black'})),
            dbc.CardBody([
                html.Pre(query1, className="mb-0", style={'color': 'black', 'overflowY': 'scroll', 'max-height': '200px'}),
            ], style={'padding': '10px'}),
        ], color="light", inverse=True),
        html.Br(),
        html.Div([
            html.Label("Sélectionnez une année :"),
            dcc.Dropdown(id="year-dropdown1",
                        options=[{'label': str(value), 'value': str(value)} for value in years()['annee_debut'].unique()],
                        value='2020'
                        ),
            html.Div(view_of_the_view1('2020'), id='view-table1', style={'overflowY': 'scroll', 'height': '400px'})
        ]),
        html.Br(),
        html.Br(),
        html.H4("La vue pour la population par région"),  
        html.Br(),
        dbc.Card([
            dbc.CardHeader(html.Span("Requête SQL", style={'color': 'black'})),
            dbc.CardBody([
                html.Pre(query2, className="mb-0", style={'color': 'black', 'overflowY': 'scroll', 'max-height': '200px'}),
            ], style={'padding': '10px'}),
        ], color="light", inverse=True),
        html.Br(),
        html.Div([
            html.Label("Sélectionnez une année :"),
            dcc.Dropdown(id="year-dropdown2",
                        options=[{'label': str(value), 'value': str(value)} for value in years()['annee_debut'].unique()],
                        value='2020'
                        ),
            html.Div(view_of_the_view2('2020'), id='view-table2', style={'overflowY': 'scroll', 'height': '400px'})
        ]),
        html.Br(),
    ])

@callback(
    Output('view-table1', 'children'),
    Input('year-dropdown1', 'value'),
    prevent_initial_call = True
)
def update_view1(year):
    updated_view = view_of_the_view1(year)
    return updated_view

@callback(
    Output('view-table2', 'children'),
    Input('year-dropdown2', 'value'),
    prevent_initial_call = True
)
def update_view2(year):
    updated_view = view_of_the_view2(year)
    return updated_view