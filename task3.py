import nltk
import numpy as np
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# 1. Sample Knowledge Base (Data for the Bot)
data = """
Hello! I am the Noida Expo AI Assistant. 
I can help you with project details, technical tasks, and developer info.
Aditya Tripathi is the lead developer of this 33-task portfolio.
The project covers Web, IoT, Java, ML, and Data Analytics.
The Noida Expo 2026 is a showcase of advanced technical skills.
"""

# 2. NLP Preprocessing
nltk.download('punkt', quiet=True)
sent_tokens = nltk.sent_tokenize(data) # Converts data to list of sentences

def LemNormalize(text):
    remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)
    return nltk.word_tokenize(text.lower().translate(remove_punct_dict))

# 3. Response Generation Logic
def response(user_response):
    robo_response = ''
    sent_tokens.append(user_response)
    
    # TF-IDF Vectorization
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    tfidf = TfidfVec.fit_transform(sent_tokens)
    
    # Calculating Similarity
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx = vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    
    if(req_tfidf == 0):
        robo_response = "I am sorry, I don't understand that."
    else:
        robo_response = sent_tokens[idx]
    
    sent_tokens.remove(user_response)
    return robo_response

# 4. Chat Interface
print("🤖 AI Bot: I am your NLP Assistant. Type 'bye' to exit.")
while True:
    user_input = input("👤 You: ").lower()
    if user_input != 'bye':
        if user_input in ['hi', 'hello', 'hey']:
            print("🤖 AI Bot: Hello Aditya! How can I help you today?")
        else:
            print(f"🤖 AI Bot: {response(user_input)}")
    else:
        print("🤖 AI Bot: Goodbye! Good luck with the Expo!")
        break
