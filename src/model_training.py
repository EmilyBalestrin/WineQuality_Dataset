import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score


def split_data(df):
    X = df.drop(['quality', 'good_quality'], axis=1)
    y = df['good_quality']
    return train_test_split(X, y, test_size=0.2, random_state=42)


def evaluate_model(y_test, y_pred, model_name):
    acc = accuracy_score(y_test, y_pred)
    print(f"\n [{model_name}] Acurácia: {acc:.4f}")
    print(f" Relatório de Classificação ({model_name}):")
    print(classification_report(y_test, y_pred))


def train_random_forest(df):
    X_train, X_test, y_train, y_test = split_data(df)

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    evaluate_model(y_test, y_pred, "Random Forest")

    # Matriz de confusão
    cm = confusion_matrix(y_test, y_pred)
    plt.figure(figsize=(6, 4))
    sns.heatmap(cm, annot=True, fmt="d", cmap='Blues')
    plt.title("Random Forest - Matriz de Confusão")
    plt.xlabel("Previsto")
    plt.ylabel("Real")
    plt.tight_layout()
    plt.savefig('results/confusion_matrix_rf.png')
    plt.clf()

    # Importância das features
    feature_importances = pd.Series(model.feature_importances_, index=X_train.columns)
    feature_importances = feature_importances.sort_values(ascending=False)

    plt.figure(figsize=(10, 6))
    sns.barplot(x=feature_importances.values, y=feature_importances.index, hue=feature_importances.index, palette='viridis', legend=False)
    plt.title("Random Forest - Importância das Variáveis")
    plt.tight_layout()
    plt.savefig('results/feature_importances_rf.png')
    plt.clf()


def train_logistic_regression(df):
    X_train, X_test, y_train, y_test = split_data(df)

    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    evaluate_model(y_test, y_pred, "Logistic Regression")

    # Matriz de confusão
    cm = confusion_matrix(y_test, y_pred)
    plt.figure(figsize=(6, 4))
    sns.heatmap(cm, annot=True, fmt="d", cmap='Greens')
    plt.title("Logistic Regression - Matriz de Confusão")
    plt.xlabel("Previsto")
    plt.ylabel("Real")
    plt.tight_layout()
    plt.savefig('results/confusion_matrix_logreg.png')
    plt.clf()


def train_decision_tree(df):
    X_train, X_test, y_train, y_test = split_data(df)

    model = DecisionTreeClassifier(random_state=42)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    evaluate_model(y_test, y_pred, "Decision Tree")

    # Matriz de confusão
    cm = confusion_matrix(y_test, y_pred)
    plt.figure(figsize=(6, 4))
    sns.heatmap(cm, annot=True, fmt="d", cmap='Oranges')
    plt.title("Decision Tree - Matriz de Confusão")
    plt.xlabel("Previsto")
    plt.ylabel("Real")
    plt.tight_layout()
    plt.savefig('results/confusion_matrix_dtree.png')
    plt.clf()
