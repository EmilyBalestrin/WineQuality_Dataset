import seaborn as sns
import matplotlib.pyplot as plt

def plot_quality_distribution(df):
    sns.countplot(x='quality', hue='quality', data=df, palette='viridis', legend=False)
    plt.title("Distribuição das Notas de Qualidade")
    plt.xlabel("Qualidade")
    plt.ylabel("Quantidade")
    plt.tight_layout()
    plt.savefig('results/quality_distribution.png')
    plt.clf()

def plot_good_quality_distribution(df):
    sns.countplot(x='good_quality', data=df, palette='Set2')
    plt.title("Distribuição de Bons e Maus Vinhos")
    plt.xlabel("Bom (1) / Ruim (0)")
    plt.ylabel("Quantidade")
    plt.tight_layout()
    plt.savefig('results/good_quality_distribution.png')
    plt.clf()

def plot_correlation_heatmap(df):
    corr = df.corr()
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
    plt.title("Mapa de Calor das Correlações")
    plt.tight_layout()
    plt.savefig('results/correlation_heatmap.png')
    plt.clf()

def plot_boxplots(df):
    features = ['alcohol', 'sulphates', 'citric acid', 'volatile acidity', 'pH']
    for feature in features:
        sns.boxplot(x='good_quality', y=feature, data=df, palette='pastel')
        plt.title(f"{feature} vs Qualidade")
        plt.tight_layout()
        plt.savefig(f'results/boxplot_{feature}.png')
        plt.clf()
