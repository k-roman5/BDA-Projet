import io
from data.connect import connection

from data.clean_data import df_region, df_departement

cursor = connection.cursor()
csv_buffer = io.StringIO()

#df_region.to_csv(csv_buffer, index=False, header=False)
#csv_data = csv_buffer.getvalue()
#cursor.copy_from(io.StringIO(csv_data), 'regions', sep=',')

df_departement.to_csv(csv_buffer, index=False, header=False)
csv_data = csv_buffer.getvalue()
cursor.copy_from(io.StringIO(csv_data), 'departements', sep=',')

connection.commit()
print("Données importées avec succès !")