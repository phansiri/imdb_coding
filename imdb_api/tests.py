from django.test import TestCase
from rest_framework.test import APITestCase, APIRequestFactory, APIClient
from rest_framework.authtoken.models import Token
from .views import api_movie_list
from .models import Rating, Movie, Actor

# test add rate API
class RateAPITestCase(APITestCase):
    def setUp(self) -> None:
        movie = Movie.objects.create(
            name='Test'
        )
        key = movie.pk
        rate = Rating.objects.create(
            rate=4,
            comment="test",
            movie_id_id=key
        )
    def test_single_rate(self):
        rate_count = Rating.objects.count()
        self.assertEqual(rate_count, 1)

# Test Movie
class MovieAPITestCase(APITestCase):
    def setUp(self) -> None:
        self.uri = '/api/v1/movie/'
        self.client = APIClient()

    # test the response to ensure status code 200 is returned
    def test_list(self):
        print(self.uri)
        print(self.client.get(self.uri))
        response = self.client.get(self.uri)
        self.assertEqual(response.status_code, 200, 'Expected Response Code 200, recieved {0} instead.'.format(response.status_code))

# Test Actor
class ActorAPITestCase(APITestCase):
    def setUp(self) -> None:
        self.uri = '/api/v1/actor/'
        self.client = APIClient()

    # test the response to ensure status code 200 is returned
    def test_list(self):
        print(self.uri)
        print(self.client.get(self.uri))
        response = self.client.get(self.uri)
        self.assertEqual(response.status_code, 200, 'Expected Response Code 200, recieved {0} instead.'.format(response.status_code))