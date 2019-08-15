from django.shortcuts import render
from .models import Movie, Actor, Rating

def movie_list(request):
    movies = Movie.objects.all().order_by('name')
    return render(request, 'imdb_api/movie_list.html', {'movies':movies})
