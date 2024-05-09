import dash
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
from dash import html, callback, Output, Input, dcc

from view.question1 import departments_of_a_region, regions, region_name, communes_of_a_department_with_population, departements, departement_name


dash.register_page(__name__, location="sidebar", external_stylesheets=[
    dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)

def layout():
    code_region = '75'
    nom_de_la_region = 'Nouvelle-Aquitaine'

    nb_habitants = 100000
    nom_du_departement = 'Gironde'
    code_dep = '33'

    return html.Div([
        html.H1("Résultats des requêtes SQL"),
        html.Br(),
        html.Div([ 
            html.H2(f"Liste des départements de la région {nom_de_la_region}"),
            html.P(f"SELECT * FROM departements WHERE code_reg = '{code_region}';"),
            departments_of_a_region(code_region),
        ], id="departements_of_a_region"),
        dmc.Select(placeholder="Choissez une région",
                            id="select-region",
                            data=regions().rename(columns={'code_reg': 'value', 'nom': 'label'}).to_dict(orient='records'),
                            value=code_region
                            ),
        html.Br(),
        html.Div([ 
            html.H2(f"Liste des communes de plus de {nb_habitants} habitants du département {nom_du_departement} en 2020"),
            html.P("SELECT code_com, code_dep, nom, annee_debut AS annee, valeur_stat" \
                + " FROM communes NATURAL JOIN populations" \
                + f" WHERE code_dep = '{code_dep}' AND valeur_stat > {nb_habitants}" \
                + " AND type_stat = 'population' AND annee_debut = '2020';"),
            communes_of_a_department_with_population(code_dep, nb_habitants),
        ], id="communes_of_a_department"),
        dmc.Select(placeholder="Choissez un département",
                            id="select-department",
                            data=departements().rename(columns={'code_dep': 'value', 'nom': 'label'}).to_dict(orient='records'),
                            value=code_dep
                            ),
        dcc.Slider(0, 6, 0.1,
                marks={i: '{}'.format(10 ** i) for i in range(4)},
                value=3,
                id='population-slider',
        ),
    ])


@callback(Output("departements_of_a_region", "children"), 
          [Input("select-region", "value")])
def update_departements_of_a_region(value):
    nom_de_la_region = region_name(value)
    return html.Div([ 
            html.H2(f"Liste des départements de la région {nom_de_la_region}"),
            html.P(f"SELECT * FROM departements WHERE code_reg = '{value}';"),
            departments_of_a_region(value),
        ], id="departements_of_a_region")

@callback(Output("communes_of_a_department", "children"),
            [Input("select-department", "value"),
             Input("population-slider", "value")])
def update_communes_of_a_department(dep, nb_habitants):
    if nb_habitants is None:
        nb_habitants = 100000
    else:
        nb_habitants = round(10 ** nb_habitants / 100) * 100
    if dep is None:
        dep = '33'
    nom_du_departement = departement_name(dep)
    return html.Div([ 
            html.H2(f"Liste des communes de plus de {nb_habitants} habitants du département {nom_du_departement} en 2020"),
            html.P("SELECT code_com, code_dep, nom, annee_debut AS annee, valeur_stat" \
                + " FROM communes NATURAL JOIN populations" \
                + f" WHERE code_dep = '{dep}' AND valeur_stat > {nb_habitants}" \
                + " AND type_stat = 'population' AND annee_debut = '2020';"),
            communes_of_a_department_with_population(dep, nb_habitants),
        ], id="communes_of_a_department")