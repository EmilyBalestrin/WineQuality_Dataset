from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import pandas as pd

def compare_models(models_results):
    # Cada modelo é um dicionário com nome e y_test/y_pred
    summary = []

    for result in models_results:
        name = result['name']
        y_test = result['y_test']
        y_pred = result['y_pred']

        summary.append({
            'Modelo': name,
            'Acurácia': round(accuracy_score(y_test, y_pred), 4),
            'Precisão': round(precision_score(y_test, y_pred), 4),
            'Revocação': round(recall_score(y_test, y_pred), 4),
            'F1-Score': round(f1_score(y_test, y_pred), 4)
        })

    df_resultados = pd.DataFrame(summary)
    print("\n Comparativo de Desempenho dos Modelos:\n")
    print(df_resultados.to_string(index=False))

    # Salvar como CSV
    df_resultados.to_csv("results/model_comparison.csv", index=False)
