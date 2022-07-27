from rest_framework import serializers
from genre.models import Genre


class GenreSerializer(serializers.ModelSerializer):


    class Meta:
        model = Genre
        fields = "__all__"



