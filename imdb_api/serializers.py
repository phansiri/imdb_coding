from rest_framework import serializers
from .models import Movie, Actor, Rating

class ActorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Actor
        fields = [
            'id',
            'fname',
            'lname',
        ]

class RatingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Rating
        fields = [
            'id',
            'rate',
            'comment',
            'movie_id',
        ]

class MovieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Movie
        fields = [
            'id',
            'name',
        ]

    def validate(self, attrs):
        qs = Movie.objects.filter(name__iexact=attrs)
        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise serializers.ValidationError("That movie already exists in the database")
        return attrs

