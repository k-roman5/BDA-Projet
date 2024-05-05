import psycopg2
import csv
from connect import connection

csv_file = "data/datafiles/area/v_commune_2023.csv"

try:
    cursor = connection.cursor()

    connection.commit()
    print("Données importées avec succès !")

except psycopg2.Error as e:
    print("Erreur lors de l'import des données dans la base de données :", e)

finally:
    if connection:
        cursor.close()
        connection.close()