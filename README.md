# 🏨 Hotel Review AI Analyzer

Progetto di Machine Learning e NLP per l’analisi automatica di recensioni alberghiere.

Il sistema è in grado di:

- classificare il sentiment delle recensioni (positivo / negativo)
- identificare il reparto coinvolto:
  - Housekeeping
  - Reception
  - F&B

Il progetto include:
- generazione dataset sintetico
- preprocessing NLP
- training modelli ML
- dashboard Streamlit
- batch prediction CSV
- esportazione risultati con timestamp

---

# 📌 Obiettivi del progetto

- Creare un dataset sintetico realistico di recensioni hotel
- Applicare tecniche base di NLP
- Addestrare modelli di classificazione testuale
- Analizzare performance tramite accuracy, F1-score e confusion matrix
- Realizzare una dashboard interattiva per inferenza live

---

# 🧠 Tecnologie utilizzate

- Python
- Pandas
- Scikit-learn
- NLTK
- Matplotlib
- Seaborn
- Streamlit
- Joblib

---

# 📂 Struttura progetto

```bash
project_work/
│
├── app/
│   └── streamlit_app.py
│
├── data/
│   ├── raw/
│   └── cleaned/
│
├── models/
│
├── src/
│   ├── dataset_generator.py
│   ├── preprocessing.py
│   ├── analysis.py
│   ├── train_sentiment.py
│   └── train_department.py
│
├── requirements.txt
└── README.md
```
# ⚙️ Pipeline progetto
1. Generazione dataset

Dataset sintetico contenente:

recensioni positive
recensioni negative
recensioni ambigue
casi misti

Colonne dataset:

id
title
body
department
sentiment
2. Preprocessing NLP

Operazioni eseguite:

lowercasing
rimozione punteggiatura
tokenizzazione
rimozione stopwords
3. Training modelli ML
Sentiment Analysis
TF-IDF
Logistic Regression
Department Classification
TF-IDF
Logistic Regression multiclass

Train/Test Split:

80% training
20% testing

Metriche:

Accuracy
F1-score
Confusion Matrix
📊 Risultati principali
Sentiment Model

Accuracy: ~94%

Department Classifier

Accuracy: ~90%

Il progetto include esempi di recensioni ambigue per simulare casi realistici.

🖥️ Dashboard Streamlit

La dashboard consente:

inserimento recensione manuale
analisi sentiment
classificazione reparto
visualizzazione confidence score
upload CSV batch
esportazione CSV risultati
🚀 Avvio progetto
1. Attivare ambiente virtuale

Windows:

venv\Scripts\activate
2. Installare dipendenze
pip install -r requirements.txt
3. Generare dataset
python src/dataset_generator.py
4. Eseguire preprocessing
python src/preprocessing.py
5. Addestrare modelli
python src/train_sentiment.py

python src/train_department.py
6. Avviare dashboard
streamlit run app/streamlit_app.py
⚠️ Limiti del progetto
dataset sintetico
limitata variabilità linguistica
no comprensione semantica reale
modelli basati su Bag-of-Words / TF-IDF
🔮 Possibili miglioramenti
utilizzo dataset reali
embeddings NLP
modelli Transformer/BERT
supporto multilingua
lemmatizzazione avanzata
deploy cloud


👨‍💻 Autore

Francesco Di Cianni

Project Work universitario - Informatica per le Aziende Digitali