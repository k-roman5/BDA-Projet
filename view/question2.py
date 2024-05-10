import pandas as pd
import dash_bootstrap_components as dbc
from dash import html

from data.db_utils import query_to_df, create_or_replace_view, connection

cursor = connection.cursor()

def df_to_table(df):
    return html.Div([
        dbc.Table.from_dataframe(df, striped=True, bordered=True, hover=True, className='table-sm table-md')
    ])
    
query = """
CREATE OR REPLACE VIEW population_departements AS 
    SELECT d.nom AS nom_departement, d.code_dep AS code_departement, p.annee_debut, p.annee_fin, SUM(p.valeur_stat) AS populations
    FROM departements d
    JOIN communes c ON d.code_dep = c.code_dep
    JOIN populations p ON c.code_com = p.code_com
    GROUP BY d.nom, d.code_dep, p.annee_debut, p.annee_fin;
"""

def view_of_the_view(year=None):
    create_or_replace_view(query)
    query_result = query_to_df(f"SELECT * FROM population_departements WHERE annee_debut = '{year}'")
    return df_to_table(query_result)

def years():
    query = "SELECT DISTINCT annee_debut FROM populations;"
    df = query_to_df(query)
    return df