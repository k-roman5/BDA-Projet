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

# DF Mariages --------------------------------------------------------------------------------
df_GroupeAgeEpoux = pd.read_csv("data/datafiles/weddings/Dep1.csv", delimiter=';', dtype=str)
# Suppression des DOM-TOM, du total sur la France métrropolitaine et sur la France entière
df_GroupeAgeEpoux = df_GroupeAgeEpoux[df_GroupeAgeEpoux['REGDEP_MAR'].apply(lambda x: len(x) == 4)]
df_GroupeAgeEpoux = df_GroupeAgeEpoux[~df_GroupeAgeEpoux['REGDEP_MAR'].str.endswith('XX')] # XX = Total
df_GroupeAgeEpoux['REGDEP_MAR'] = df_GroupeAgeEpoux['REGDEP_MAR'].str[-2:]
df_GroupeAgeEpoux = df_GroupeAgeEpoux.rename(columns={'REGDEP_MAR': 'DEP_MAR'})

df_EtatMatrimonialAnterieur = pd.read_csv("data/datafiles/weddings/Dep2.csv", delimiter=';', dtype=str)
# Suppression des DOM-TOM, du total sur la France métrropolitaine et sur la France entière
df_EtatMatrimonialAnterieur = df_EtatMatrimonialAnterieur[df_EtatMatrimonialAnterieur['REGDEP_MAR'].apply(lambda x: len(x) == 4)]
df_EtatMatrimonialAnterieur = df_EtatMatrimonialAnterieur[~df_EtatMatrimonialAnterieur['REGDEP_MAR'].str.endswith('XX')] # XX = Total
df_EtatMatrimonialAnterieur['REGDEP_MAR'] = df_EtatMatrimonialAnterieur['REGDEP_MAR'].str[-2:]
df_EtatMatrimonialAnterieur = df_EtatMatrimonialAnterieur.rename(columns={'REGDEP_MAR': 'DEP_MAR'})

df_GroupeAgePremierMariage = pd.read_csv("data/datafiles/weddings/Dep3.csv", delimiter=';', dtype=str)
# Suppression des DOM-TOM, du total sur la France métrropolitaine et sur la France entière
df_GroupeAgePremierMariage = df_GroupeAgePremierMariage[df_GroupeAgePremierMariage['REGDEP_MAR'].apply(lambda x: len(x) == 4)]
df_GroupeAgePremierMariage = df_GroupeAgePremierMariage[~df_GroupeAgePremierMariage['REGDEP_MAR'].str.endswith('XX')] # XX = Total
df_GroupeAgePremierMariage['REGDEP_MAR'] = df_GroupeAgePremierMariage['REGDEP_MAR'].str[-2:]
df_GroupeAgePremierMariage = df_GroupeAgePremierMariage.rename(columns={'REGDEP_MAR': 'DEP_MAR'})

df_NationaliteEpoux = pd.read_csv("data/datafiles/weddings/Dep4.csv", delimiter=';', dtype=str)
# Suppression des DOM-TOM, du total sur la France métrropolitaine et sur la France entière
df_NationaliteEpoux = df_NationaliteEpoux[df_NationaliteEpoux['REGDEP_DOMI'].apply(lambda x: len(x) == 4)]
df_NationaliteEpoux = df_NationaliteEpoux[~df_NationaliteEpoux['REGDEP_DOMI'].str.endswith('XX')] # XX = Total
df_NationaliteEpoux['REGDEP_DOMI'] = df_NationaliteEpoux['REGDEP_DOMI'].str[-2:]
df_NationaliteEpoux = df_NationaliteEpoux.rename(columns={'REGDEP_DOMI': 'DEP_DOMI'})

df_PaysNaissanceEpoux = pd.read_csv("data/datafiles/weddings/Dep5.csv", delimiter=';', dtype=str)
# Suppression des DOM-TOM, du total sur la France métrropolitaine et sur la France entière
df_PaysNaissanceEpoux = df_PaysNaissanceEpoux[df_PaysNaissanceEpoux['REGDEP_DOMI'].apply(lambda x: len(x) == 4)]
df_PaysNaissanceEpoux = df_PaysNaissanceEpoux[~df_PaysNaissanceEpoux['REGDEP_DOMI'].str.endswith('XX')] # XX = Total
df_PaysNaissanceEpoux['REGDEP_DOMI'] = df_PaysNaissanceEpoux['REGDEP_DOMI'].str[-2:]
df_PaysNaissanceEpoux = df_PaysNaissanceEpoux.rename(columns={'REGDEP_DOMI': 'DEP_DOMI'})

df_RepartitionMensuelleMariages = pd.read_csv("data/datafiles/weddings/Dep6.csv", delimiter=';', dtype=str)
# Suppression des DOM-TOM, du total sur la France métrropolitaine et sur la France entière
df_RepartitionMensuelleMariages = df_RepartitionMensuelleMariages[df_RepartitionMensuelleMariages['REGDEP_MAR'].apply(lambda x: len(x) == 4)]
df_RepartitionMensuelleMariages = df_RepartitionMensuelleMariages[~df_RepartitionMensuelleMariages['REGDEP_MAR'].str.endswith('XX')] # XX = Total
df_RepartitionMensuelleMariages['REGDEP_MAR'] = df_RepartitionMensuelleMariages['REGDEP_MAR'].str[-2:]
df_RepartitionMensuelleMariages = df_RepartitionMensuelleMariages.rename(columns={'REGDEP_MAR': 'DEP_MAR'})


# DF Popultation -----------------------------------------------------------------------------
def process_demographic_data(file_path, columns_to_merge, value_columns, type_stat):
    df = pd.read_csv(file_path, delimiter=';', dtype=str)
    df = df.dropna()
    df['CODGEO'] = df['CODGEO'].apply(lambda x: '0' + str(x) if len(str(x)) == 4 else x)
    df_merge = pd.merge(df, df_communes, left_on='CODGEO', right_on='COM')
    df_merge = df_merge[columns_to_merge]
    for col in value_columns:
        df_merge[col] = pd.to_numeric(df_merge[col], errors='coerce')
    df_merge = pd.melt(df_merge, id_vars=['CODGEO'], var_name='annee', value_name='valeur_stat')

    if value_columns[1].startswith(('P', 'D')) and value_columns[1][1:3].isdigit():
        df_merge['annee_debut'] = df_merge.apply(lambda x: int('20' + x['annee'][1:3]) if x['annee'].startswith('P') else int('19' + x['annee'][1:3]), axis=1)
        df_merge['annee_fin'] = df_merge.apply(lambda x: int('20' + x['annee'][1:3]) if x['annee'].startswith('P') else int('19' + x['annee'][1:3]), axis=1)
    else:
        if type_stat == 'naissances' : 
            df_merge['annee_debut'] = df_merge.apply(lambda x: int(x['annee'][4:6]) + 2000 if x['annee'].startswith(('NAIS20', 'NAIS14', 'NAIS09')) else int(x['annee'][4:6]) + 1900 if x['annee'].startswith('NAIS') else None, axis=1)
            df_merge['annee_fin'] = df_merge.apply(lambda x: int(x['annee'][6:]) + 2000 if x['annee'].startswith(('NAIS20', 'NAIS14', 'NAIS09','NAIS99')) else int(x['annee'][6:]) + 1900 if x['annee'].startswith('NAIS') else None, axis=1)
        elif type_stat == 'décès' :
            df_merge['annee_debut'] = df_merge.apply(lambda x: int(x['annee'][4:6]) + 2000 if x['annee'].startswith(('DECE20','DECE14', 'DECE09')) else int(x['annee'][4:6]) + 1900 if x['annee'].startswith('DECE') else None, axis=1)
            df_merge['annee_fin'] = df_merge.apply(lambda x: int(x['annee'][6:]) + 2000 if x['annee'].startswith(('DECE20','DECE14', 'DECE09','DECE99')) else int(x['annee'][6:]) + 1900 if x['annee'].startswith('DECE') else None, axis=1)
    
    df_merge['type_stat'] = type_stat
    df_merge = df_merge.drop('annee', axis=1)
    return df_merge

# Popultation -----------------------------------------------------------------------------
df_pop = process_demographic_data(
    "data/datafiles/population/France_hors_Mayotte.CSV",
    ['CODGEO','P20_POP', 'P14_POP','P09_POP','D99_POP', 'D90_POP', 'D82_POP','D75_POP','D68_POP'],
    ['P20_POP', 'P14_POP','P09_POP','D99_POP', 'D90_POP', 'D82_POP','D75_POP','D68_POP'],
    'population'
)

# Logement -----------------------------------------------------------------------------
df_log = process_demographic_data(
    "data/datafiles/population/France_hors_Mayotte.CSV",
    ['CODGEO','P20_LOG', 'P14_LOG','P09_LOG','D99_LOG', 'D90_LOG', 'D82_LOG','D75_LOG','D68_LOG'],
    ['P20_LOG', 'P14_LOG','P09_LOG','D99_LOG', 'D90_LOG', 'D82_LOG','D75_LOG','D68_LOG'],
    'logement'
)

# Naissances -----------------------------------------------------------------------------
df_nais = process_demographic_data(
    "data/datafiles/population/France_hors_Mayotte.CSV",
    ['CODGEO', 'NAIS1420', 'NAIS0914', 'NAIS9909', 'NAIS9099', 'NAIS8290', 'NAIS7582', 'NAIS6875'],
    ['NAIS1420', 'NAIS0914', 'NAIS9909', 'NAIS9099', 'NAIS8290', 'NAIS7582', 'NAIS6875'],
    'naissances'
)

# Décès -----------------------------------------------------------------------------
df_deces = process_demographic_data(
    "data/datafiles/population/France_hors_Mayotte.CSV",
    ['CODGEO', 'DECE1420', 'DECE0914', 'DECE9909', 'DECE9099', 'DECE8290', 'DECE7582', 'DECE6875'],
    ['DECE1420', 'DECE0914', 'DECE9909', 'DECE9099', 'DECE8290', 'DECE7582', 'DECE6875'],
    'décès'
)

# Concatenation -----------------------------------------------------------------------------
df_combined_pop = pd.concat([df_pop, df_log, df_nais, df_deces]).reset_index(drop=True)
df_combined_pop['annee_debut'] = df_combined_pop['annee_debut'].astype(int)
df_combined_pop['annee_fin'] = df_combined_pop['annee_fin'].astype(int)

new_column_order = ['CODGEO', 'annee_debut', 'annee_fin', 'type_stat', 'valeur_stat']
df_combined_pop = df_combined_pop[new_column_order]