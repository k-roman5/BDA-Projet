import io
from connect_db import connection
from clean_data import df_region, df_departement, df_communes, df_cheflieudep, df_cheflieureg

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

connection.commit()
print("Données importées avec succès !")