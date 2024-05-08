import pandas as pd

def clean_csv(file_path, columns_to_drop, filter_column=None, filter_value=None):
    df = pd.read_csv(file_path, delimiter=',', dtype=str)
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

# DF Mariages --------------------------------------------------------------------------------
def regdep_formatting(df):
    """Format the REGDEP column in the dataframe to keep only the metropolitan department number ."""
    column_name = 'REGDEP_MAR' if 'REGDEP_MAR' in df.columns else 'REGDEP_DOMI'    
    df = df.dropna()
    df = df[df[column_name].apply(lambda x: len(x) == 4)]
    df = df[~df[column_name].str.endswith('XX')]
    df[column_name] = df[column_name].str[-2:]
    new_column_name = 'DEP_MAR' if 'REGDEP_MAR' in df.columns else 'DEP_DOMI'
    df = df.rename(columns={column_name: new_column_name})
    return df

df_GroupeAgeEpoux = pd.read_csv("data/datafiles/weddings/Dep1.csv", delimiter=';', dtype=str)
df_GroupeAgeEpoux = regdep_formatting(df_GroupeAgeEpoux)

df_EtatMatrimonialAnterieur = pd.read_csv("data/datafiles/weddings/Dep2.csv", delimiter=';', dtype=str)
df_EtatMatrimonialAnterieur = regdep_formatting(df_EtatMatrimonialAnterieur)

df_GroupeAgePremierMariage = pd.read_csv("data/datafiles/weddings/Dep3.csv", delimiter=';', dtype=str)
df_GroupeAgePremierMariage = regdep_formatting(df_GroupeAgePremierMariage)

df_NationaliteEpoux = pd.read_csv("data/datafiles/weddings/Dep4.csv", delimiter=';', dtype=str)
df_NationaliteEpoux = regdep_formatting(df_NationaliteEpoux)

df_PaysNaissanceEpoux = pd.read_csv("data/datafiles/weddings/Dep5.csv", delimiter=';', dtype=str)
df_PaysNaissanceEpoux = regdep_formatting(df_PaysNaissanceEpoux)

df_RepartitionMensuelleMariages = pd.read_csv("data/datafiles/weddings/Dep6.csv", delimiter=';', dtype=str)
df_RepartitionMensuelleMariages = regdep_formatting(df_RepartitionMensuelleMariages)

# DF Population -----------------------------------------------------------------------------
def process_demographic_data(file_path, columns, type_stat, communes):
    df = pd.read_csv(file_path, delimiter=';', dtype=str)
    df = df.dropna()
    df = df[df['CODGEO'].isin(communes)]
    df = df[columns]
    df = pd.melt(df, id_vars=['CODGEO'], var_name='annee', value_name='valeur_stat')

    if type_stat == 'population' or type_stat == 'logement':
        year_column = df.apply(lambda x: '20' + x['annee'][1:3] if x['annee'].startswith('P') else '19' + x['annee'][1:3], axis=1)
        df['annee_debut'] = year_column
        df['annee_fin'] = year_column
    else:
        df['annee_debut'] = df.apply(lambda x: '20' + x['annee'][4:6] if x['annee'][4:6] in ['09', '14'] else '19' + x['annee'][4:6], axis=1)
        df['annee_fin'] = df.apply(lambda x: '20' + x['annee'][-2:] if x['annee'][-2:] in ['09', '14', '20'] else '19' + x['annee'][-2:], axis=1)

    df['type_stat'] = type_stat
    df = df.drop('annee', axis=1)
    df = df.dropna()
    return df

# Population -----------------------------------------------------------------------------
df_pop = process_demographic_data(
    "data/datafiles/population/France_hors_Mayotte.CSV",
    ['CODGEO','P20_POP', 'P14_POP','P09_POP','D99_POP', 'D90_POP', 'D82_POP','D75_POP','D68_POP'],
    'population',
    df_communes['COM']
)

# Logement -------------------------------------------------------------------------------
df_log = process_demographic_data(
    "data/datafiles/population/France_hors_Mayotte.CSV",
    ['CODGEO','P20_LOG', 'P14_LOG','P09_LOG','D99_LOG', 'D90_LOG', 'D82_LOG','D75_LOG','D68_LOG'],
    'logement',
    df_communes['COM']
)

# Naissances -----------------------------------------------------------------------------
df_nais = process_demographic_data(
    "data/datafiles/population/France_hors_Mayotte.CSV",
    ['CODGEO', 'NAIS1420', 'NAIS0914', 'NAIS9909', 'NAIS9099', 'NAIS8290', 'NAIS7582', 'NAIS6875'],
    'naissances',
    df_communes['COM']
)

# Décès ----------------------------------------------------------------------------------
df_deces = process_demographic_data(
    "data/datafiles/population/France_hors_Mayotte.CSV",
    ['CODGEO', 'DECE1420', 'DECE0914', 'DECE9909', 'DECE9099', 'DECE8290', 'DECE7582', 'DECE6875'],
    'décès',
    df_communes['COM']
)

# Concatenation ---------------------------------------------------------------------------
df_combined_pop = pd.concat([df_pop, df_log, df_nais, df_deces]).reset_index(drop=True)
df_combined_pop['annee_debut'] = df_combined_pop['annee_debut'].astype(int)
df_combined_pop['annee_fin'] = df_combined_pop['annee_fin'].astype(int)

new_column_order = ['CODGEO', 'annee_debut', 'annee_fin', 'type_stat', 'valeur_stat']
df_combined_pop = df_combined_pop[new_column_order]