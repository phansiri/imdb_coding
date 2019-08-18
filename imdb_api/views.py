from django.shortcuts import render
from .models import Movie, Actor, Rating
from .forms import RatingForm
from django.shortcuts import render, get_object_or_404, redirect

from rest_framework import viewsets
from .serializers import MovieSerializer, ActorSerializer, RatingSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import generics, mixins
from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from django_filters import FilterSet
from django_filters import rest_framework as filters

# API VIEWS

# good
@api_view(['GET'])
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

# good
@api_view(['GET'])
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


# POST is not complete
# @api_view(['GET','POST', 'DELETE'])
# def api_rates_detail(request, pk, format=None):
#     try:
#         queryset = Rating.objects.filter(movie_id=pk)
#     except Rating.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#     if request.method == 'GET':
#         serializer = RatingSerializer(queryset, many=True, context={'request': request})
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = RatingSerializer(queryset, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'DELETE':
#         queryset.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

class RateListCreateView(generics.ListCreateAPIView):
    serializer_class = RatingSerializer
    def get_queryset(self):
        queryset = Rating.objects.all()
        movie_id = self.request.query_params.get('movie_id', None)
        if movie_id is not None:
            queryset = queryset.filter(movie_id=movie_id)
        return queryset

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save()


# @api_view(['GET'])
# def api_rating_list(request, format=None):
#     try:
#         queryset = Rating.objects.all()
#     except Rating.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#     if request.method == 'GET':
#         serializer = RatingSerializer(queryset, many=True, context={'request': request})
#         return Response(serializer.data)

# functionality is slightly off
@api_view(['GET'])
def api_rating_list_search(request, pk, format=None):
    try:
        queryset = Rating.objects.filter(rate__gte=pk)
    except Rating.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        entries = Actor.objects.filter(Q(movie_id__actor__movie_id__in=queryset.values('movie_id_id'))).distinct()
        serializer = ActorSerializer(entries, many=True, context={'request': request})
        return Response(serializer.data)

class RateSearch(generics.ListAPIView):
    serializer_class = RatingSerializer

    def get_queryset(self):
        movie_id = self.request.query_params.get('movie_id', None)




# working on search function
def movie_list(request):
    query = request.GET.get("q_m")
    if query:
        q_list = Actor.objects.filter(movie_id__name__icontains=query)
        print('@@@@@@@@@@@@@@@@@@@@@@@',q_list)

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
