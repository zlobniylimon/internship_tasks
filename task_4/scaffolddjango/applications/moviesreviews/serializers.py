from rest_framework import serializers
from applications.moviesreviews.models import *


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source='author.username', read_only=True)

    class Meta:
        model = Comment
        exclude = ()


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source='author.username', read_only=True)

    class Meta:
        model = Review
        exclude = ()


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        exclude = ()
