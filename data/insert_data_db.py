import io
from connect_db import connection
from format_data import read_csv, clean_csv, regdep_formatting, process_demographic_data, concat_dataframes

### DATA ###
df_region = clean_csv("data/datafiles/area/v_region_2023.csv", ['CHEFLIEU', 'TNCC', 'NCC', 'NCCENR'])
df_departement = clean_csv("data/datafiles/area/v_departement_2023.csv", ['CHEFLIEU', 'TNCC', 'NCC', 'NCCENR'])
df_communes = clean_csv("data/datafiles/area/v_commune_2023.csv", 
                                 ['TYPECOM', 'REG', 'CTCD', 'ARR', 'TNCC', 'NCC', 'NCCENR', 'CAN', 'COMPARENT'], 
                                 filter_column='TYPECOM', filter_value='COM')
df_cheflieudep = clean_csv("data/datafiles/area/v_departement_2023.csv", ['REG', 'TNCC', 'NCC', 'NCCENR', 'LIBELLE'])
df_cheflieureg = clean_csv("data/datafiles/area/v_region_2023.csv", ['TNCC', 'NCC', 'NCCENR', 'LIBELLE'])
# DF Mariages
df_GroupeAgeEpoux = read_csv("data/datafiles/weddings/Dep1.csv", delimiter=';')
df_GroupeAgeEpoux = regdep_formatting(df_GroupeAgeEpoux)
df_EtatMatrimonialAnterieur = read_csv("data/datafiles/weddings/Dep2.csv", delimiter=';')
df_EtatMatrimonialAnterieur = regdep_formatting(df_EtatMatrimonialAnterieur)
df_GroupeAgePremierMariage = read_csv("data/datafiles/weddings/Dep3.csv", delimiter=';')
df_GroupeAgePremierMariage = regdep_formatting(df_GroupeAgePremierMariage)
df_NationaliteEpoux = read_csv("data/datafiles/weddings/Dep4.csv", delimiter=';')
df_NationaliteEpoux = regdep_formatting(df_NationaliteEpoux)
df_PaysNaissanceEpoux = read_csv("data/datafiles/weddings/Dep5.csv", delimiter=';')
df_PaysNaissanceEpoux = regdep_formatting(df_PaysNaissanceEpoux)
df_RepartitionMensuelleMariages = read_csv("data/datafiles/weddings/Dep6.csv", delimiter=';')
df_RepartitionMensuelleMariages = regdep_formatting(df_RepartitionMensuelleMariages)
# DF Population
df_pop = process_demographic_data(
    "data/datafiles/population/France_hors_Mayotte.CSV",
    ['CODGEO','P20_POP', 'P14_POP','P09_POP','D99_POP', 'D90_POP', 'D82_POP','D75_POP','D68_POP'],
    'population',
    df_communes['COM']
)
df_log = process_demographic_data(
    "data/datafiles/population/France_hors_Mayotte.CSV",
    ['CODGEO','P20_LOG', 'P14_LOG','P09_LOG','D99_LOG', 'D90_LOG', 'D82_LOG','D75_LOG','D68_LOG'],
    'logement',
    df_communes['COM']
)
df_nais = process_demographic_data(
    "data/datafiles/population/France_hors_Mayotte.CSV",
    ['CODGEO', 'NAIS1420', 'NAIS0914', 'NAIS9909', 'NAIS9099', 'NAIS8290', 'NAIS7582', 'NAIS6875'],
    'naissances',
    df_communes['COM']
)
df_deces = process_demographic_data(
    "data/datafiles/population/France_hors_Mayotte.CSV",
    ['CODGEO', 'DECE1420', 'DECE0914', 'DECE9909', 'DECE9099', 'DECE8290', 'DECE7582', 'DECE6875'],
    'décès',
    df_communes['COM']
)
df_combined_pop = concat_dataframes([df_pop, df_log, df_nais, df_deces])
new_column_order = ['CODGEO', 'annee_debut', 'annee_fin', 'type_stat', 'valeur_stat']
df_combined_pop = df_combined_pop[new_column_order]
############


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
copy_data_to_db_table(df_GroupeAgeEpoux, 'groupeageepoux', cursor)
copy_data_to_db_table(df_EtatMatrimonialAnterieur, 'etatmatrimonialanterieur', cursor)
copy_data_to_db_table(df_GroupeAgePremierMariage, 'groupeagepremiermariage', cursor)
copy_data_to_db_table(df_NationaliteEpoux, 'nationaliteepoux', cursor)
copy_data_to_db_table(df_PaysNaissanceEpoux, 'paysnaissanceepoux', cursor)
copy_data_to_db_table(df_RepartitionMensuelleMariages, 'repartitionmensuellemariages', cursor)

connection.commit()
print("Données importées avec succès !")