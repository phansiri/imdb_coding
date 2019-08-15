from django.db import models

# Relational Database Tables in the form of ORM
class Movie(models.Model):
    movie_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return '{}: {}'.format(self.movie_id, self.name)

class Actor(models.Model):
    actor_id = models.AutoField(primary_key=True)
    movie_id = models.ManyToManyField(Movie)
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)

    def __str__(self):
        return '{} {}'.format(self.fname, self.lname)

class Rating(models.Model):
    rating_id = models.AutoField(primary_key=True)
    movie_id = models.ManyToManyField(Movie)
    rate = models.IntegerField()
    comment = models.TextField()

    def __str__(self):
        return self.rate
