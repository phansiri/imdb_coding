# Coding Challange
This project was to deliver a minial viable product that meets the intent of the prompt below.

## Prompt
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

## Built with
* [Django](https://www.djangoproject.com) - Python Web Framework version 2.2.4
* [Django REST framework](https://www.django-rest-framework.org/) - Powerful and flexible toolkit for building web apis version 3.10.2
* [PostgreSQL](https://www.postgresql.org) - Relational Database version 10.10 for Windows 10 64-bit

## Technology utilized
* Postman to test api functionality
* Pycharm IDE

## Overview of development process
### High level checklist
1. Create Database
2. Establish github repo
3. Generate Django web framework
    - [x] connect with db
    - [x] serve up data on the web page
    - [x] allow any user to add rating
    - [x] create api endpoints through Django REST framework
    - [x] create user interaction with api
    - [x] clean up code
    
### Detailed thought process
1. First step after reading the prompt was to create a database that can hold information necessary for the prompt.
2. Movie, actor, and rating is what I gathered to create the main tables from.
    * Utilizing Django makes generating a database easy in order to allow the developer to focus on the functionality of what is important. However, below is a drawn ERD.
3. Movie table has (2) attributes of id (primary key) and name.
4. Actor table has (3) attributes of id (primary key), fname, and lname.
5. Rating table has (4) attributes of id (primary key), movie_id (foreign key), rate, and comment.
6. Created joining table for Movie and Actor tables because they have a many to many relationship. One movie can have multiple actors and one actor can star in multiple movies.
7. The Movie and Rating table has a one to many relationship because one movie can have multiple ratings while one rating can only be for one movie.
8. Once the database was created through localhost, it was time to create the Django project and app.
9. Once I go the web app running, I tested the connection through psycopg2 to ensure the database was set up correctly and other admin settings.
10. Once the connection was established, I created the models (database tables) through Django's language. Below is an Entity Relational Diagram.
* This was the time I submitted my initial git push to the repo. My thought process on the workflow is as follows: The master branch should not have any commits, develop branch will be the main and staging branch where all other branches stem out from. Each branch that come out of develop will tackle a single feature because getting pushed to the repo. Once there is a pull request, I ensure it is handled from that branch to the develop branch. After a good amount of functionality is completed, then develop branch will merge with master.
* If you want to verify see [https://github.com/phansiri/imdb_coding/network](https://github.com/phansiri/imdb_coding/network)
* Models are broken down to at least 3rd Normal form so that one piece of information is in one cell.
![Entity Relationship Diagram](/screenshots/imdb_db_erd.PNG)
11. I added some test data that will test functionality of the prompts.
12. created movie list to showcase movie through non-api in order to see the behavior on the frontend through the views.py code.
13. created movie detail that will show actors and its ratings same as above
14. inside movie detail, give the ability to input a rating scale 1-5, add comment, and submit it to the database same as above
15. Once I got it all working, I started on the API section
16. Django utilizes the Django REST framework which makes creating api easier
17. I started out with creating a serializer, updating my urls, and then the views. These three py files were heavily edited.
18. All the tests are mainly in the test.py file
 
 
### Answering prompt questions
Number 1. The endpoint is [/api/v1/movie/]. To interact with it, pass in [?q=name of movie] at the end of the url and the results of how star in them with return.

For example /api/v1/movie?q=terminator and json object that returns will be the actors (as a bonus, I added other movies that they also star in)
![IMDB api movie list](/screenshots/imdb_api_movie_list.PNG)
![IMDB api movie list search result](/screenshots/imdb_api_movie_list-search-result.PNG)

Number 2. The endpoint is [/api/v1/actor/]. To interact with it, pass in [?q=Schwarzenegger] at the end of the url and the results of how many movies that actor as stared in.

For example /api/v1/actor?q=schwarzenegger and a json object will have a list of movies in it
![IMDB api actor list](/screenshots/imdb_api_actor_list.PNG)
![IMDB api actor list search result](/screenshots/imdb_api_actor_list-search-result.PNG)

Number 3. The endpoint is [/api/v1/rate/]. To interact with it, pass in [?rate=int&comment=string&movie_id=int]

For example /api/v1/rate/?rate=5&comment=hi&movie_id=3 and the csrf token is needed in order to be able to post
In the serializers.py, I set the rate variable with a min of 1 and max of 5. All fields are required too.
However, below is the interactive way Django lets the user add their own. 

![IMDB api rate list top](/screenshots/imdb_api_rate_list_top.PNG)
![IMDB api rate list bottom](/screenshots/imdb_api_rate_list_bottom.PNG)

#### Handling validation for rate on the backend
![IMDB api rate list create rate 6 bad request](/screenshots/imdb_rate_list_create_rate_6_bad_request.PNG)
![IMDB api rate list create rate -1 bad request](/screenshots/imdb_rate_list_create_rate_-1_bad_request.PNG)
![IMDB api rate list create rate successful created](/screenshots/imdb_rate_list_create_rate_created.PNG)

Number 4. The endpoint is [/api/v1/rate/int:rating](). To interact with it, change the int:rating to a number within 1 to 5 and the api will return a json list of all movies and actors that have a star rating greater than what was passed in at the end
![IMDB api rate list search result](/screenshots/imdb_api_rate_list_search_result.PNG)

### Swagger API view
![IMDB Swagger API view](/screenshots/imdb-swagger-api-view.PNG)