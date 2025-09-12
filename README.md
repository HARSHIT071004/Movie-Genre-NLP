Movie Genre Predictor – NLP Project
Project Overview

The Movie Genre Predictor is an NLP-based machine learning project that predicts the genre of a movie based on its plot summary. The system uses natural language processing techniques for text preprocessing and feature extraction, followed by classification models to predict genres.

Key Features

Text Preprocessing:

Tokenization

Stopword removal

Lemmatization or stemming

Feature Extraction:

Bag-of-Words (BoW)

TF-IDF vectorization

Modeling:

Logistic Regression for multi-class classification

Random Forest Classifier for improved performance

Hyperparameter tuning using GridSearchCV

Evaluation Metrics:

Accuracy

Precision, Recall, F1-score

Confusion Matrix

Dataset

The dataset consists of movie plot summaries along with their corresponding genres. Preprocessing includes:

Cleaning text data

Handling missing values

Encoding genres as labels

Tech Stack

Python 3.x

pandas, numpy

scikit-learn

NLTK / spaCy for NLP preprocessing

matplotlib, seaborn for visualization

How to Use

Load the dataset and clean text data.

Perform text preprocessing (tokenization, stopword removal, lemmatization).

Convert text into numerical features using BoW or TF-IDF.

Split data into training and testing sets.

Train classification models (Logistic Regression, Random Forest).

Evaluate model performance using accuracy and classification metrics.

Use the trained model to predict genres for new movie plots.

Results

Logistic Regression and Random Forest models achieved strong classification performance after preprocessing and tuning.

Random Forest generally performed better due to its ensemble nature and ability to handle complex patterns in text data.

Future Work

Experiment with deep learning models (LSTM, BERT) for better text understanding.

Handle multi-label classification if movies have multiple genres.

Deploy the model as a web app or API for real-time genre prediction.

Author

Harshit Sharma – NLP & Machine Learning Developer
