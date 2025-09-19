# app.py
import os
import streamlit as st
import pickle

# -----------------------------
# Load saved model, vectorizer & genre mapping
# -----------------------------


# Folder path jahan pickle files hain
pickle_folder = "Outputs"

with open(os.path.join(pickle_folder, "tfidf_vectorizer.pkl"), "rb") as f:
    vectorizer = pickle.load(f)

with open(os.path.join(pickle_folder, "best_logreg_model.pkl"), "rb") as f:
    model = pickle.load(f)

with open(os.path.join(pickle_folder, "label_encoder.pkl"), "rb") as f:
    genre_map = pickle.load(f)


# -----------------------------
# Streamlit UI
# -----------------------------
st.set_page_config(page_title="Movie Genre Predictor", layout="centered")
st.title("🎬 Movie Genre Predictor")
st.write("Enter a movie plot and get the predicted genre.")

# Text area for user input
user_plot = st.text_area("Movie Plot:", height=200)

# Predict button
if st.button("Predict Genre"):
    if user_plot.strip() == "":
        st.error("Please enter a movie plot!")
    else:
        # -----------------------------
        # Transform & Predict
        # -----------------------------
        X_input = vectorizer.transform([user_plot])    # transform user input
        prediction_num = model.predict(X_input)       # predict numeric label

        # Convert numeric prediction to genre name using the dictionary
        prediction_label = genre_map.get(prediction_num[0], "Unknown")

        st.success(f"Predicted Genre: {prediction_label}")

# -----------------------------
# Footer
# -----------------------------
st.markdown("---")
# st.markdown("Made  using Streamlit")
st.markdown("Made using Streamlit")
