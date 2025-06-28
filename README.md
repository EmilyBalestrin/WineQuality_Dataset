# 🍷 Análise e Classificação da Qualidade de Vinhos – Wine Quality Dataset

Este projeto tem como objetivo aplicar técnicas de **mineração de dados** para analisar a qualidade de vinhos, utilizando o `Wine Quality Dataset` (red wine) disponível publicamente no UCI Machine Learning Repository.

O projeto foi desenvolvido com **Python** e bibliotecas como `pandas`, `scikit-learn`, `matplotlib` e `seaborn`, atendendo aos critérios da disciplina **Tópicos Especiais em Computação I**.

---

## 📊 Sobre o Dataset

- **Nome:** Wine Quality - Red Wine
- **Origem:** [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/wine+quality)
- **Registros:** 1.599
- **Colunas:** 11 atributos físico-químicos + 1 coluna de qualidade sensorial

---

## ⚙️ Tecnologias e Bibliotecas

- Python 3.x
- pandas
- matplotlib
- seaborn
- scikit-learn

---

## 🧪 Técnicas Aplicadas

- Análise exploratória de dados (EDA)
- Classificação binária com:
  - ✅ Random Forest
  - ✅ Logistic Regression
  - ✅ Decision Tree
- Avaliação de desempenho:
  - Acurácia
  - Precisão
  - Revocação (Recall)
  - F1-Score
- Geração de gráficos:
  - Distribuição de qualidade
  - Heatmap de correlação
  - Boxplots por variável
  - Matrizes de confusão
  - Importância das variáveis
  - Gráfico comparativo de modelos

---

## 📊 Visualizações do Dataset
Esta seção apresenta algumas visualizações geradas a partir da análise exploratória do dataset de qualidade de vinhos.

### Mapa de Calor das Correlações
![correlation_heatmap](https://github.com/user-attachments/assets/a9abab1e-0a1b-4c2b-92d4-4e579aaf1518)

### Importância das Variáveis (Random Forest)
![feature_importances_rf](https://github.com/user-attachments/assets/1fb8e220-5632-4087-bac6-b19fda72302b)

### Comparação de Desempenho dos Modelos
![model_comparison_chart](https://github.com/user-attachments/assets/46db1168-559e-4742-ae80-35f3febb26cd)

### Distribuição de Vinhos (Bons vs. Ruins)
![good_quality_distribution](https://github.com/user-attachments/assets/c82685f6-b286-4ea4-938d-7e7aca449f3b)

### Distribuição das Notas de Qualidade
![quality_distribution](https://github.com/user-attachments/assets/588e2b3c-47cc-4163-96b3-f837d7a17223)

---

## 📁 Estrutura do Projeto

```
WineQuality-Dataset/
│
├── data/ # Dataset original (CSV)
├── results/ # Gráficos e comparações geradas
├── src/ # Código-fonte
│ ├── data_preparation.py
│ ├── evaluation.py
│ ├── model_training.py
│ └── visualization.py
├── 105140 - Emily L. Balestrin - Relatório.pdf
├── main.py # Script principal
├── README.md
└── requirements.txt # Bibliotecas utilizadas
```
---

# ▶️ Como Executar

## 1. **Clone o repositório:**

```bash
git clone https://github.com/EmilyBalestrin/WineQuality_Dataset.git
cd WineQuality-Dataset
```

## 2. **Crie um ambiente virtual (opcional, mas recomendado):**

```bash
python -m venv .venv
```

### Ative o ambiente virtual:

* No **Windows**:

```bash
.venv\Scripts\activate
```

* No **Linux/macOS**:

```bash
source .venv/bin/activate
```

## 3. **Instale as dependências:**

```bash
pip install -r requirements.txt
```

## 4. **Execute o script principal:**

```bash
python main.py
```

Todos os gráficos e resultados serão salvos automaticamente na pasta `results/`.
