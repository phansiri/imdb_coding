from django.contrib import admin
from .models import Movie, Actor, Rating

# Registered to quickly interactive way to add data to the models (database tables)
admin.site.register(Movie)
admin.site.register(Actor)
admin.site.register(Rating)