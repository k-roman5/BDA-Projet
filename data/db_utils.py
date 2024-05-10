import pandas as pd
from data.connect_db import connection
import psycopg2

cursor = connection.cursor()

def query_to_df(query, cursor=cursor):
    cursor.execute(query)
    columns = [col.name for col in cursor.description]
    return pd.DataFrame(cursor.fetchall(), columns=columns)

def create_or_replace_view(query, cursor=cursor):
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()