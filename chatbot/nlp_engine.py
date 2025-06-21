import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

faq_df = pd.read_csv("data/faq_dataset.csv")
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(faq_df['question'])

def get_answer(query):
    """
    Return the most similar answer from FAQ dataset using TF-IDF similarity.
    """
    q_vec = vectorizer.transform([query])
    sim = cosine_similarity(q_vec, X)
    idx = sim.argmax()
    return faq_df.iloc[idx]['answer']
