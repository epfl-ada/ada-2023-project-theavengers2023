import pandas as pd
import numpy as np
import os
import json
import re
import requests
import sys

#load the datasets 

def load_cmu_movies():
    #load the dataset
    df_movie = pd.read_csv("../MovieSummaries/movie.metadata.tsv",delimiter='\t')
    df_movie.columns = ['Wikipedia ID', 'Freebase ID', 'Name', 'Release Date', 'Revenue', \
                        'Run Time', 'Language', 'Countries', 'Genres']

    return df_movie

def load_cmu_characters():
    #load the dataset
    df_character = pd.read_csv("../MovieSummaries/character.metadata.tsv",delimiter='\t')
    df_character.columns = ['Wikipedia ID', 'Freebase ID', 'Release Date', 'Character Name', 'Actor Birth', 'Actor Gender', \
                             'Actor Height', 'Ethnicity', 'Actor Name', 'Actor Age At Movie Release', \
                                'Freebase Actor/Character Map ID', 'Freebase Character ID', 'Freebase Actor ID']
    
    return df_character


def load_kaggle_movies():
    #load the dataset
    df_kaggle_movie = pd.read_csv("../movies_metadata.csv", sep=',', header=0, low_memory=False)
    df_kaggle_movie.rename(columns={'title': 'Name', 'revenue': 'Revenue', 'id': 'movieId', 'release_date': 'Release date', 'imdb_id': 'tconst'}, inplace=True)

    return df_kaggle_movie


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






