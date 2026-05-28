import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
import re

from nltk.corpus import stopwords
import nltk

try:
    stop_words = set(stopwords.words('italian'))
except:
    nltk.download('stopwords')
    stop_words = set(stopwords.words('italian'))

df = pd.read_csv("data/raw/reviews.csv")

sns.countplot(data=df, x="sentiment")
plt.title("Distribuzione del Sentiment")
plt.show()

sns.countplot(data=df, x="department")
plt.title("Distribuzione per Reparto")
plt.show()

sns.countplot(data=df, x="department", hue="sentiment")
plt.title("Sentiment per Reparto")
plt.show()

def get_words(text):
    text = text.lower()
    text = re.sub(r"[^\w\s]", "", text)
    words = text.split()
    
    # rimuovi parole inutili
    words = [w for w in words if w not in stop_words and len(w) > 2]
    
    return words

all_words_pos = []
all_words_neg = []

for _, row in df.iterrows():
    words = get_words(row["body"])
    if row["sentiment"] == "positivo":
        all_words_pos.extend(words)
    else:
        all_words_neg.extend(words) 

print("\nParole più frequenti POSITIVE:")
print(Counter(all_words_pos).most_common(10))

print("\nParole più frequenti NEGATIVE:")
print(Counter(all_words_neg).most_common(10))

print(df.info())
print(df.head())
print("\nDistribuzione sentiment:")
print(df["sentiment"].value_counts())

print("\nDistribuzione reparti:")
print(df["department"].value_counts())

print("\nAnalisi parole per reparto e sentiment:")

for dept in df["department"].unique():
    print(f"\n=== {dept} ===")
    
    subset = df[df["department"] == dept]
    
    words_pos = []
    words_neg = []
    
    for _, row in subset.iterrows():
        words = get_words(row["body"])
        
        if row["sentiment"] == "positivo":
            words_pos.extend(words)
        else:
            words_neg.extend(words)
    
    print("\nTop parole POSITIVE:")
    print(Counter(words_pos).most_common(5))
    
    print("\nTop parole NEGATIVE:")
    print(Counter(words_neg).most_common(5))

