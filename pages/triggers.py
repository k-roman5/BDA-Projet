import dash
import dash_bootstrap_components as dbc
from dash import html, callback, Output, Input, dcc, State

from view.fonctions import years, lire_contenu_fichier_sql, view_population_dep_annee, view_population_reg_annee, insert

dash.register_page(__name__, location="sidebar", external_stylesheets=[
    dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)

def layout():
    return html.Div([
        html.Br(),
        html.Br(),
        html.H2("Triggers SQL"),
        html.Br(),
        html.Br(),
        dbc.Card([
            dbc.CardHeader(html.Span("Requête SQL", style={'color': 'black'})),
            dbc.CardBody([
                html.Pre(lire_contenu_fichier_sql('data/sql/triggers.sql'), className="mb-0", style={'color': 'black', 'overflowY': 'scroll', 'max-height': '500px'}),
            ], style={'padding': '10px'}),
        ], color="light", inverse=True),
        html.Br(),
        html.Br(),
        html.H4("La table pour la population par département"),  
        html.Br(),
        html.Div([
            html.Label("Sélectionnez une année :"),
            dcc.Dropdown(id="year-dropdown5",
                        options=[{'label': str(value), 'value': str(value)} for value in years()['annee_debut'].unique()],
                        value='2020'
                        ),
            html.Div(view_population_dep_annee('2020'), id='view-table5', style={'overflowY': 'scroll', 'height': '400px'})
        ]),
        html.Br(),
        html.Br(),
        html.H4("La table pour la population par région"),  
        html.Br(),
        html.Div([
            html.Label("Sélectionnez une année :"),
            dcc.Dropdown(id="year-dropdown6",
                        options=[{'label': str(value), 'value': str(value)} for value in years()['annee_debut'].unique()],
                        value='2020'
                        ),
            html.Div(view_population_reg_annee('2020'), id='view-table6', style={'overflowY': 'scroll', 'height': '400px'})
        ]),
        html.Br(),
        html.Br(),
        html.Div([
            html.H4("Insertion de données"),
            dbc.Input(id='code-input', placeholder='Code', type='text'),
            dbc.Input(id='year-input', placeholder='Année', type='number'),
            dbc.Input(id='population-input', placeholder='Population', type='number'),
            html.Button('Insérer', id='insert-button', n_clicks=0)
        ]),
        html.Br(),
        html.Div(id='insertion-result')
    ])

@callback(
    [Output('insertion-result', 'children')],
    [Input('insert-button', 'n_clicks')], 
    [State('code-input', 'value'), State('year-input', 'value'), State('population-input', 'value')],
    prevent_initial_call=True
)
def insert_data(n_clicks, code, year, population, ):
    if n_clicks > 0:
        insert_result = insert(code, str(year), population)
        return html.Div(f"Données insérées avec succès : {insert_result}")
    else:
        return dash.no_update, dash.no_update, html.Div(f"Impossible d'insérer des données")
    
@callback(
    Output('view-table5', 'children'),
    [Input('insertion-result', 'children'), Input('year-dropdown5', 'value')]
)
def update_view(_, year_dep):
    if year_dep is None:
        year_dep = '2020'
    updated_view_dep = view_population_dep_annee(str(year_dep))
    return updated_view_dep

@callback(
    Output('view-table6', 'children'),
    [Input('insertion-result', 'children'), Input('year-dropdown6', 'value')]
)
def update_view(_, year_reg):
    if year_reg is None:
        year_reg = '2020'
    updated_view_reg = view_population_reg_annee(str(year_reg))
    return updated_view_reg
