import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib

# Load datasets
true = pd.read_csv("True.csv")
fake = pd.read_csv("Fake.csv")

# Add labels
fake["label"] = 0
true["label"] = 1


data = pd.concat([fake, true], ignore_index=True)


data = data.dropna()

# Features and labels
X = data["title"]
y = data["label"]

# Convert text to numbers
vectorizer = TfidfVectorizer(stop_words="english", max_features=5000)
X = vectorizer.fit_transform(X)

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = LogisticRegression()
model.fit(X_train, y_train)

# Save model and vectorizer
joblib.dump(model, "model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")

print("Model trained successfully!")