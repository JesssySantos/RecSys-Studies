from typing import List
import pandas as pd
import numpy as np

def get_movies_genres(df_movies:pd.DataFrame) -> List:
    list_all = df_movies['genres'].str.split('|').dropna().to_numpy()
    listGenres = np.unique(sum(list_all, []))
    return listGenres
