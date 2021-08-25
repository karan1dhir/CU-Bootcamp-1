#Find out the percentage of the budget for each genre in IMDB Movie Dataset?Plot the pie chart.
import sqlite3
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
db = sqlite3.connect('IMDB.sqlite')
dataFrame_movies = pd.read_sql_query('Select * from IMDB',db)
dataFrame_genre = pd.read_sql_query('Select * from genre',db)
all_unique_movies = dataFrame_movies['Movie_id'].value_counts().index
genre_array = []
for i in range(len(all_unique_movies)):
    single_genre = []
    single = dataFrame_genre[dataFrame_genre['Movie_id'] == all_unique_movies[i]]['genre'].values
    single_genre.append(all_unique_movies[i])
    for i in single:
        single_genre.append(i)
    genre_array.append(single_genre)    

new_genre = pd.DataFrame(genre_array,columns=['Movie_id','genre1','genre2','genre3'])
result = pd.merge(dataFrame_movies,new_genre,on='Movie_id')
result['Budget'].replace('',0,inplace=True)
genre_1_name = result.groupby('genre1')['Budget'].sum().index
genre_1_amount = result.groupby('genre1')['Budget'].sum().values
genre_2_name = result.groupby('genre2')['Budget'].sum().index
genre_2_amount = result.groupby('genre2')['Budget'].sum().values
genre_3_name = result.groupby('genre3')['Budget'].sum().index
genre_3_amount = result.groupby('genre3')['Budget'].sum().values

genre_name = {}
for index in range(len(genre_1_name)):
    genre_name[genre_1_name[index]] = genre_1_amount[index]

for index in range(len(genre_2_name)):
    if genre_2_name[index] in genre_name:
        genre_name[genre_2_name[index]] = genre_name.get(genre_2_name[index]) + genre_2_amount[index]
    else:
        genre_name[genre_2_name[index]] = genre_2_amount[index]

for index in range(len(genre_3_name)):
    if genre_3_name[index] in genre_name:
        genre_name[genre_3_name[index]] = genre_name.get(genre_3_name[index]) + genre_3_amount[index]
    else:
        genre_name[genre_3_name[index]] = genre_3_amount[index]

del genre_name['']
np_genre_names = np.array(list(genre_name.keys()))
np_genre_amount = np.array(list(genre_name.values()))

perAmount = np.true_divide(np_genre_amount,np_genre_amount.sum()) * 100

# for index in range(len(np_genre_names)):
#     print(np_genre_names[index],format(perAmount[index],'.2f'))

plt.pie(perAmount, labels = np_genre_names,autopct="%.2f%%");
plt.title("Percentage of the budget for each genre.")
plt.axis("equal")
plt.show()