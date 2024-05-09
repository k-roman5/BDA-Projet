import pandas as pd
from data.connect_db import connection

cursor = connection.cursor()

def query_to_df(query, cursor=cursor):
    cursor.execute(query)
    columns = [col.name for col in cursor.description]
    return pd.DataFrame(cursor.fetchall(), columns=columns)
