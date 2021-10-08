import dbMethods as dbm
import theMoviedbAPI as my_api

#load data from the db api
movie_ids, titles, original_titles, descriptions = my_api.get_movie_details()
directors_ids, directors_names = my_api.get_director_details(movie_ids)
imdb_links = my_api.build_director_imdb_link(directors_ids)


#insert data to the moviedb database
for i in range(len(movie_ids)):
    dbm.insert_into_director_table(directors_ids[i], directors_names[i], imdb_links[i])
    dbm.insert_into_movie_table(movie_ids[i], titles[i], descriptions[i], original_titles[i])
    dbm.insert_into_movie_director_table(movie_ids[i], directors_ids[i])
