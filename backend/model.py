import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Load dataset
data = pd.read_csv("dataset.csv")

# Train model
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(data["log"])
y = data["root_cause"]

model = LogisticRegression()
model.fit(X, y)

def predict_root_cause(log_text):
    vector = vectorizer.transform([log_text])
    prediction = model.predict(vector)[0]
    return prediction
