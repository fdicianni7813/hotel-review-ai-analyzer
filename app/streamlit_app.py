import streamlit as st
import joblib
import sys
import os
import pandas as pd
from datetime import datetime

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.preprocessing import clean_text


BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

sentiment_model = joblib.load(
    os.path.join(BASE_DIR, "models", "sentiment_model.pkl")
)

sentiment_vectorizer = joblib.load(
    os.path.join(BASE_DIR, "models", "sentiment_vectorizer.pkl")
)

department_model = joblib.load(
    os.path.join(BASE_DIR, "models", "department_model.pkl")
)

department_vectorizer = joblib.load(
    os.path.join(BASE_DIR, "models", "department_vectorizer.pkl")
)


# TITOLO APP
st.title("🏨 Hotel Review AI Analyzer")

st.markdown("""
Questa applicazione utilizza tecniche di Machine Learning e NLP
per analizzare recensioni alberghiere e prevedere:

- sentiment della recensione
- reparto coinvolto
""")


# INPUT TESTO
review = st.text_area(
    "✍️ Inserisci una recensione",
    placeholder="Esempio: Camera molto pulita ma check-in lento..."
)

# BOTTONE PREDIZIONE
if st.button("Analizza Recensione"):

    # PREPROCESSING TESTO
    cleaned_review = clean_text(review)

    # VECTORIZATION SENTIMENT
    review_sentiment_vectorized = sentiment_vectorizer.transform(
        [cleaned_review]
    )

    # PREDIZIONE SENTIMENT
    sentiment_prediction = sentiment_model.predict(
        review_sentiment_vectorized
    )[0]

    sentiment_probability = sentiment_model.predict_proba(
        review_sentiment_vectorized
    ).max()

    # VECTORIZATION DEPARTMENT
    review_department_vectorized = department_vectorizer.transform(
        [cleaned_review]
    )

    # PREDIZIONE DEPARTMENT
    department_prediction = department_model.predict(
        review_department_vectorized
    )[0]

    department_probability = department_model.predict_proba(
        review_department_vectorized
    ).max()

   # OUTPUT
    st.subheader("📊 Risultati Analisi")
    
    # EMOJI SENTIMENT
    if sentiment_prediction == "positivo":
        sentiment_emoji = "🟢"
    else:
        sentiment_emoji = "🔴"
    
    st.markdown(f"""
    ### {sentiment_emoji} Sentiment
    **Predizione:** {sentiment_prediction}
    
    **Confidenza modello:** {sentiment_probability:.2%}
    """)
    
    st.markdown(f"""
    ### 🏢 Reparto Coinvolto
    **Predizione:** {department_prediction}
    
    **Confidenza modello:** {department_probability:.2%}
    """)

    st.divider()

st.header("📂 Analisi Batch CSV")

uploaded_file = st.file_uploader(
    "Carica un file CSV con una colonna 'body'",
    type=["csv"]
)

if uploaded_file is not None:

    # LETTURA CSV
    batch_df = pd.read_csv(uploaded_file)

    st.write("Anteprima dataset:")
    st.dataframe(batch_df.head())

    # CONTROLLO COLONNA
    if "body" not in batch_df.columns:
        st.error("Il CSV deve contenere una colonna chiamata 'body'.")

    else:

        # PREPROCESSING
        batch_df["cleaned_body"] = batch_df["body"].apply(clean_text)

        # VECTORIZATION SENTIMENT
        sentiment_vectors = sentiment_vectorizer.transform(
            batch_df["cleaned_body"]
        )

        # PREDICTION SENTIMENT
        batch_df["predicted_sentiment"] = sentiment_model.predict(
            sentiment_vectors
        )

        # PROBABILITÀ SENTIMENT
        batch_df["sentiment_confidence"] = sentiment_model.predict_proba(
            sentiment_vectors
        ).max(axis=1)

        # VECTORIZATION DEPARTMENT
        department_vectors = department_vectorizer.transform(
            batch_df["cleaned_body"]
        )

        # PREDICTION DEPARTMENT
        batch_df["predicted_department"] = department_model.predict(
            department_vectors
        )

        # PROBABILITÀ DEPARTMENT
        batch_df["department_confidence"] = department_model.predict_proba(
            department_vectors
        ).max(axis=1)

        st.success("Analisi completata.")

        st.dataframe(batch_df.head())

        # TIMESTAMP
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

        output_filename = f"predictions_{timestamp}.csv"

        # EXPORT CSV
        csv = batch_df.to_csv(index=False).encode("utf-8")

        st.download_button(
            label="⬇️ Scarica risultati CSV",
            data=csv,
            file_name=output_filename,
            mime="text/csv"
        )