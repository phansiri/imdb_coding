from django.shortcuts import render
from .models import Movie, Actor, Rating
from .forms import RatingForm
from django.shortcuts import render, get_object_or_404, redirect


def movie_list(request):
    movies = Movie.objects.all().order_by('name')
    return render(request, 'imdb_api/movie_list.html', {'movies': movies})


def movie_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    actors = Actor.objects.filter(movie_id=pk)
    ratings = Rating.objects.filter(movie_id_id=pk)
    return render(request, 'imdb_api/movie_detail.html',
                  {'movie': movie,
                   'actors': actors,
                   'ratings': ratings,
                   })

def rate_new(request, pk):
    if request.method == 'POST':
        form = RatingForm(request.POST)

        if form.is_valid():
            rateObj = Rating()
            rateObj.rate = int(request.POST['user_rate'])
            rateObj.comment = request.POST['user_comment']
            rateObj.movie_id_id = pk
            rateObj.save()
            return redirect('movie_detail', pk=pk)
        else:
            return render(request, 'imdb_api/rate_new.html', {
                'form': form,
                'error': ('There was a problem with your submission.',)
            })
    else:
        form = RatingForm()
        movie = get_object_or_404(Movie, pk=pk)
        return render(request, 'imdb_api/rate_new.html', {
            'form': form,
            'movie': movie,
        })
