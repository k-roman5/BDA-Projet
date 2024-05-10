import dash
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
from dash import html, callback, Output, Input, dcc
from view.question2 import view_of_the_view1, view_of_the_view2, years1

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

def layout():
    return html.Div([
        html.Br(),
        html.Br(),
        html.H2("Vues des requêtes SQL"),
        html.Br(),
        html.H4("La vue pour la population département"),  
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
            dmc.Select(placeholder="Choissez une années",
                                id="year-dropdown1",
                                data=years1().rename(columns={'annee_debut': 'value'}).to_dict(orient='records'),
                                value='2020'
                                ),
            html.Div(view_of_the_view1('2020'), id='view-table1', style={'overflowY': 'scroll', 'height': '400px'})
        ]),
        html.Br(),
        html.Br(),
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