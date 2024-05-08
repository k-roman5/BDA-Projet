import pandas as pd

def read_csv(file_path, delimiter=',', dtype=str):
    return pd.read_csv(file_path, delimiter=delimiter, dtype=dtype)

def clean_csv(file_path, columns_to_drop, filter_column=None, filter_value=None):
    df = read_csv(file_path)
    if filter_column is not None and filter_value is not None:
        df = df[df[filter_column] == filter_value]
    df = df.drop(columns=columns_to_drop, axis=1)
    return df

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
