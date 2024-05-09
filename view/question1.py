import configparser
import dash_bootstrap_components as dbc
from dash import html

from data.db_utils import query_to_df

### DATA ###
# Read the queries file
config = configparser.ConfigParser()
config.read('data/queries_sql.ini')

# Get the queries and their titles
title1 = config.get('QUESTION1', 'title1')
query1 = config.get('QUESTION1', 'query1')
title2 = config.get('QUESTION1', 'title2')
query2 = config.get('QUESTION1', 'query2')
title3 = config.get('QUESTION1', 'title3')
query3 = config.get('QUESTION1', 'query3')
title4 = config.get('QUESTION1', 'title4')
query4 = config.get('QUESTION1', 'query4')
############

def df_to_table(df):
    return html.Div([
        dbc.Table.from_dataframe(df, striped=True, bordered=True, hover=True, className='table-sm table-md')
    ])

def departments_of_a_region(code_region):
    query = f"SELECT * FROM departements WHERE code_reg = '{code_region}';"
    df = query_to_df(query)
    return df_to_table(df)

def regions():
    query = "SELECT * FROM regions;"
    df = query_to_df(query)
    return df

def region_name(code_region):
    query = f"SELECT nom FROM regions WHERE code_reg = '{code_region}';"
    df = query_to_df(query)
    return df.iloc[0, 0]