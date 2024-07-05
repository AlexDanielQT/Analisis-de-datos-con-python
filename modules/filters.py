import pandas as pd

def filter_data(df, departamentos, provincias, distritos):
    df_copy = df.copy()

    if len(departamentos) > 0:
        df_copy = df_copy[df_copy['DD'].isin(departamentos)]
    if len(provincias) > 0:
        df_copy = df_copy[df_copy['PP'].isin(provincias)]
    if len(distritos) > 0:
        df_copy = df_copy[df_copy['DI'].isin(distritos)]

    return df_copy
