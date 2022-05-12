from django.core.exceptions import ValidationError
from django.db import models

# Create your models here.


class League(models.Model):
    name = models.CharField(max_length=50)
    max_number_of_teams = models.IntegerField(10)
    points_for_win = 3
    points_for_lost = 0
    points_for_draw = 1

    @property
    def teams_number(self):
        return self.team_set.all().count()

    @property
    def all_matches(self):
        return self.match_set.all().count()

    @property
    def played_matches(self):
        return self.match_set.filter(result__isnull=False).count()

    @property
    def ended(self):
        # TODO: Implement conditions for ending a league
        if self.all_matches == self.played_matches:
            return True
        else:
            return False

    @property
    def winner(self):
        # TODO: Implement condition for winning a league
        pass


class Team(models.Model):
    league = models.ForeignKey(League)
    team_id = models.CharField(max_length=10)
    matches_won = models.IntegerField()
    matches_draw = models.IntegerField()
    matches_lost = models.IntegerField()

    def save(self, *args, **kwargs):
        if self.league.teams_number >= self.league.max_teams_in_league:
            raise ValidationError("Max number of teams exceeded", code="max_teams")
        return super().save(*args, **kwargs)

class SumOfPoints(models.Model):
    pass


class Result(models.Model):
    pass


class Match(models.Model):
    time = models.DateTimeField()
    league = models.ForeignKey(League, on_delete=models.CASCADE)
    result = models.CharField(max_length=20, null=True)


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
    match_id = models.ForeignKey(Match, on_delete=models.CASCADE)