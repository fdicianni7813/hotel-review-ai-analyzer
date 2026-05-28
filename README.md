````md
# ⚙️ Pipeline progetto

## 1. Generazione dataset

Dataset sintetico contenente:

- recensioni positive
- recensioni negative
- recensioni ambigue
- casi misti

### Colonne dataset

- `id`
- `title`
- `body`
- `department`
- `sentiment`

---

## 2. Preprocessing NLP

Operazioni eseguite:

- lowercasing
- rimozione punteggiatura
- tokenizzazione
- rimozione stopwords

---

## 3. Training modelli ML

### Sentiment Analysis

- TF-IDF
- Logistic Regression

### Department Classification

- TF-IDF
- Logistic Regression multiclass

### Train/Test Split

- 80% training
- 20% testing

### Metriche utilizzate

- Accuracy
- F1-score
- Confusion Matrix

---

# 📊 Risultati principali

## Sentiment Model

- Accuracy: ~96%

## Department Classifier

- Accuracy: ~83%

Il progetto include esempi di recensioni ambigue per simulare casi realistici.

---

# 🖥️ Dashboard Streamlit

La dashboard consente:

- inserimento recensione manuale
- analisi sentiment
- classificazione reparto
- visualizzazione confidence score
- upload CSV batch
- esportazione CSV risultati

---

# 🚀 Avvio progetto

## 1. Attivare ambiente virtuale

### Windows

```bash
venv\Scripts\activate
````

---

## 2. Installare dipendenze

```bash
pip install -r requirements.txt
```

---

## 3. Generare dataset

```bash
python src/dataset_generator.py
```

---

## 4. Eseguire preprocessing

```bash
python src/preprocessing.py
```

---

## 5. Addestrare modelli

```bash
python src/train_sentiment.py
python src/train_department.py
```

---

## 6. Avviare dashboard

```bash
streamlit run app/streamlit_app.py
```

---

# ⚠️ Limiti del progetto

* dataset sintetico
* limitata variabilità linguistica
* no comprensione semantica reale
* modelli basati su Bag-of-Words / TF-IDF

---

# 🔮 Possibili miglioramenti

* utilizzo dataset reali
* embeddings NLP
* modelli Transformer/BERT
* supporto multilingua
* lemmatizzazione avanzata
* deploy cloud

---

# 👨‍💻 Autore

Francesco Di Cianni

Project Work universitario - Informatica per le Aziende Digitali

```
```
