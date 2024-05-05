import pandas as pd

def read_csv(file_path):
    df = pd.read_csv(file_path, delimiter=',')
    return df

def clean_csv(file_path, columns_to_drop, filter_column=None, filter_value=None):
    df = read_csv(file_path)
    if filter_column is not None and filter_value is not None:
        df = df[df[filter_column] == filter_value]
    df = df.drop(columns=columns_to_drop, axis=1)
    return df

df_region = clean_csv("data/datafiles/area/v_region_2023.csv", ['CHEFLIEU', 'TNCC', 'NCC', 'NCCENR'])
df_departement = clean_csv("data/datafiles/area/v_departement_2023.csv", ['CHEFLIEU', 'TNCC', 'NCC', 'NCCENR'])
df_communes = clean_csv("data/datafiles/area/v_commune_2023.csv", 
                                 ['TYPECOM', 'REG', 'CTCD', 'ARR', 'TNCC', 'NCC', 'NCCENR', 'CAN', 'COMPARENT'], 
                                 filter_column='TYPECOM', filter_value='COM')
df_cheflieudep = clean_csv("data/datafiles/area/v_departement_2023.csv", ['REG', 'TNCC', 'NCC', 'NCCENR', 'LIBELLE'])
df_cheflieureg = clean_csv("data/datafiles/area/v_region_2023.csv", ['TNCC', 'NCC', 'NCCENR', 'LIBELLE'])