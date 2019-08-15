from django.shortcuts import render

def movie_list(request):
    return render(request, 'imdb_api/movie_list.html', {})
