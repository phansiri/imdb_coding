from django.shortcuts import render
from .models import Movie, Actor, Rating
from django.shortcuts import render, get_object_or_404

def movie_list(request):
    movies = Movie.objects.all().order_by('name')
    return render(request, 'imdb_api/movie_list.html', {'movies':movies})

def movie_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    actors = Actor.objects.filter(movie_id=pk)
    return render(request, 'imdb_api/movie_detail.html',
                  {'movie': movie,
                   'actors': actors,
                   })