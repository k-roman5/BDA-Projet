import pandas as pd

df_region = pd.read_csv("data/datafiles/area/v_region_2023.csv", delimiter=',')
df_region = df_region.drop(columns=['CHEFLIEU', 'TNCC', 'NCC', 'NCCENR'], axis=1)

df_departement = pd.read_csv("data/datafiles/area/v_departement_2023.csv", delimiter=',')
df_departement = df_departement.drop(columns=['CHEFLIEU', 'TNCC', 'NCC', 'NCCENR'], axis=1)
print(df_departement)