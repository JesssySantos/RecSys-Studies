from utils.streamlit_utils import get_movies_genres
from itertools import cycle
import streamlit as st
import pandas as pd

DATA_FOLDER = "../ml-latest-small/"

# Loading Data
df_movies = pd.read_csv(DATA_FOLDER + "movies.csv")
df_posters = pd.read_csv(DATA_FOLDER + "movie-posters.csv")

# Page Title
st.set_page_config(page_title="Movie Lens Recommender", layout='wide')
st.title('Movies Recomender with Streamlit')

# Sidebar
genres = get_movies_genres(df_movies)
genre_choice = st.sidebar.selectbox('Select Genre', sorted(genres), index = 0)

# Image Grid
moviePosters = df_posters['posterURL'].to_list()[:20]
caption = df_movies['title'].to_list()[:20] 
cols = cycle(st.columns(4))

for idx, filteredImage in enumerate(moviePosters):
    next(cols).image(filteredImage, width=150, caption=caption[idx])
    