from psycopg2 import Error

from connect import connection

script_path = "data/sql/create_table.sql"

try:
    cursor = connection.cursor()

    with open(script_path, 'r') as file:
        sql_script = file.read()

    cursor.execute(sql_script)
    connection.commit()
    print("Tables créées avec succès.")

except (Exception, Error) as error:
    print("Erreur lors de la création des tables :", error)

finally:
    if connection:
        cursor.close()
        connection.close()
        print("Connexion à la base de données fermée.")