from django.db import models

class Review(models.Model):
    stars = models.IntegerField()
    reviews = models.TextField()
    spoilers = models.BooleanField(default=False)
    recomendation = models.CharField(max_length=50)

    movie = models.ForeignKey(to = "movie.Movie", on_delete=models.CASCADE, related_name='review')
    user = models.ForeignKey(to = "users.User", on_delete=models.CASCADE, related_name='review')
