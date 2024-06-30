import streamlit as st
import pandas as pd
import pickle
import gzip
import requests

# Load the preprocessed data for popularity-based recommendation
with open('popularity_model.pkl', 'rb') as f_popularity:
    movie_scored_df = pickle.load(f_popularity)

# Load the compressed preprocessed data for content-based recommendation
with gzip.open('content_model.pkl.gz', 'rb') as f_content:
    tagged_movie = pickle.load(f_content)


# Function to fetch movie poster
def fetch_poster(id):
    url = f"https://api.themoviedb.org/3/movie/{id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"

    try:
        data = requests.get(url)
        data.raise_for_status()  # Raise an error for bad responses (4xx or 5xx)
        data = data.json()
        poster_path = data['poster_path']
        full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
        return full_path
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching movie information: {e}")
        return None

# Function to recommend similar movies based on the selected movie
def recommend(movie):
    index = tagged_movie[tagged_movie['title'] == movie].index[0]
    distances = sorted(list(enumerate(tagged_movie['similarity'][index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:6]:
        # fetch the movie poster
        movie_id = tagged_movie.iloc[i[0]]['id']
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(tagged_movie.iloc[i[0]]['title'])

    return recommended_movie_names, recommended_movie_posters

# Streamlit app
st.title('Movie Recommender System')

# Add sub-header buttons for different recommendation systems
recommendation_system = st.sidebar.radio("Select Recommendation System", ["Popularity Based", "Content Based"])

if recommendation_system == "Popularity Based":
    st.header('Popularity Based Movie Recommendation System')

    # Check if 'genres' is a list and explode it to individual rows
    if isinstance(movie_scored_df['genres'].iloc[0], list):
        movie_scored_df = movie_scored_df.explode('genres')

    # Create a dropdown for genres
    selected_genre = st.selectbox('Select Genre', movie_scored_df['genres'].unique())

    # Filter movies based on the specified genre
    df = movie_scored_df[movie_scored_df['genres'] == selected_genre]

    # Select specific columns from the DataFrame
    selected_columns = ['title','score', 'id']
    df = df[selected_columns]

    # Sort movies based on the 'score' column in descending order
    df = df.sort_values('score', ascending=False).head(250)

    # Display recommended movies with title, poster, and score
    for index, row in df.iterrows():
        st.write(f"### {row['title']}")
        st.image(fetch_poster(row['id']), caption=f"Score: {row['score']:.2f}", use_column_width=True)

elif recommendation_system == "Content Based":
    st.header('Content Based Movie Recommendation System')

   # Save the updated DataFrame to the pickle file
    with gzip.open('content_model.pkl.gz', 'wb') as f_content:
            pickle.dump(tagged_movie, f_content)

    # Create a dropdown for movie selection
    selected_movie = st.selectbox('Select Movie', tagged_movie['title'].values)

    # Recommend similar movies based on the selected movie
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])

    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])
