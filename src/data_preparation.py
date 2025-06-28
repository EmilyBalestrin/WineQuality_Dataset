import pandas as pd

def load_wine_data(path='data/winequality-red.csv'):
    df = pd.read_csv(path, sep=',', encoding='utf-8')  # Agora com o separador correto
    print("\nColunas carregadas:")
    print(df.columns.tolist())
    return df

def clean_data(df):
    # Verificar valores ausentes
    print("\nValores ausentes por coluna:")
    print(df.isnull().sum())

    # Criar coluna binária: 1 se qualidade >= 7, senão 0
    df['good_quality'] = df['quality'].apply(lambda q: 1 if q >= 7 else 0)

    # Mostrar distribuição da nova coluna
    print("\nDistribuição da coluna 'good_quality':")
    print(df['good_quality'].value_counts())

    return df