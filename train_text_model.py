"""
Training script for text-based stress detection model
Uses the dreaddit-train.csv dataset with text posts
"""
import pandas as pd
import numpy as np
import pickle
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report

# Load the dataset
print("Loading dataset...")
df = pd.read_csv('dreaddit-train.csv', encoding='ISO-8859-1')

# Use text and label columns
print(f"Dataset shape: {df.shape}")
print(f"Label distribution:\n{df['label'].value_counts()}")

# Prepare data
X = df['text'].fillna('')  # Text data
y = df['label']  # Labels: 0 = No Stress, 1 = Stress

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

print(f"\nTraining samples: {len(X_train)}")
print(f"Test samples: {len(X_test)}")

# Vectorize text using TF-IDF
print("\nVectorizing text...")
vectorizer = TfidfVectorizer(
    max_features=5000,  # Use top 5000 features
    ngram_range=(1, 2),  # Use unigrams and bigrams
    stop_words='english',
    min_df=2,  # Word must appear in at least 2 documents
    max_df=0.95  # Ignore words that appear in more than 95% of documents
)

X_train_vect = vectorizer.fit_transform(X_train)
X_test_vect = vectorizer.transform(X_test)

print(f"Feature matrix shape: {X_train_vect.shape}")

# Train KNN model
print("\nTraining KNN model...")
knn = KNeighborsClassifier(n_neighbors=5, metric='cosine')
knn.fit(X_train_vect, y_train)

# Evaluate model
print("\nEvaluating model...")
y_pred = knn.predict(X_test_vect)
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.4f}")
print("\nClassification Report:")
print(classification_report(y_test, y_pred, target_names=['No Stress', 'Stress']))

# Save model and vectorizer
print("\nSaving model and vectorizer...")
with open('stresslevel_text_model.pkl', 'wb') as f:
    pickle.dump(knn, f)

with open('stresslevel_text_vectorizer.pkl', 'wb') as f:
    pickle.dump(vectorizer, f)

print("✅ Model saved as 'stresslevel_text_model.pkl'")
print("✅ Vectorizer saved as 'stresslevel_text_vectorizer.pkl'")
print("\nYou can now use these files in your Flask app!")
