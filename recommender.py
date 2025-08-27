import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import streamlit as st

@st.cache_data
def load_and_prepare_data(data_path):
    """
    Loads the dataset, preprocesses it, and computes the similarity matrix.
    
    Args:
        data_path (str): The path to the CSV file.
        
    Returns:
        tuple: A tuple containing the preprocessed DataFrame and the cosine similarity matrix.
    """
    df = pd.read_csv(data_path)

    feature_cols = ['Genre', 'Director', 'Star1', 'Star2', 'Star3', 'Star4', 'Overview']
    for col in feature_cols:
        df[col] = df[col].fillna('')

    def clean_text(text):
        if isinstance(text, str):
            return text.replace(' ', '').replace(',', ' ')
        return ''

    df['Director'] = df['Director'].apply(clean_text)
    df['Star1'] = df['Star1'].apply(clean_text)
    df['Star2'] = df['Star2'].apply(clean_text)
    df['Star3'] = df['Star3'].apply(clean_text)
    df['Star4'] = df['Star4'].apply(clean_text)
    df['Genre'] = df['Genre'].apply(lambda x: x.replace(',', ' '))

    df['tags'] = (df['Genre'] + ' ' + 
                  df['Director'] + ' ' + 
                  df['Star1'] + ' ' + 
                  df['Star2'] + ' ' + 
                  df['Star3'] + ' ' + 
                  df['Star4'] + ' ' + 
                  df['Overview'].apply(lambda x: x.lower()))

    tfidf = TfidfVectorizer(max_features=5000, stop_words='english')
    vectors = tfidf.fit_transform(df['tags']).toarray()

    similarity_matrix = cosine_similarity(vectors)
    
    return df, similarity_matrix

def get_recommendations(movie_title, df, similarity_matrix, num_recommendations=10):
    """
    Recommends movies based on a given movie title.
    
    Args:
        movie_title (str): The title of the movie to get recommendations for.
        df (pd.DataFrame): The preprocessed DataFrame of movies.
        similarity_matrix (np.ndarray): The cosine similarity matrix.
        num_recommendations (int): The number of recommendations to return.
        
    Returns:
        pd.DataFrame: A DataFrame containing the recommended movies.
    """
    try:
        movie_index = df[df['Series_Title'] == movie_title].index[0]
    except IndexError:
        return pd.DataFrame()

    similarity_scores = list(enumerate(similarity_matrix[movie_index]))

    sorted_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)

    top_movies_indices = [i[0] for i in sorted_scores[1:num_recommendations + 1]]

    recommended_movies = df.iloc[top_movies_indices][['Series_Title', 'Released_Year', 'Genre', 'IMDB_Rating']]
    
    return recommended_movies