# DATASET

* Dataset sintetico creato in Python tramite generatore parametrico.
* Numero recensioni: 350 (180 negative, 170 positive; Housekeeping 118, F&B 117, Reception 115).
* Reparti:

  * Housekeeping
  * Reception
  * F&B
* Sentiment:

  * positivo
  * negativo

# Motivazioni dataset sintetico

* La traccia richiede esplicitamente dati generati ad hoc.
* Nessun utilizzo di dati personali o recensioni reali.
* Maggiore controllo sulle classi e sulla distribuzione dei dati.
* Possibilità di introdurre recensioni ambigue e casi limite.

# Caratteristiche del dataset

* Presenza di:

  * sinonimi
  * lunghezze variabili
  * recensioni miste
  * rumore testuale moderato

* Separazione tra:

  * dataset RAW
  * dataset CLEANED

# Dataset RAW

* Simula recensioni realistiche.
* Contiene variabilità linguistica e casi ambigui.
* Utilizzato per simulare input reale.

# Dataset CLEANED

* Utilizzato per il training ML.
* Include:

  * lowercasing
  * rimozione punteggiatura
  * rimozione stopwords
  * tokenizzazione

# Limiti del dataset

* Dataset sintetico e relativamente controllato.
* Possibile presenza di pattern ripetitivi.
* Minore variabilità rispetto a dati reali.
* Possibile accuracy ottimistica rispetto a contesti reali.

# EDA - EXPLORATORY DATA ANALYSIS

# Analisi iniziale

* Analisi distribuzione:

  * sentiment
  * reparti
* Utilizzo di grafici countplot con Seaborn.

# Analisi parole frequenti

* Estrazione parole più frequenti:

  * recensioni positive
  * recensioni negative
* Utilizzo stopwords italiane tramite NLTK.

# Insight principali

## Housekeeping

* Criticità legate a:

  * pulizia
  * capelli
  * stanza sporca
* Esperienze percepite come variabili tra clienti.

## Reception

* Aspetti positivi:

  * disponibilità personale

* Problemi principali:

  * lentezza
  * attese
  * percezione di scortesia

## F&B

* Aspetti positivi:

  * qualità cibo
  * varietà colazione

* Criticità:

  * lentezza servizio
  * aspettative non soddisfatte

# Considerazioni EDA

* Il dataset risulta relativamente bilanciato.
* Alcune recensioni risultano semanticamente ambigue.
* Presenza di overlap lessicale tra reparti.

# MODELLO SENTIMENT

# Pipeline utilizzata

Pipeline:
testo
↓
preprocessing
↓
TF-IDF
↓
Logistic Regression
↓
predizione

# Algoritmi scelti

## TF-IDF

Scelto per:

* semplicità
* interpretabilità
* efficacia su dataset testuali piccoli

## Logistic Regression

Scelta per:

* velocità
* semplicità
* ottime prestazioni su classificazione testuale

# Risultati sentiment

* Accuracy: 97,1%
* Dataset test: 20%
* Train/Test split: 80/20

# Considerazioni risultati

* Sul test set: recall negativo 1,00, recall positivo 0,94.
* Il modello intercetta bene recensioni negative.
* Utile in ambito hotel per individuare rapidamente criticità.

# Limiti

* Dataset sintetico può produrre accuracy ottimistica.
* Possibile apprendimento di pattern stilistici ripetitivi.

# MODELLO CLASSIFICAZIONE REPARTI

# Problema ML

Classificazione multiclass:

* Housekeeping
* Reception
* F&B

# Risultati

* Accuracy: 91,4%

# Osservazioni

Valori per classe sul test set:

* Housekeeping: F1 0,90
* F&B: F1 0,92
* Reception: F1 0,93

## F&B

* Lessico molto specifico:

  * colazione
  * buffet
  * ristorante
  * cibo

## Reception

* Prestazioni molto buone.
* Presenza di keyword forti:

  * check-in
  * pagamento
  * reception

## Housekeeping

* Classe più difficile.
* Presenza di termini condivisi:

  * camera
  * servizio
  * pulizia

# Considerazioni confusion matrix

* Alcune recensioni vengono confuse tra:

  * Housekeeping
  * Reception

Possibile motivo:

* recensioni semanticamente miste
* presenza contemporanea di problemi diversi

# Insight importante

La presenza di errori realistici dimostra:

* ambiguità naturale del linguaggio
* limiti della classificazione automatica
* comportamento coerente del modello

# SCELTE TECNICHE

# Struttura progetto

Utilizzo di:

* cartelle separate
* file modulari
* dataset RAW e CLEANED
* script Python distinti

# Motivazioni

* maggiore leggibilità
* migliore organizzazione
* facilità di manutenzione
* pipeline più professionale

# Librerie principali

* pandas
* scikit-learn
* matplotlib
* seaborn
* nltk
* joblib
* streamlit (fase dashboard)

# Motivazione notebook vs .py

Scelta file .py per:

* modularità
* ordine
* struttura professionale

Notebook considerati utili principalmente per:

* EDA
* prototipazione
* sperimentazione

# TRAIN / TEST SPLIT

Il dataset è stato suddiviso utilizzando un approccio train/test split con proporzione 80/20.

* 80% dei dati utilizzati per il training
* 20% dei dati utilizzati per il testing

Questo approccio consente di valutare il comportamento del modello su dati non visti durante la fase di addestramento.

# DASHBOARD STREAMLIT

È stata sviluppata una dashboard interattiva tramite Streamlit per consentire:

* inserimento recensioni manuali
* analisi automatica del sentiment
* classificazione reparto
* visualizzazione probabilità modello

# Pipeline dashboard

Input utente
↓
preprocessing testo
↓
TF-IDF vectorization
↓
modello ML
↓
predizione finale

# Motivazioni utilizzo Streamlit

* semplicità implementazione
* rapidità prototipazione
* interfaccia chiara e leggera
* integrazione semplice con modelli Python

# Esempi di ambiguità modello

Recensione:
"Camera pulita e personale disponibile"

Risultato:

* Sentiment: positivo
* Department: Reception

Possibile spiegazione:
Il modello assegna maggiore peso a espressioni come "personale disponibile", frequentemente associate al reparto Reception.

Considerazione:
Le recensioni contenenti elementi appartenenti a più reparti possono generare classificazioni ambigue.

Il modello mostra alcune difficoltà nella gestione di recensioni semanticamente ambigue o contenenti sinonimi non presenti nel dataset di training. Questo comportamento evidenzia uno dei principali limiti degli approcci basati su TF-IDF e Bag-of-Words, che non comprendono realmente il significato contestuale delle parole ma si basano principalmente sulla frequenza e distribuzione statistica dei termini.

# LIMITI NLP OSSERVATI

Durante i test sono emerse alcune limitazioni tipiche dei modelli NLP basati su TF-IDF e Bag-of-Words.

Esempi osservati:

* difficoltà nella gestione di sinonimi non presenti nel dataset
* classificazione ambigua di recensioni contenenti aspetti positivi e negativi contemporaneamente
* sensibilità alla distribuzione statistica delle parole

Esempio:
"Camera pulita ma personale molto scortese"

In alcuni casi il modello può assegnare peso maggiore agli elementi positivi presenti nella frase.

Questo comportamento evidenzia come il modello non comprenda realmente il significato semantico del testo, ma operi tramite associazioni statistiche apprese durante il training.

# ARCHITETTURA PROGETTO

Il progetto è stato organizzato in maniera modulare attraverso cartelle separate:

* app/
* src/
* data/raw
* data/cleaned
* models/

Questa struttura consente:

* maggiore ordine
* manutenzione semplificata
* separazione responsabilità
* migliore leggibilità del codice

Approccio ispirato al principio:
"divide et impera"

# LIMITI

* Dataset sintetico.
* Variabilità linguistica limitata.
* Assenza di sarcasmo reale.
* Numero ridotto di classi.
* Assenza di lemmatizzazione.

# POSSIBILI MIGLIORAMENTI

* utilizzo dati reali
* lemmatizzazione
* stemming
* supporto multilingua
* modelli più avanzati
* aumento variabilità dataset
* utilizzo embeddings NLP

# BATCH PREDICTION (GIÀ IMPLEMENTATA)

La dashboard include già il supporto all'upload CSV per:

* analisi multipla recensioni
* predizione automatica batch
* esportazione risultati con timestamp

Questa funzionalità simula un possibile utilizzo reale in ambito aziendale per l'analisi automatizzata dei feedback clienti.
