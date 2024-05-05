import psycopg2

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