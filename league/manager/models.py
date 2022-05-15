from django.core.exceptions import ValidationError
from django.db import models

# Create your models here.


class League(models.Model):
    name = models.CharField(max_length=50)
    max_number_of_teams = models.IntegerField(default=10)
    points_for_win = models.IntegerField(default=3)
    points_for_lost = models.IntegerField(default=0)
    points_for_draw = models.IntegerField(default=1)

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
        if self.all_matches > 0:
            return self.all_matches == self.played_matches
        else:
            return False

    @property
    def winner(self):
        # TODO: Implement condition for winning a league
        pass


class Team(models.Model):
    team_name = models.CharField(max_length=10)
    matches_won = models.IntegerField(default=0)
    matches_draw = models.IntegerField(default=0)
    matches_lost = models.IntegerField(default=0)
    league = models.ForeignKey(League, on_delete=models.CASCADE)
    max_players_number = models.IntegerField(default=11)


    def number_of_players(self):
        return self.teamplayer_set.all().count


    @property
    def sum_of_points(self):
        return self.matches_won * self.league.points_for_win\
            + self.matches_draw * self.league.points_for_draw \
            + self.matches_lost * self.league.points_for_lost


    @property
    def matches_teams_played(self):
        return self.matches_won + self.matches_draw + self.matches_lost



class Match(models.Model):
    # match_id = models.IntegerField()
    # bo nie potrzebne
    time = models.DateTimeField()
    result = models.IntegerField(default=0)
    teams = models.ManyToManyField(Team)
    league = models.ForeignKey(League, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if self.league.number_of_players >= self.team.max_players_number:
            raise ValidationError("Max number of players exceed", code="max_players")
        if self.league.number_of_players() <= 0:
            raise ValidationError("Number of players is not enough", code="not_enough_players")
        if self.league.teams_number() >= self.league.max_number_of_teams:
            raise ValidationError("Max number of teams exceed", code="max_teams")
        if self.league.teams_number() < 2:
            raise ValidationError("Number of teams is not enough", code="not_enough_teams")
        return super().save(*args, **kwargs)


class TeamPlayer(models.Model):
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True)
    score = models.IntegerField(default=0)
    nick = models.CharField(max_length=20)


class EventType(models.Model):
    name = models.CharField(max_length=30)


class Event(models.Model):
    time = models.DateTimeField()
    player = models.ForeignKey(TeamPlayer, on_delete=models.CASCADE)
    event_type = models.ForeignKey(EventType, on_delete=models.CASCADE)
    match = models.ForeignKey(Match, on_delete=models.CASCADE)

