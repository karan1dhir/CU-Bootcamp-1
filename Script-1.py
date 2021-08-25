#Find the highest-grossing movie (i.e domestic earning + worldwide earning) in IMDB database year wise. 

import sqlite3
import pandas as pd
from matplotlib import pyplot as plt
db = sqlite3.connect('IMDB.sqlite')
heighest_movie_arr = []
dataFrame_earning = pd.read_sql_query('Select * from earning',db)
dataFrame_movies = pd.read_sql_query('Select * from IMDB',db)
all_movies_titles = dataFrame_movies['Title']
new_dataFrame_earning = dataFrame_earning['Domestic'] + dataFrame_earning['Worldwide']
dataFrame_movies['grossing'] = new_dataFrame_earning
def findYear(title):
    return int(title.split('(')[-1][:-1])
dataFrame_movies['Years'] = dataFrame_movies['Title'].apply(findYear)
unique_years = sorted(dataFrame_movies['Years'].unique())
for index in range(len(unique_years)):
    earning = max(dataFrame_movies[dataFrame_movies['Years'] == unique_years[index]]['grossing'])
    heighest_movie_arr.append(dataFrame_movies[dataFrame_movies['grossing'] == earning]['Title'].values[0]);
    #print(unique_years[index],dataFrame_movies[dataFrame_movies['grossing'] == earning]['Title'].values[0])
print(dataFrame_movies.describe())    
plt.bar(unique_years,heighest_movie_arr,width=0.6)
plt.show()
