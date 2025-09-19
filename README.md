🎬 Movie Genre Predictor – NLP Project

Predict the genre of a movie based solely on its plot description using Natural Language Processing (NLP) and Logistic Regression. This project demonstrates text preprocessing, feature extraction with TF-IDF, and multi-class classification, and is deployed as an interactive Streamlit web app.

📖 Table of Contents

Overview

Dataset

Tech Stack

Project Workflow

Model Performance

App Features

How to Run Locally

Deployment

Future Improvements

Acknowledgements

📝 Overview

This app predicts a movie’s genre (e.g., Drama, Comedy, Action, Romance, Thriller, Horror) based on its plot description. It uses TF-IDF vectorization and a Logistic Regression classifier tuned via GridSearchCV for optimal hyperparameters.

The model handles imbalanced data by using class weights and was evaluated on CountVectorizer and TF-IDF representations. The final deployment uses the TF-IDF version, as it produced a higher F1-score.

📊 Dataset

Dataset obtained from Kaggle: Wikipedia Movie Plots

Columns used: Movie name, Genre, and Plot

Cleaned using Python (removed missing values, duplicates, and non-English entries).

Final balanced labels: Drama, Comedy, Horror, Action, Thriller, Romance.

🛠 Tech Stack

Language: Python 3.11+

Libraries:

scikit-learn – TF-IDF, CountVectorizer, Logistic Regression, GridSearchCV

pandas, numpy – Data cleaning & analysis

matplotlib, seaborn – Visualization

streamlit – Web app deployment

pickle – Model persistence

🚀 Project Workflow

Data Cleaning – Removed duplicates, fixed missing values, limited to six core genres.

Exploratory Data Analysis (EDA) – Checked class imbalance, visualized top terms.

Feature Engineering –

TF-IDF Vectorizer (tfidf_vectorizer.pkl)

CountVectorizer for comparison

Model Training – Logistic Regression with hyperparameter tuning using GridSearchCV (class_weight='balanced').

Evaluation – Best F1-Score: 0.5198 (LogReg + CountVectorizer), slightly better with TF-IDF on unseen data.

Deployment Prep – Saved model (best_logreg_model.pkl) and mapping (label_encoder.pkl).

Streamlit App – Built interactive UI (app.py) to input plots and predict genres.

📈 Model Performance
Vectorizer	Classifier	Best F1-Score
CountVectorizer	Logistic Regression	0.5199
TF-IDF	Logistic Regression	~0.52

⚠ Predictions may be inaccurate for tricky or ambiguous plots.

🌟 App Features

Clean UI with Streamlit.

Enter any movie plot and instantly predict its genre.

Uses saved TF-IDF vectorizer and Logistic Regression model for fast inference.

Lightweight and deployable on Streamlit Cloud.

💻 How to Run Locally
1️⃣ Clone the Repository
git clone https://github.com/HARSHIT071004/Movie-Genre-Predictor-NLP-main.git
cd Movie-Genre-Predictor-NLP-main

2️⃣ Install Requirements
pip install -r requirements.txt

3️⃣ Run the App
streamlit run app.py


Then open the displayed URL (e.g., http://localhost:8501) in your browser.

🌐 Deployment

Deployed on Streamlit Cloud.

Repository: HARSHIT071004/Movie-Genre-Predictor-NLP-main

Branch: main

Main file path: Movie-Genre-Predictor-NLP-main/app.py

Ensure these files are in the same folder as app.py:

tfidf_vectorizer.pkl

best_logreg_model.pkl

label_encoder.pkl

🔮 Future Improvements

Add more genres and train with larger balanced data.

Use advanced models (e.g., SVM, BERT) for improved accuracy.

Display confidence scores for predictions.

Include visualizations (word clouds, top features) in the app.

Deploy the model as a web app or API for real-time genre prediction.

Author

Harshit Sharma – NLP & Machine Learning Developer
