import requests
import json
import os
from dotenv import load_dotenv
from ratelimit import limits, sleep_and_retry

load_dotenv()
FIVE_MINUTES = 300



"""
 * The method queries the movies which play from 2021-09-02 to 2021-09-15 
 * in theaters of Greece and returns the details of the movies that are queried
 @return: list ids: a list of integers of ids of movies
 @return: list title: a list of strings of titles of movies
 @return: list original_title: a list of strings of original titles of movies
 @return: list description: a list of strings of descriptions of movies
 """

@sleep_and_retry
@limits(calls=30, period=FIVE_MINUTES)
def get_movie_details():

    query = 'https://api.themoviedb.org/3/discover/movie?api_key='+os.getenv('API_key')+'&region=GR' \
           '&release_date.gte=2021-10-01&' \
            '%release_date.lte=2021-10-15&with_release_type=2|3'

    response = requests.get(query)

    if response.status_code == 200:

            array = response.json()
            text = json.dumps(array)
            text = json.loads(text)


    else:
            print("error")
    dataset = text['results']
    title = {}
    original_title = {}
    description = {}
    id = {}

    for i in range(len(dataset)):
        id[i] = dataset[i]['id']
        title[i] = dataset[i]['title']
        original_title[i] = dataset[i]['original_title']
        description[i] = dataset[i]['overview']

    return id, title, original_title, description


"""
 * The method queries the directors of movies which play from 2021-09-02 to 2021-09-15 
 * in theaters of Greece and returns the details of the directors that are queried
 @return: list director_ids: a list of integers of ids of directors
 @return: list director_names: a list of strings of names of directors
 """

@sleep_and_retry
@limits(calls=30, period=FIVE_MINUTES)
def get_director_details(movie_ids):
    responses = {}
    movies = {}
    crew = {}
    directors_ids = {}
    directors_names = {}

    for d in range(len(movie_ids)):

        query2 = 'https://api.themoviedb.org/3/movie/'+str(movie_ids[d])+'/credits?api_key='+os.getenv('API_key')+'&language=en-US'
        responses[d] = requests.get(query2)
        if responses[d].status_code == 200:

            array = responses[d].json()
            text = json.dumps(array)
            movies[d] = json.loads(text)
            crew[d] = movies[d]['crew']

            for j in range(len(crew[d])):
                if crew[d][j]['job'] == 'Director':
                    directors_ids[d] = crew[d][j]['id']

                    directors_names[d] = crew[d][j]['name']

        else:
            print("error")

    return directors_ids, directors_names


"""
 * The method queries the imdb links of directors of movies which play from 2021-09-02 to 2021-09-15 
 * in theaters of Greece and returns the imdb links of the directors that are queried
 @return: list imdb_links: a list of strings of imdb links of directors

 """

@sleep_and_retry
@limits(calls=30, period=FIVE_MINUTES)
def build_director_imdb_link(director_id):

    imdb_ids = {}
    responses1 = {}
    person = {}
    imdb_links = {}

    for d in range(len(director_id)):
        query3 = 'https://api.themoviedb.org/3/person/'+str(director_id[d]) + \
               '/external_ids?api_key='+os.getenv('API_key')+'&language=en-US'
        responses1[d] = requests.get(query3)
        if responses1[d].status_code == 200:
            an_array = responses1[d].json()
            a_text = json.dumps(an_array)
            person[d] = json.loads(a_text)



            if(person[d]['imdb_id']!=None):
                imdb_ids[d] = person[d]['imdb_id']

                imdb_links[d] = 'https://www.imdb.com/name/'+imdb_ids[d]+'/'

            else:
                imdb_ids[d] = 'Not Found'

                imdb_links[d] = 'Not Found'

        else:
            print("error")
    return imdb_links


