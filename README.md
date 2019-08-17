#Coding Challange
This project was to deliver a minial viable product that meets the intent of the prompt below.

##Prompt
Write the backend for a web application that searches a movies and actors in IMDB. Your application should:
1. Define a database schema that supports movie names, actors in those movies, and user reviews for movies
2. Explain the rationale for your schema in code comments.
3. You can pull data from IMDB Interfaces into your database.

Build a web API that allows any user to:
1. Search for names of movies an actor has appeared in
2. Search for names of actors in a given movie
3. Rate a movie on a 1-5 scale, with a comment
4. Search movies with a rating above a set value, and return both the movie name and the actors in it
5. You must have tests for your application, although there is no specific coverage requirement.

##Built with
* [Django](https://www.djangoproject.com) - Python Web Framework version 2.2.4
* [PostgreSQL](https://www.postgresql.org) - Relational Database version 10.10 for Windows 10 64-bit

##Overview of development process
###High level checklist
1. Create Database
2. Generate Django web framework
    - [x] connect with db
    - [x] serve up data on the web page
    - [ ] allow any user to add rating
    - [ ] create api endpoints through Django REST framework
    - [ ] create user interaction with api
    
###Detailed thought process
1. First step after reading the prompt was to create a database that can hold information necessary for the prompt.
2. Movie, actor, and rating is what I gathered to create the main tables from.
3. Movie table has (2) attributes of movie_id (primary key) and name
4. Actor table has (3) attributes of actor_id (primary key), fname, and lname.
5. Rating table has (4) attributes of rating_id (primary key), movie_id (foreign key), rate, and comment.
6. Created joining table for Movie and Actor tables because they have a many to many relationship. One movie can have multiple actors and one actor can star in multiple movies.
7. The Movie and Rating table has a one to many relationship because one movie can have multiple ratings while one rating can only be for one movie.
8. Once the database was created through localhost, it was time to create the Django project and app.
9. Once I go the web app running, I tested the connection through psycopg2 to ensure the database was set up correctly.
10. Once the connection was established, I created the models (database tables) through Django's language. Below is an Entity Relational Diagram.
****Add ERD picture
11. I added some test data that will test functionality of the prompts. (api will come later)
12. created movie list to showcase movie
13. created movie detail that will show actors and its ratings
14. inside movie detail, give the ability to input a rating scale 1-5, add comment, and submit it to the database
 