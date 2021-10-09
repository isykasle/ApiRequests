# ApiRequests
A python app that requests data from the Movie database API and appends these data to a SQL database.

The project is developed in Python 3.7.11 version.

I prefer to develop Python projects in PyCharm and creating virtualenvs 
for every different project.
So open the directory of the project in PyCharm
or every else IDE that you prefer 
and create a new environment for the project.

The file requirements.txt includes every library 
with specific version that I added 
to the environment/project
to develop the application.

In order to install the requirements of project:

1.open cmd

2.Navigate to the directory of the project 
where Python 3.7.11 is installed also,
or open the virtualenv of the project.

3.run: 

pip install -r requirements.txt 

This is installing all the dependencies of the project.
 
DDL database schema:

The ddl database schema of moviedb database is the moviedb.sql file

To run the project: 

1.Load the ddl database schema in a Postgres database.
Create a database named moviedb. Copy and run the commands from the file moviedb.sql
Or load them in the database moviedb.


2.Run the Python application: 
  
  2.1 open cmd
  
  2.2 Navigate to the directory of the project 
  where Python 3.7.11 is installed also,
  or open the project in the IDE .
  
  2.3 run in cmd: python3 -m movie_db_app
      Or run from the GUI of IDE 
      the movie_db_app.py file. 
