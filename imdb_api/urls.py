from django.urls import path, include
from . import views

from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', views.movie_list, name='movie_list'),
    path('movie/<int:pk>/', views.movie_detail, name='movie_detail'),
    path('movie/<int:pk>/new/', views.rate_new, name='rate_new'),

    path('api/v1/movie/', views.api_movie_list, name='api_movie_list'),
    path('api/v1/actor/', views.api_actor_list, name='api_actor_list'),
    # path('api/v1/movie/<int:pk>', views.api_rates_detail, name='api_rates_detail'),
    # path('api/v1/rate/', views.api_rating_list, name='api_rating_list'),
    path('api/v1/rate/<int:pk>/', views.api_rating_list_search, name='api_rating_list_search'),

    path('api/v1/rate/', views.RateListCreateView.as_view(), name='RateListCreateView')

]

urlpatterns = format_suffix_patterns(urlpatterns)

