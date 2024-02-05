# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 20:35:11 2024

@author: user
"""

import pandas

file = pandas.read_csv("movie_dataset.csv")

print(file)

print(file.info())

print(file.describe())


#removing redundant ranking column

import pandas as pd

df= pd.read_csv("movie_dataset.csv",index_col=0)


#removing the nan from the dataset

df.dropna(inplace= True)
df = df.reset_index(drop=True)


#Filtering for year 2015 to 2017

df2 = df.loc[(df['Year'] >= 2015) & (df['Year'] < 2018)] 
print(df2)
print(df2.describe())


#How many movies were released in the year 2016?

df3 = df.loc[(df['Year'] == 2016)]
print(df3)
df3.shape[0]


#determining rating of 8.0 and above
df4 = df.loc[(df['Rating'] >= 8.0)]
print(df4)
print(df4.info())

#Median for movies by Christopher Nolan
df5 = df.loc[(df['Director']) == 'Christoper Nolan']
print(df5)



year_average_score = df.loc[df['Title_Year'].isin(year2.index)].groupby('title_year')['Rating'].mean()

