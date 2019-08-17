from django.db import models

# Relational Database Tables in the form of classes. Django will understand
# and create the the table in the postgresql database that is in
# setting.py

# Prompt: Define a database schema that supports movie names, actors in
# those movies, and user reviews for movies.
# Prompt: Explain the rationale for your schema in code comments.

# Movie table that has a primary key of movie_id and one attribute
# called name with the type string and a max character length of 255
class Movie(models.Model):
    name = models.CharField(max_length=255)

    # __str__ method returns a string "movie_id: name"
    def __str__(self):
        return self.name

# Actor table has a primary key of actor_id, a many to many relationship with the Movie table
# because one movie can have many actors while one actor can star in many movies.
# The ManytoManyField method creates an additional join table where movie_id and actor_id
# are in a table that has its own id. To finish off, Actor table has two attributes,
# fname and lname representing only one actor
class Actor(models.Model):
    movie_id = models.ManyToManyField(Movie)
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)

    # __str__ method returns a string "fname lname"
    def __str__(self):
        return '{} {}'.format(self.fname, self.lname)

# Rating table has a primary key of rating_id, it has a one to many relationship
# with the Movie table because one movie can have many ratings while one rating
# can be for one movie. The ForeignKey method creates a strong relationship with Movie table.
# To finish off, Rating table has two attributes, rate and comment.


class Rating(models.Model):
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rate = models.IntegerField()
    comment = models.TextField()

    def __str__(self):
        return str(self.rate)
