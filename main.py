from src.data_preparation import load_wine_data, clean_data

# Carregar e limpar os dados
df = load_wine_data()
df = clean_data(df)

# Exibir amostra dos dados
print("\nPrimeiras linhas:")
print(df.head())

print("\nInformações:")
print(df.info())

print("\nEstatísticas descritivas:")
print(df.describe())
