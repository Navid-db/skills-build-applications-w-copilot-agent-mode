from djongo import models
from django.contrib.auth.models import AbstractUser

class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)

class User(AbstractUser):
    email = models.EmailField(unique=True)
    team = models.CharField(max_length=100, null=True, blank=True)

class Activity(models.Model):
    user = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    duration = models.IntegerField()

class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

class Leaderboard(models.Model):
    user = models.CharField(max_length=100)
    points = models.IntegerField()
