import io
from connect_db import connection
from clean_data import *

def copy_data_to_db_table(df, table_name, cursor):
    csv_buffer = io.StringIO()
    df.to_csv(csv_buffer, index=False, header=False)
    csv_data = csv_buffer.getvalue()
    cursor.copy_from(io.StringIO(csv_data), table_name, sep=',')

cursor = connection.cursor()

copy_data_to_db_table(df_region, 'regions', cursor)
copy_data_to_db_table(df_departement, 'departements', cursor)
copy_data_to_db_table(df_communes, 'communes', cursor)
copy_data_to_db_table(df_cheflieudep, 'cheflieudep', cursor)
copy_data_to_db_table(df_cheflieureg, 'cheflieureg', cursor)
copy_data_to_db_table(df_combined_pop, 'populations', cursor)
"""
copy_data_to_db_table(df_GroupeAgeEpoux, 'GroupeAgeEpoux', cursor)
copy_data_to_db_table(df_EtatMatrimonialAnterieur, 'EtatMatrimonialAnterieur', cursor)
copy_data_to_db_table(df_GroupeAgePremierMariage, 'GroupeAgePremierMariage', cursor)
copy_data_to_db_table(df_NationaliteEpoux, 'NationaliteEpoux', cursor)
copy_data_to_db_table(df_PaysNaissanceEpoux, 'PaysNaissanceEpoux', cursor)
copy_data_to_db_table(df_RepartitionMensuelleMariages, 'RepartitionMensuelleMariages', cursor)
"""

connection.commit()
print("Données importées avec succès !")