import streamlit as st
import pandas as pd
from recommender import load_and_prepare_data, get_recommendations

st.set_page_config(
    page_title="Movie Recommendation System",
    page_icon="🎬",
    layout="wide"
)

st.title("🎬 IMDB Movie Recommendation System")
st.markdown("""
This app recommends movies based on content similarity. Select a movie you like from the dropdown
list below, and the system will suggest similar movies for you to watch next!
""")

DATA_PATH = 'data/imdb_top_1000.csv'
try:
    df, similarity_matrix = load_and_prepare_data(DATA_PATH)
    movie_titles = df['Series_Title'].sort_values().tolist()
except FileNotFoundError:
    st.error(f"Error: The data file was not found at '{DATA_PATH}'.")
    st.error("Please download the 'imdb_top_1000.csv' file from Kaggle and place it in the 'data/' directory.")
    st.stop()

st.sidebar.header("Get Your Recommendations")
selected_movie = st.sidebar.selectbox(
    "Select a movie you like:",
    options=movie_titles
)

num_recs = st.sidebar.slider(
    "Number of recommendations:",
    min_value=5,
    max_value=20,
    value=10,
    step=1
)

if st.sidebar.button("Recommend", type="primary"):
    if selected_movie:
        st.subheader(f"Because you liked '{selected_movie}', you might also like:")
        
        recommendations = get_recommendations(selected_movie, df, similarity_matrix, num_recs)
        
        if not recommendations.empty:
            cols = st.columns(5)
            
            for i, row in enumerate(recommendations.itertuples()):
                with cols[i % 5]:
                    st.markdown(f"**{row.Series_Title}** ({row.Released_Year})")
                    st.info(f"**Genre:** {row.Genre}")
                    st.warning(f"**IMDB Rating:** {row.IMDB_Rating} ⭐")
                    st.markdown("---")
        else:
            st.warning("Could not find recommendations for this movie.")
else:
    st.info("Select a movie and click 'Recommend' to get started.")