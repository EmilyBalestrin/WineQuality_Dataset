from src.data_preparation import load_wine_data, clean_data
from src.model_training import train_random_forest

from src.evaluation import compare_models

# Reexecuta os modelos e coleta resultados para comparação
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier

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

from src.model_training import (
    train_random_forest,
    train_logistic_regression,
    train_decision_tree
)

train_random_forest(df)
train_logistic_regression(df)
train_decision_tree(df)

X = df.drop(['quality', 'good_quality'], axis=1)
y = df['good_quality']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

models = [
    ('Random Forest', RandomForestClassifier(n_estimators=100, random_state=42)),
    ('Logistic Regression', LogisticRegression(max_iter=1000)),
    ('Decision Tree', DecisionTreeClassifier(random_state=42))
]

results = []

for name, model in models:
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    results.append({'name': name, 'y_test': y_test, 'y_pred': y_pred})

compare_models(results)

