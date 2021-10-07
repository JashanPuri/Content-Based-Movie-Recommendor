import streamlit as st
import pandas as pd
import pickle

movie_sim_matrix = pickle.load(open("movie_sim_matrix.pkl", 'rb'))
movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

def recommend_movies(title, count=5):
    movie_index = movies[movies['title'] == title].index[0]
    similarities = movie_sim_matrix[movie_index]
    sorted_similarities = sorted(list(enumerate(similarities)),reverse=True, key=lambda x: x[1])[1:count+1]
    recommended = []

    for i in sorted_similarities:
        recommended.append(movies.iloc[i[0]]['title'])

    return recommended

st.title("Movie Recommendation System")

selected_movie = st.selectbox('Select a movie', movies['title'].values)

if st.button("Recommend"):
    recommended = recommend_movies(selected_movie)
    
    for i in recommended:
        st.write(i)