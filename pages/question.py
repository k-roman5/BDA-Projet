import dash
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
from dash import html, callback, Output, Input

from view.question1 import departments_of_a_region, regions, region_name


dash.register_page(__name__, location="sidebar", external_stylesheets=[
    dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)

def layout():
    code_region = '75'
    nom_de_la_region = 'Nouvelle-Aquitaine'

    return html.Div([
        html.H1("Résultats des requêtes SQL"),
        html.Br(),
        dmc.Select(placeholder="Choissez une région",
                            id="select-region",
                            data=regions().rename(columns={'code_reg': 'value', 'nom': 'label'}).to_dict(orient='records'),
                            value=code_region
                            ),
        html.Br(),
        html.Div([ 
            html.H2(f"Liste des départements de la région {nom_de_la_region}"),
            dbc.Card([
                dbc.CardHeader(html.Span("Requête SQL", style={'color': 'black'})),
                dbc.CardBody([
                    html.Pre([
                        html.Code(f"SELECT * FROM departements WHERE code_reg = '{code_region}';", style={'color': 'white'}),
                    ], className="mb-0", style={'margin': 0, 'background-color': '#dcdcdc', 'padding': '10px', 'border-radius': '5px'}),
                ], style={'padding': '10px'}),
            ], color="light", inverse=True),
            departments_of_a_region(code_region),
        ], id="departements_of_a_region",),
    ])

@callback(Output("departements_of_a_region", "children"), 
          [Input("select-region", "value")])
def update_departements_of_a_region(value):
    nom_de_la_region = region_name(value)
    return html.Div([ 
            html.H2(f"Liste des départements de la région {nom_de_la_region}"),
            html.Br(),
            dbc.Card([
                dbc.CardHeader(html.Span("Requête SQL", style={'color': 'black'})),
                dbc.CardBody([
                    html.Pre([
                        html.Code(f"SELECT * FROM departements WHERE code_reg = '{value}';", style={'color': 'black'}),
                    ], className="mb-0", style={'margin': 0, 'background-color': '#dcdcdc', 'padding': '10px', 'border-radius': '5px'}),
                ], style={'padding': '10px'}),
            ], color="light", inverse=True),
            html.Br(),
            departments_of_a_region(value),
        ], id="departements_of_a_region",)