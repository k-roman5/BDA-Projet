import pandas as pd
from data.connect_db import connection

cursor = connection.cursor()

def query_to_df(query, cursor=None):
    if cursor is None:
        cursor = connection.cursor()
    cursor.execute(query)
    columns = [col.name for col in cursor.description]
    return pd.DataFrame(cursor.fetchall(), columns=columns)

def create_or_replace_view(query, cursor=None):
    if cursor is None:
        cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()

def executer_fichier_sql(nom_fichier):
    with open(nom_fichier, 'r') as fichier:
        contenu_sql = fichier.read()
    cursor.execute("SELECT EXISTS (SELECT FROM information_schema.tables WHERE table_name IN ('population_dep_annee', 'population_reg_annee'));")
    tables_exist = cursor.fetchone()[0]
    if not tables_exist :
        cursor.execute(contenu_sql)
    connection.commit()
