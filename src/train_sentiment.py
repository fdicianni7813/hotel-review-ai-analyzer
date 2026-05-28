import pandas as pd
import joblib

from sklearn.model_selection import train_test_split

from sklearn.feature_extraction.text import TfidfVectorizer

from sklearn.linear_model import LogisticRegression

from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix


# LOAD DATASET
df = pd.read_csv("data/cleaned/reviews_cleaned.csv")


# INPUT E TARGET
X = df["cleaned_body"]

y = df["sentiment"]


# TRAIN / TEST SPLIT
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# TF-IDF
vectorizer = TfidfVectorizer()

X_train_vectorized = vectorizer.fit_transform(X_train)

X_test_vectorized = vectorizer.transform(X_test)


# MODELLO
model = LogisticRegression()

model.fit(X_train_vectorized, y_train)


# PREDIZIONI
predictions = model.predict(X_test_vectorized)


# METRICHE
accuracy = accuracy_score(y_test, predictions)

print("\nAccuracy:")
print(accuracy)

print("\nClassification Report:")
print(classification_report(y_test, predictions))


# CONFUSION MATRIX
cm = confusion_matrix(y_test, predictions)

print("\nConfusion Matrix:")
print(cm)


# SALVATAGGIO MODELLO
joblib.dump(model, "models/sentiment_model.pkl")


# SALVATAGGIO VECTORIZER
joblib.dump(vectorizer, "models/sentiment_vectorizer.pkl")

print("\nModello sentiment salvato correttamente.")