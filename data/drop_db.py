from psycopg2 import Error
from connect_db import connection

script_path = "data/sql/drop_table.sql"

try:
    with connection.cursor() as cursor:
        with open(script_path, 'r') as file:
            sql_script = file.read()

        cursor.execute(sql_script)
        connection.commit()
        print("Tables dropped successfully.")

except Error as error:
    print("Error dropping tables:", error)

finally:
    if connection:
        connection.close()
        print("Database connection closed.")