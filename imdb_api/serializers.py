from rest_framework import serializers
from .models import Movie, Actor, Rating

# This allows the Actor model to be rendered as JSON objects
# movie_id variable holds a string related field of the id
# the string form is found as a method on the models.py for Actor
# which will return both fname and lname
class ActorSerializer(serializers.ModelSerializer):
    movie_id = serializers.StringRelatedField(many=True)
    class Meta:
        model = Actor
        fields = '__all__'

# This allows the Rate model to be rendered as JSON objects
# rate value is overwritten with a max and min to ensure the integer passed through
# will not break the system
class RatingSerializer(serializers.ModelSerializer):
    # validates the max and min of rate
    rate = serializers.IntegerField(min_value=1, max_value=5)
    class Meta:
        model = Rating
        fields = '__all__'

    # method create with a param of validate_data that is checked again before returning
    # a created rate object
    def create(self, validated_data):
        return Rating.objects.create(**validated_data)

# This allows the Movie model to be rendered as JSON objects
# The actor variable is a nested serializer from Actor. This is done in order to view actors in selected movies
class MovieSerializer(serializers.ModelSerializer):
    actors = ActorSerializer(many=True, read_only=True)
    class Meta:
        model = Movie
        fields = '__all__'

    # method validate takes 1 param. it filters movies with exact name passed in
    # this is done to ensure only one movie with that name can only exists
    def validate(self, attrs):
        qs = Movie.objects.filter(name__iexact=attrs)
        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise serializers.ValidationError("That movie already exists in the database")
        return attrs
