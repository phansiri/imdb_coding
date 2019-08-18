from . import views
from django.urls import path
from rest_framework_swagger.views import get_swagger_view
from rest_framework.urlpatterns import format_suffix_patterns

schema_view = get_swagger_view(title='IMDB API')

# URL in a list
urlpatterns = [

    # Frontend view
    path('', views.movie_list, name='movie_list'),
    path('movie/<int:pk>/', views.movie_detail, name='movie_detail'),
    path('movie/<int:pk>/new/', views.rate_new, name='rate_new'),

    # API view
    path('api/v1/movie/', views.api_movie_list, name='api_movie_list'),
    path('api/v1/actor/', views.api_actor_list, name='api_actor_list'),
    path('api/v1/rate/', views.RateListCreateView.as_view(), name='RateListCreateView'),
    path('api/v1/rate/<int:pk>/', views.api_rating_list_search, name='api_rating_list_search'),

    path('docs/', schema_view, name='docs'),

]

urlpatterns = format_suffix_patterns(urlpatterns)

