import pandas as pd

def load_wine_data(path='data/winequality-red.csv'):
    df = pd.read_csv(path, sep=';')  # Dataset usa ; como separador
    return df

def clean_data(df):
    # Aqui você pode fazer ajustes se quiser, por enquanto só retorna o mesmo
    return df
