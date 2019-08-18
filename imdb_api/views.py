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
def movie_list(request):
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
def actor_list(request):
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
            serializer = MovieSerializer(new_search, many=True, context={'request': request})
        return Response(serializer.data)

@api_view(['GET'])
def rates(request, pk, format=None):
    print(pk)
    if request.method == 'GET':
        queryset = Rating.objects.all()
        serializer = RatingSerializer(queryset, many=True)
        return Response(serializer)


# class MovieList(generics.ListAPIView):
#     lookup_field = 'pk'
#     serializer_class = MovieSerializer
    # filter_backends = (DjangoFilterBackend, SearchFilter)
    # search_fields = [
    #     'name',
    #     'actor__fname',
    #     'actor__lname',
    # ]

    #
    #
    # def get_queryset(self):
    #     queryset = Movie.objects.all()
    #     qs = self.request.GET.get('q')
    #     if qs is not None:
    #         queryset = queryset.filter(
    #             Q(name__icontains=qs)
    #         ).distinct()
    #         key = queryset[0].pk
    #         queryset = Actor.objects.filter(movie_id=key)
    #         queryset_serializer = ActorSerializer(queryset, many=True)
    #         print('!!!!!!!!!!!!!!!!!!!!!!!!!!!', queryset_serializer.data)
    #         return queryset_serializer
    #     return queryset

    # def get_object(self):
    #     queryset = self.get_queryset()
    #     qs = self.request.GET.get('q')
    #     if qs is not None:
    #         queryset = queryset.filter(
    #             Q(name__icontains=qs)
    #         ).distinct()
    #         pk = queryset[0].pk
    #         queryset = get_object_or_404(queryset, pk=pk)
    #     return queryset

# class ActorList(generics.ListAPIView):
#     lookup_field = 'pk'
#     serializer_class = ActorSerializer
#
#     def get_queryset(self):
#         queryset = Actor.objects.all()
#         qs = self.request.GET.get('q')
#         if qs is not None:
#             queryset = queryset.filter(
#                 Q(name__icontains=qs)
#             ).distinct()
#             key = queryset[0].pk
#             queryset = Actor.objects.filter(movie_id=key)
#             print('!!!!!!!!!!!!!!!!!!!!!!!!!!!', queryset)
#         return queryset



#
# def movie_list(request):
#     query = request.GET.get("q_m")
#     if query:
#         q_list = Actor.objects.filter(movie_id__name__icontains=query)
#         print('@@@@@@@@@@@@@@@@@@@@@@@',q_list)
#
#     movies = Movie.objects.all().order_by('name')
#     return render(request, 'imdb_api/movie_list.html', {'movies': movies})
#
#
# def movie_detail(request, pk):
#     movie = get_object_or_404(Movie, pk=pk)
#     actors = Actor.objects.filter(movie_id=pk)
#     ratings = Rating.objects.filter(movie_id_id=pk)
#     return render(request, 'imdb_api/movie_detail.html',
#                   {'movie': movie,
#                    'actors': actors,
#                    'ratings': ratings,
#                    })

# def rate_new(request, pk):
#     if request.method == 'POST':
#         form = RatingForm(request.POST)
#
#         if form.is_valid():
#             rateObj = Rating()
#             rateObj.rate = int(request.POST['user_rate'])
#             rateObj.comment = request.POST['user_comment']
#             rateObj.movie_id_id = pk
#             rateObj.save()
#             return redirect('movie_detail', pk=pk)
#         else:
#             return render(request, 'imdb_api/rate_new.html', {
#                 'form': form,
#                 'error': ('There was a problem with your submission.',)
#             })
#     else:
#         form = RatingForm()
#         movie = get_object_or_404(Movie, pk=pk)
#         return render(request, 'imdb_api/rate_new.html', {
#             'form': form,
#             'movie': movie,
#         })
