import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()


"""
* Sets the connection to the database 
* @return conn the connection to a database
"""


def open_con():

    conn = psycopg2.connect(host=os.getenv('dbhost'),
                            database=os.getenv('db'),
                            user=os.getenv('dbuser'),
                            password=os.getenv('dbpass'))

    return conn


"""
* Inserts new vars to the table movie of database moviedb
"""


def insert_into_movie_table(movie_id, title, description, original_title):

    sql = """INSERT INTO movie(movie_id,title,description,original_title)
                  VALUES(%s,%s,%s,%s);"""

    conn = None

    try:
        # connect to the moviedb database
        conn = open_con()
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(sql, (movie_id, title, description, original_title))
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


"""
* Inserts new vars to the table director of database moviedb
"""


def insert_into_director_table(director_id, name, imdb_link):

    sql = """INSERT INTO director(director_id,name,imdb_link)
                  VALUES(%s,%s,%s);"""

    conn = None

    try:
        # connect to the moviedb database
        conn = open_con()
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(sql, (director_id, name, imdb_link))
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


"""
* Inserts new vars to the table movie_director of database moviedb
"""


def insert_into_movie_director_table(movie_id, director_id):

    sql = """INSERT INTO movie_director(movie_id,director_id)
                  VALUES(%s,%s);"""

    conn = None

    try:
        # connect to the moviedb database
        conn = open_con()
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(sql, (movie_id, director_id))
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()









