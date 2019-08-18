from django.urls import path, include
from . import views

from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    # path('', views.MovieList.as_view(), name='MoveList'),
    # path('actors/', views.ActorList.as_view(), name='ActorList')

    path('api/v1/movie/', views.movie_list, name='movie_list'),
    path('api/v1/actor/', views.actor_list, name='actor_list'),
    path('api/v1/movie/<int:pk>/rates', views.rates, name='rates'),

    # path('movie/<int:pk>/', views.movie_detail, name='movie_detail'),
    # path('movie/<int:pk>/new/', views.rate_new, name='rate_new'),
]

