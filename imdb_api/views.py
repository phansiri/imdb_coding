from .models import Movie, Actor, Rating
from .forms import RatingForm
from django.shortcuts import render, get_object_or_404, redirect
from .serializers import MovieSerializer, ActorSerializer, RatingSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from django.db.models import Q

# API VIEWS
# Two ways of how I approach handling APIs.
# 1) @api_view decorator for functions - this gives me flexibility on what HTTP I need to use.
# GET is default so there was no need to pass in any parameters such as ['POST']
# 2) Generic API classes - it inherits what I need without me breaking Don't Repeat Yourself (DRY)...
# unless I have to override the method


# function that gets a returned response of serialized data
# Can also pass in a url search of ?q=movie to return a filtered list of
# actors that stared in that searched movie
@api_view()
def api_movie_list(request):
    if request.method == 'GET':
        queryset = Movie.objects.all()
        serializer = MovieSerializer(queryset, many=True, context={'request': request})
        qs = request.GET.get('q')
        if qs is not None:
            queryset = queryset.filter(
                Q(name__icontains=qs)
            ).distinct()
            new_search = Actor.objects.filter(movie_id=queryset[0].pk)
            serializer = ActorSerializer(new_search, many=True)
        return Response(serializer.data)

# function that gets a returned response of serialized data
# Can also pass in a url search of ?q=arnold to return a filtered list of
# movies that stared in that searched actor first or last name
# Q advanced search is used to ensure the 'OR' of the select statement will be recognized
@api_view()
def api_actor_list(request):
    if request.method == 'GET':
        queryset = Actor.objects.all()
        serializer = ActorSerializer(queryset, many=True, context={'request': request})
        qs = request.GET.get('q')
        if qs is not None:
            queryset = queryset.filter(
                Q(fname__icontains=qs) |
                Q(lname__icontains=qs)
            ).distinct()
            new_search = Movie.objects.filter(actor__id=queryset[0].pk)
            print('new_search prior to serializer: {}'.format(new_search))
            serializer = MovieSerializer(new_search, many=True, context={'request': request})
        return Response(serializer.data)

# RateListCreateView takes in a param of generics.ListCreateAPIView
# It extends from GenericAPIView but adds the ability to GET and POST
class RateListCreateView(generics.ListCreateAPIView):
    serializer_class = RatingSerializer

    # override default behavior of get_queryset
    # filters rating objects with passed in param as movie_id and
    # returns queryset
    def get_queryset(self):
        queryset = Rating.objects.all()
        movie_id = self.request.query_params.get('movie_id', None)
        if movie_id is not None:
            queryset = queryset.filter(movie_id=movie_id)
        return queryset

# function that gets a returned response of serialized data
# passes in request and pk (rating). The queryset holds data from the Rating object
# that is filtered with only rate is greater to or equal the pk.
# from there Q advance search will filter the Actor object to grab actors in movie id
# the distinct method is to ensure no duplicates are in the result. The returned data
# has movie and actor information
@api_view()
def api_rating_list_search(request, pk, format=None):
    try:
        queryset = Rating.objects.filter(rate__gte=pk)
    except Rating.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        entries = Actor.objects.filter(Q(movie_id__actor__movie_id__in=queryset.values('movie_id_id'))).distinct()
        serializer = ActorSerializer(entries, many=True, context={'request': request})
        return Response(serializer.data)


# ###################################################################################

# This is the frontend view. Since this is not part of the coding challenge, read at your own pace.

# working on search function
# function that returns a list of all movies and sends the object to the movie_list.html
def movie_list(request):
    query = request.GET.get("q_m")
    if query:
        q_list = Actor.objects.filter(movie_id__name__icontains=query)
    movies = Movie.objects.all().order_by('name')
    return render(request, 'imdb_api/movie_list.html', {'movies': movies})

# detailed view of a single movie. the param passed is the primary key of the movie
# from the pk, the movie, actors, and ratings can be gathered and sent to the movie_detail.html
def movie_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    actors = Actor.objects.filter(movie_id=pk)
    ratings = Rating.objects.filter(movie_id_id=pk)
    return render(request, 'imdb_api/movie_detail.html',
                  {'movie': movie,
                   'actors': actors,
                   'ratings': ratings,
                   })

# function that handles how to will save a new rate. It utilizes the RatingForm
# in forms.py to capture all attributes in that class. if the form is valid, a
# new rate form is created and saved to the database.
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
