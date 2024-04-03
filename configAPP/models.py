# from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.sessions.models import Session
user = get_user_model()
gender = ('man', 'woman')


class Movie(models.Model):
    name = models.CharField(max_length=150)
    year = models.DateField()
    genre = models.CharField(max_length=50)
    actor = models.ManyToManyField('Actor')


class Actor(models.Model):
    gender = (
        ('m', 'man'),
        ('w', 'woman'),
    )

    name = models.CharField(max_length=150)
    birthdate = models.DateField()
    gender = models.CharField(max_length=10, choices=gender, default='man')


class Comment(models.Model):
    user_id = models.ForeignKey(user, on_delete=models.CASCADE)
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
    content = models.TextField()



