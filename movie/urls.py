from django.urls import path
from movie.views import MovieIdView, MovieView

urlpatterns = [
    path("movie/", MovieView.as_view()),
    path("movie/<int:movie_id>/", MovieIdView.as_view()),
]