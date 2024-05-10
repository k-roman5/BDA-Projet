import dash_bootstrap_components as dbc
from dash import html

from data.db_utils import query_to_df, create_or_replace_view, executer_fichier_sql

def df_to_table(df):
    return html.Div([
        dbc.Table.from_dataframe(df, striped=True, bordered=True, hover=True, className='table-sm table-md')
    ])

def years():
    query = "SELECT DISTINCT annee_debut FROM populations;"
    df = query_to_df(query)
    return df
    
def view_of_the_view1(year=None, query=None):
    create_or_replace_view(query)
    query_result = query_to_df(f"SELECT * FROM population_departements WHERE annee_debut = '{year}'")
    return df_to_table(query_result)

def view_of_the_view2(year=None, query=None):
    create_or_replace_view(query)
    query_result = query_to_df(f"SELECT * FROM population_regions WHERE annee_debut = '{year}'")
    return df_to_table(query_result)
   
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

def insert(code, year, population):
    nom_fichier_sql = 'data/sql/procedure_stockee.sql'
    executer_fichier_sql(nom_fichier_sql)
    query = f"INSERT INTO population_dep_annee (code_dep, annee, population) VALUES ('{code}', {year}, {population})"
    query_result = query_to_df(query)
    return query_result