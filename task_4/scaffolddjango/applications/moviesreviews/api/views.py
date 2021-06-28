from rest_framework import viewsets
from rest_framework.response import Response

from applications.moviesreviews.models import Movie, Review, Comment
from applications.moviesreviews.serializers import MovieSerializer, CommentSerializer, ReviewSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()

    model = Movie
    serializer_class = MovieSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()

    model = Comment
    serializer_class = CommentSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        serializer = ReviewSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save(author=request.user)
        return Response(serializer.data)


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()

    model = Review
    serializer_class = ReviewSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        serializer = ReviewSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save(author=request.user)
        return Response(serializer.data)


