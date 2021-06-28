from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.contrib.auth.models import User


class Movie(models.Model):
    """
    Фильм
    """
    title = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=500, null=False, default='')
    release_date = models.DateField()
    director = models.CharField(max_length=100)


class Review(models.Model):
    """
    Рецензия
    """
    content = models.CharField(max_length=1000, null=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    rating_value = models.IntegerField(validators=[MaxValueValidator(10), MinValueValidator(1)])
    movie = models.ForeignKey(to=Movie, null=False, on_delete=models.CASCADE)


class Comment(models.Model):
    """
    Комментарий к рецензии
    """
    content = models.CharField(max_length=250, null=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    review = models.ForeignKey(to=Review, null=False, on_delete=models.CASCADE)
