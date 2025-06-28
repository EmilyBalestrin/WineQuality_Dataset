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

print("\nColunas lidas:")
print(df.columns)

from src.visualization import (
    plot_quality_distribution,
    plot_good_quality_distribution,
    plot_correlation_heatmap,
    plot_boxplots
)

# Gerar gráficos
plot_quality_distribution(df)
plot_good_quality_distribution(df)
plot_correlation_heatmap(df)
plot_boxplots(df)

print("\nGráficos salvos na pasta /results")
