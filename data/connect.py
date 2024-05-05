import psycopg2

dbname = "postgres"
user = "postgres"
password = "SQL"
host = "localhost"
port = "5432"

connection = psycopg2.connect(
    database=dbname,
    user=user,
    password=password,
    host=host,
)