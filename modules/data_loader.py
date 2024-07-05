import pandas as pd

def load_data():
    file_path_limpio = './data/DATA6.csv'
    file_path_mapeo = './data/DATA_DE_MAPEO_INPE.csv'
    file_path_establecimientos = './data/DATA_DE_PENALES_INPE.csv'

    df_origin = pd.read_csv(file_path_limpio, encoding='utf-8')
    df_mapeo = pd.read_csv(file_path_mapeo, encoding='utf-8')
    df_establecimientos = pd.read_csv(file_path_establecimientos, encoding='utf-8')

    return df_origin, df_mapeo, df_establecimientos
