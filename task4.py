# PROJECT: Spam Email Detection
# TASK 34: Predictive Modeling with Scikit-Learn
# DELIVERABLE: Machine Learning Pipeline for Text Classification

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# 1. Dataset (Sample Emails)
data = {
    'text': [
        'Free entry in 2 a weekly comp to win FA Cup final tickets 21st May 2005.',
        'Hi, how are you? Are we still meeting for lunch today?',
        'WINNER!! As a valued network customer you have been selected to receivea £900 prize reward!',
        'Can you please send me the report by EOD?',
        'URGENT! Your Mobile number has been awarded with a £2000 bonus prize.',
        'I will call you back in 5 minutes, busy right now.',
        'Get a free gift card now by clicking this link!',
        'Let me know when you are free to talk about the project.'
    ],
    'label': ['spam', 'ham', 'spam', 'ham', 'spam', 'ham', 'spam', 'ham']
}

df = pd.DataFrame(data)

# 2. Preprocessing & Feature Extraction
# Converting text into a matrix of token counts
cv = CountVectorizer(stop_words='english')
X = cv.fit_transform(df['text'])
y = df['label']

# 3. Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Model Training (Naive Bayes)
model = MultinomialNB()
model.fit(X_train, y_train)

# 5. Model Evaluation
y_pred = model.predict(X_test)
print(f"✅ Model Accuracy: {accuracy_score(y_test, y_pred) * 100}%")
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))

# 6. Live Prediction Test
def predict_mail(new_mail):
    test_cv = cv.transform([new_mail])
    return model.predict(test_cv)[0]

sample_mail = "Congratulations! You won a lottery, click here to claim."
print(f"\nEmail: {sample_mail}")
print(f"Result: {predict_mail(sample_mail).upper()}")
