import streamlit as st
import pickle
import pandas as pd

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distance = similarity[movie_index]
    movie_list = sorted(list(enumerate(distance)),reverse=True,key=lambda x: x[1])[1:6]
    recommended = []
    for i in movie_list:
        recommended.append(movies.iloc[i[0]].title)
    return recommended



movies = pd.read_pickle('movies.pkl', compression='infer')
similarity = pickle.load(open('similarity.pkl','rb'))


st.title('Movie Recommendation System')

select_movie_name =st.selectbox(
    "Movie List",
    movies['title'].values
)

if st.button('Recommend'):
    recommendations = recommend(select_movie_name)
    for i in recommendations:
        st.write(i)