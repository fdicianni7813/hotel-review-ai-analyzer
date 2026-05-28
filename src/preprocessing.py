import pandas as pd
import re
import os

from nltk.corpus import stopwords
import nltk

# DOWNLOAD STOPWORDS
try:
    stop_words = set(stopwords.words("italian"))
except:
    nltk.download("stopwords")
    stop_words = set(stopwords.words("italian"))

os.makedirs("data/cleaned", exist_ok=True)


# FUNZIONE PREPROCESSING
def clean_text(text):

    # lowercase
    text = text.lower()

    # rimozione punteggiatura
    text = re.sub(r"[^\w\s]", "", text)

    # tokenizzazione
    words = text.split()

    # rimozione stopwords
    words = [word for word in words if word not in stop_words]

    # ricostruzione frase
    cleaned_text = " ".join(words)

    return cleaned_text


# ESECUZIONE SCRIPT
if __name__ == "__main__":

    # LOAD DATASET
    df = pd.read_csv("data/raw/reviews.csv")

    # APPLICA PREPROCESSING
    df["cleaned_body"] = df["body"].apply(clean_text)

    # SALVA CLEANED DATASET
    df.to_csv("data/cleaned/reviews_cleaned.csv", index=False)

    print("Dataset cleaned salvato correttamente.")