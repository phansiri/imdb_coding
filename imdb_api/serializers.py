from rest_framework import serializers
from .models import Movie, Actor, Rating

class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'

class RatingSerializer(serializers.ModelSerializer):
    # validates the max and min of rate
    rate = serializers.IntegerField(min_value=1, max_value=5)
    class Meta:
        model = Rating
        fields = '__all__'

    def create(self, validated_data):
        return Rating.objects.create(**validated_data)

class MovieSerializer(serializers.ModelSerializer):
    actors = ActorSerializer(many=True, read_only=True)
    class Meta:
        model = Movie
        fields = '__all__'

    def validate(self, attrs):
        qs = Movie.objects.filter(name__iexact=attrs)
        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise serializers.ValidationError("That movie already exists in the database")
        return attrs
