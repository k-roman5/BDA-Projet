from data.db_utils import executer_fichier_sql, query_to_df
import dash_bootstrap_components as dbc
from dash import html


def df_to_table(df):
    return html.Div([
        dbc.Table.from_dataframe(df, striped=True, bordered=True, hover=True, className='table-sm table-md')
    ])

def lire_contenu_fichier_sql(nom_fichier):
    with open(nom_fichier, 'r') as fichier:
        contenu = fichier.read()
    return contenu

def view_population_reg_annee(year=None):
    nom_fichier_sql = 'data/sql/procedure_stockee.sql'
    executer_fichier_sql(nom_fichier_sql)
    query_result = query_to_df(f"SELECT * FROM population_reg_annee WHERE annee = '{year}'")
    return df_to_table(query_result)

def view_population_dep_annee(year=None):
    nom_fichier_sql = 'data/sql/procedure_stockee.sql'
    executer_fichier_sql(nom_fichier_sql)
    query_result = query_to_df(f"SELECT * FROM population_dep_annee WHERE annee = '{year}'")
    return df_to_table(query_result)