from django.test import TestCase
from rest_framework.test import APITestCase
from .models import Rating, Movie

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