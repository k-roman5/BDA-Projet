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

# Popultation -----------------------------------------------------------------------------
df_pop = pd.read_csv("data/datafiles/population/France_hors_Mayotte.CSV", delimiter=';', dtype=str)
df_pop = df_pop.dropna()
df_pop['CODGEO'] = df_pop['CODGEO'].apply(lambda x: '0' + str(x) if len(str(x)) == 4 else x)
df_pop_merge = pd.merge(df_pop, df_communes, left_on='CODGEO', right_on='COM')
df_pop_merge = df_pop_merge[df_pop.columns]
df_population = df_pop_merge[['CODGEO', 'P20_POP', 'P14_POP', 'P09_POP', 'D99_POP', 'D90_POP', 'D82_POP', 'D75_POP', 'D68_POP']]
colonnes_population = ['P20_POP', 'P14_POP', 'P09_POP', 'D99_POP', 'D90_POP', 'D82_POP', 'D75_POP', 'D68_POP']
df_population[colonnes_population] = df_population[colonnes_population].astype(int)
df_population = df_population[(df_population[colonnes_population] != 0).any(axis=1)]
print(df_population)

# Mariages --------------------------------------------------------------------------------
df_GroupeAgeEpoux = pd.read_csv("data/datafiles/weddings/Dep1.csv", delimiter=';', dtype=str)
df_EtatMatrimonialAnterieur = pd.read_csv("data/datafiles/weddings/Dep2.csv", delimiter=';', dtype=str)
df_GroupeAgePremierMariage = pd.read_csv("data/datafiles/weddings/Dep3.csv", delimiter=';', dtype=str)
df_NationaliteEpoux = pd.read_csv("data/datafiles/weddings/Dep4.csv", delimiter=';', dtype=str)
df_PaysNaissanceEpoux = pd.read_csv("data/datafiles/weddings/Dep5.csv", delimiter=';', dtype=str)
df_RepartitionMensuelleMariages = pd.read_csv("data/datafiles/weddings/Dep6.csv", delimiter=';', dtype=str)