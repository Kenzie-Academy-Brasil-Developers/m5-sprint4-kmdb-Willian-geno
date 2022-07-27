from django.shortcuts import get_object_or_404
from rest_framework.views import Response, Request, status, APIView
from movie.models import Movie
from rest_framework.pagination import PageNumberPagination

from movie.serializers import MovieSerializer


class MovieView(APIView, PageNumberPagination):
    
    def post(self, request: Request):
        
        serialized = MovieSerializer(data=request.data)
        serialized.is_valid(raise_exception=True)
        serialized.save()
        return Response(serialized.data, status.HTTP_201_CREATED)
       

    def get(self,request: Request):
        movies = Movie.objects.all()
        result_page = self.paginate_queryset(movies, request, view=self)
        serialized = MovieSerializer(result_page, many=True)        
        
        return Response(serialized.data, status.HTTP_200_OK)

class MovieIdView(APIView):

    def get(self, _:Request, movie_id):
        movie =get_object_or_404(Movie, pk=movie_id)
        serialized = MovieSerializer(movie).data

        return Response(serialized, status.HTTP_200_OK)

