import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pickle

df = pd.read_csv("/Users/test/Downloads/ex.csv")

df['Singer/Artists'] = df['Singer/Artists'].fillna('')
df['Genre'] = df['Genre'].fillna('')
df['Album/Movie'] = df['Album/Movie'].fillna('')

df['tags'] = (
    df['Singer/Artists'] + " " +
    df['Genre'] + " " +
    df['Album/Movie']
)

df['tags'] = df['tags'].astype(str).str.lower()

new_df = df[['Song-Name', 'tags']].copy()
new_df.rename(columns={'Song-Name': 'title'}, inplace=True)

cv = CountVectorizer(max_features=2000, stop_words='english')
vectors = cv.fit_transform(new_df['tags']).toarray()

similarity = cosine_similarity(vectors)

pickle.dump(new_df, open('musicrec.pkl','wb'))
pickle.dump(similarity, open('similarities.pkl','wb'))

print("Pickle files created successfully")