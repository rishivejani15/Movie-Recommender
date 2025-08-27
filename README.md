# Task 2 - IMDB Movie Recommendation System

This project is a simple yet effective movie recommendation system built using a content-based filtering approach on the "IMDB Dataset of Top 1000 Movies and TV Shows". It features a web interface created with Streamlit where users can select a movie and get a list of similar movie recommendations.

## ✨ Features

- **Content-Based Filtering:** Recommends movies based on their inherent features (genre, director, cast, plot overview).
- **Interactive UI:** A user-friendly web interface built with Streamlit to easily get recommendations.
- **Customizable:** Users can select the number of recommendations they want to see.
- **Efficient:** Uses Streamlit's caching to load and process the data only once, ensuring fast responses.

## 🛠️ Approach and Methodology

The core of this project is a **Content-Based Filtering** algorithm. This method was chosen because the provided IMDB dataset is rich in metadata about the movies but lacks user-specific data (like ratings or watch history), which would be required for collaborative filtering.

The process is as follows:

1.  **Data Loading & Preprocessing:**
    - The `imdb_top_1000.csv` dataset is loaded using Pandas.
    - Missing values in crucial columns (`Genre`, `Director`, `Stars`, `Overview`) are filled with empty strings.
    - Text data for directors and stars is cleaned by removing spaces (e.g., "James Cameron" becomes "JamesCameron") to treat them as single, unique entities.

2.  **Feature Engineering (Creating a "Content Soup"):**
    - A new feature column named `tags` is created for each movie.
    - This `tags` column is a concatenation of the movie's `Genre`, `Director`, `Stars`, and `Overview`. This combined string serves as a comprehensive representation of the movie's content.

3.  **Vectorization:**
    - The textual `tags` are converted into numerical vectors using `TfidfVectorizer` from Scikit-learn. TF-IDF (Term Frequency-Inverse Document Frequency) is used to give more weight to words that are significant to a specific movie's content rather than common words that appear across all movies.

4.  **Similarity Calculation:**
    - The **Cosine Similarity** is calculated between the TF-IDF vectors of all movies. This results in a similarity matrix where each entry `(i, j)` represents the content similarity between movie `i` and movie `j`. A score closer to 1 indicates higher similarity.

5.  **Recommendation Generation:**
    - When a user selects a movie, the system finds its corresponding row in the similarity matrix.
    - It then retrieves the movies with the highest similarity scores, sorts them, and returns the top N recommendations (excluding the input movie itself).

## 🔧 Tools and Libraries Used

- **Python:** The core programming language.
- **Pandas:** For data manipulation and preprocessing.
- **Scikit-learn:** For implementing the TF-IDF vectorizer and calculating cosine similarity.
- **Streamlit:** For building and serving the interactive web application.

## ⚙️ Setup and Installation

Follow these steps to set up and run the project locally.

**1. Clone the repository:**
```bash
git clone [https://github.com/rishivejani15/csi-task-aiml.git](https://github.com/rishivejani15/csi-task-aiml.git)
cd csi-task-aiml
