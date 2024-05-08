import dash
from dash import html
import dash_bootstrap_components as dbc
import psycopg2
import configparser

dash.register_page(__name__, location="sidebar", external_stylesheets=[
    dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)

dbname = "postgres"
user = "postgres"
password = "SQL" # Le mdp de pgAdmin de Karina
host = "localhost"
port = "5432"

connection = psycopg2.connect(
    database=dbname,
    user=user,
    password=password,
    host=host,
)

def show_request():
    config = configparser.ConfigParser()
    config.read("data/queries_sql.ini")

    query1 = config.get("QUESTION1", "query1")
    
    df = 0
    return html.Div([
        dbc.Table.from_dataframe(df, striped=True, bordered=True, hover=True, className='table-sm table-md')
    ])

def layout():
    return html.Div([
        html.H1("Résultats des requêtes SQL"),
        html.Br(),
        show_request(), 
    ])