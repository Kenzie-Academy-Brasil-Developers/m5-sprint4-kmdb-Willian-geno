from django.db import models

from movie.models import Movie

class Genre(models.Model):
    name = models.CharField(max_length=127)


    movies =  models.ManyToManyField(Movie)