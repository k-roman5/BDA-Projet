import psycopg2

dbname = "postgres"
user = "postgres"
password = "SQL"
host = "localhost" 
port = "5432"

try:
    connection = psycopg2.connect(
        dbname = dbname, user = user, password = password, host = host, port = port
    )
    print("Connexion réussie ! Yippee !")
    
    
    connection.close()
    print("Connexion fermée.")
    
except psycopg2.Error as e:
    print("Erreur lors de la connexion à la base de données :", e)
