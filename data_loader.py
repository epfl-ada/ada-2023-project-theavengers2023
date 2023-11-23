import pandas as pd
import numpy as np
import os
import json
import re
import requests
import sys
import seaborn as sns
import matplotlib.pyplot as plt
## Define the paths to the datasets

#-----------------CMU dataset-----------------#

CMU_PATH = 'datasets/MovieSummaries/'
CHARACTER_DATASET = CMU_PATH+"character.metadata.tsv"
MOVIE_DATASET = CMU_PATH+"movie.metadata.tsv"

#-----------------Kaggle movie dataset-----------------#
KAGGLE_MOVIE_PATH = 'datasets/kaggle_movie/'
KAGGLE_MOVIE = KAGGLE_MOVIE_PATH+"movies_metadata.csv"
KAGGLE_RATING = KAGGLE_MOVIE_PATH+"ratings.csv"

#-----------------Kaggle IMDB dataset-----------------#
KAGGLE_IMDB_PATH = 'datasets/kaggle_imdb/'
KAGGLE_TITLE_IMDB = KAGGLE_IMDB_PATH+"/title.basics.tsv/data.tsv"
KAGGLE_RATING_IMDB = KAGGLE_IMDB_PATH+"/title.ratings.tsv/data.tsv"

#-----------------Consumer price index dataset-----------------#
PRICE_INDEX_PATH = 'datasets/consumer_price_index/'
CONSUMER_PRICE_INDEX = PRICE_INDEX_PATH+"consumer_price_index_2010.csv"
CONSUMER_PRICE_INDEX1 = PRICE_INDEX_PATH+"CPI.csv"








#load the datasets 

def load_cmu_movies():
    #load the dataset
    df_movie = pd.read_csv(MOVIE_DATASET,delimiter='\t')
    df_movie.columns = ['Wikipedia ID', 'Freebase ID', 'Name', 'Release date', 'Revenue', \
                        'Run Time', 'Language', 'Countries', 'Genres']
    
        #convert the 'Release date' column of movie dataset to YYYY-MM-DD format with 3 new columns : 'Year', 'Day'
    df_movie['Year'] = np.nan
    df_movie['Month'] = np.nan
    df_movie['Day'] = np.nan

    #extract Year, Month, and Day based on the string format
    for index, release_date in enumerate(df_movie['Release date']):
        #if date_str is NaN, Year, Month, and Day remain NaN
        if pd.notnull(release_date):
           date_parts = str(release_date).split('-')
           df_movie.at[index, 'Year'] = int(date_parts[0])
           #if only the year is available, Month and Day are left as NaN
           if len(date_parts) == 3:  # Full date is present
              df_movie.at[index, 'Month'] = int(date_parts[1])
              df_movie.at[index, 'Day'] = int(date_parts[2])
            
    #convert columns to nullable integer types
    df_movie['Year'] = df_movie['Year'].astype('Int64')
    df_movie['Month'] = df_movie['Month'].astype('Int64')
    df_movie['Day'] = df_movie['Day'].astype('Int64')


    return df_movie

def load_cmu_characters():
    #load the dataset
    df_character = pd.read_csv(CHARACTER_DATASET,delimiter='\t')
    df_character.columns = ['Wikipedia ID', 'Freebase ID', 'Release date', 'Character Name', 'Actor Birth', 'Actor Gender', \
                             'Actor Height', 'Ethnicity', 'Actor Name', 'Actor Age At Movie Release', \
                                'Freebase Actor/Character Map ID', 'Freebase Character ID', 'Freebase Actor ID']
    
    return df_character


def load_kaggle_movies():
    #load the dataset
    df_kaggle_movie = pd.read_csv(KAGGLE_MOVIE, sep=',', header=0, low_memory=False)
    df_kaggle_movie.rename(columns={'title': 'Name', 'revenue': 'Revenue', 'id': 'movieId', 'release_date': 'Release date', 'imdb_id': 'tconst'}, inplace=True)

        #convert the 'Release date' column of movie dataset to YYYY-MM-DD format with 3 new columns : 'Year', 'Day'
    df_kaggle_movie['Year'] = np.nan
    df_kaggle_movie['Month'] = np.nan
    df_kaggle_movie['Day'] = np.nan

    #extract Year, Month, and Day based on the string format
    for index, release_date in enumerate(df_kaggle_movie['Release date']):
        #if date_str is NaN, Year, Month, and Day remain NaN
        if pd.notnull(release_date):
           date_parts = str(release_date).split('-')
           df_kaggle_movie.at[index, 'Year'] = int(date_parts[0])
           #if only the year is available, Month and Day are left as NaN
           if len(date_parts) == 3:  # Full date is present
              df_kaggle_movie.at[index, 'Month'] = int(date_parts[1])
              df_kaggle_movie.at[index, 'Day'] = int(date_parts[2])
            
    #convert columns to nullable integer types
    df_kaggle_movie['Year'] = df_kaggle_movie['Year'].astype('Int64')
    df_kaggle_movie['Month'] = df_kaggle_movie['Month'].astype('Int64')
    df_kaggle_movie['Day'] = df_kaggle_movie['Day'].astype('Int64')

    return df_kaggle_movie


def load_movie_imdb_kaggle():
    df_movie_imdb = pd.read_csv(KAGGLE_TITLE_IMDB, sep='\t', header=0, low_memory=False)
    df_movie_imdb.rename(columns={'primaryTitle': 'Name'}, inplace=True)
    df_movie_imdb = df_movie_imdb[df_movie_imdb['titleType'] == 'movie']

    df_movie_imdb.rename(columns={'startYear': 'Year'}, inplace=True)
    df_movie_imdb['Year'] = pd.to_numeric(df_movie_imdb['Year'], errors='coerce').astype('Int64')


    df_movie_imdb.rename(columns={'runtimeMinutes': 'Runtime'}, inplace=True)
    df_movie_imdb['Runtime'] = pd.to_numeric(df_movie_imdb['Runtime'], errors='coerce').astype('float')

    return df_movie_imdb

def load_rating_imdb_kaggle():
    df_rating_imdb = pd.read_csv(KAGGLE_RATING_IMDB, sep='\t', header=0)

    return df_rating_imdb






###helper functions for preprocessing the data

def extract_features_names(row):
    #define the regular expression pattern
    pattern = r'"([A-Z][\w\s]*)"'
    
    #extract all matching country names
    matches = re.findall(pattern, row)
    
    return matches

def get_wikidata_id_translations():
    query = """
    SELECT ?item ?imdbID ?freebaseID WHERE {
      ?item wdt:P345 ?imdbID.
      OPTIONAL {?item wdt:P646 ?freebaseID.}
    }
  
    """

    url = 'https://query.wikidata.org/sparql'
    headers = {'User-Agent': 'WDQS-example Python/%s.%s' % (sys.version_info[0], sys.version_info[1])}
    data = requests.get(url, headers=headers, params={'query': query, 'format': 'json'}).json()
    
    imdb_id = []
    freebase_id = []
    for item in data['results']['bindings']:
        imdb_id.append(item['imdbID']['value'])
        freebase_id_val = item.get('freebaseID', {}).get('value', None)
        freebase_id.append(freebase_id_val)


    return pd.DataFrame(data={'tconst': imdb_id, 'Freebase ID': freebase_id})



#check for non-empty and non-NaN entries in a list
def is_nonempty_list(lst):
    return isinstance(lst, list) and len(lst) > 0 and not any(pd.isna(item) for item in lst)


#function that count the number of known actors
def count_known_actors(actor_list):
    #if the value is a list (and not NaN or None), return its length
    if isinstance(actor_list, list):
        return len(actor_list)
    #if the value is NaN or None, return 0
    else:
        return 0
    
def load_inflation():
    consumer_price_inflation = pd.read_csv(CONSUMER_PRICE_INDEX, sep = ',',skiprows=3)
    consumer_price_inflation = pd.read_csv(CONSUMER_PRICE_INDEX1, sep = ';')

    inflation_Dollar = consumer_price_inflation # Select US 
    #inflation_Dollar = inflation_Dollar.iloc[4:-1] # Select only the value : We have to multiply each revenu by 100 and divide by the appropriate rate
    #inflation_Dollar = inflation_Dollar.reset_index()
    pd_inflation_Dollar = pd.DataFrame(inflation_Dollar)
    pd_inflation_Dollar = pd_inflation_Dollar[['Year', 'CPI']]
    #pd_inflation_Dollar.rename(columns={'index': 'Year', 251 : 'CPI'}, inplace=True)
    #pd_inflation_Dollar['Year'] = pd_inflation_Dollar['Year'].astype(int)


    return pd_inflation_Dollar


def compute_categorical_variable(df, string_categorie ,number = 5):
 # Only show the number biggest movie producer 

    #compute the percentage of occurrences for each country
    df_percentages = df.value_counts(normalize=True) * 100

    #compute the top 5 categories
    top = df_percentages.nlargest(number).index

    # Filter the DataFrame to include only the top 5 countries
    df_top5 = df[df.isin(top)]


def transformCat(x):
    if (x>=0) and (x<10):
        return '00'+str(x)
    elif x<=30:
        return '0'+str(x)
    else:
        return ('30+')






