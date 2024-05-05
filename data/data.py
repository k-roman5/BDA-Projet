import psycopg2
import csv

dbname = "postgres"
user = "postgres"
password = "SQL"
host = "localhost"
port = "5432"

csv_file = "data/datafiles/area/v_commune_2023.csv"

try:
    connection = psycopg2.connect(
        dbname = dbname, user = user, password = password, host = host, port = port
    )
    cursor = connection.cursor()

    with open(csv_file, 'r') as f:
        next(f)
        cursor.copy_from(f, 'communities', sep=',')

    connection.commit()
    print("Données importées avec succès !")

except psycopg2.Error as e:
    print("Erreur lors de l'import des données dans la base de données :", e)

finally:
    if connection:
        cursor.close()
        connection.close()