from django.db import models

# Create your models here.


class League(models.Model):
    name = models.CharField(max_length=50)


class Team(models.Model):
    team_id = models.CharField(max_length=10)


class SumOfPoints(models.Model):
    pass


class Result(models.Model):
    pass


class Match(models.Model):
    time = models.DateTimeField()


class TeamPlayer(models.Model):
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True)
    score = models.IntegerField()
    nick = models.CharField(max_length=20)


class EventType(models.Model):
    name = models.CharField(max_length=30)


class Event(models.Model):
    time = models.DateTimeField()
    player = models.ForeignKey(TeamPlayer, on_delete=models.CASCADE)
    event_type = models.ForeignKey(EventType, on_delete=models.CASCADE)

