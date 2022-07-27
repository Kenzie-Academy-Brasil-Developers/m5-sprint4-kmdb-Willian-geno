from rest_framework import serializers
from genre.serializers import GenreSerializer
from movie.models import Movie


class MovieSerializer(serializers.ModelSerializer):


    class Meta:
        model = Movie
        fields = "__all__"
    
    def create(self, validated_data):
        return Movie.objects.create(**validated_data)
