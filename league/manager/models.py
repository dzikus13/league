from enum import Enum

from django.core.exceptions import ValidationError
from django.db import models
from datetime import datetime


class League(models.Model):
    name = models.CharField(max_length=50)
    points_for_win = models.IntegerField(default=3)
    points_for_lost = models.IntegerField(default=0)
    points_for_draw = models.IntegerField(default=1)
    max_number_of_teams = models.IntegerField(default=10)
    max_number_of_players_in_team = models.IntegerField(default=2)

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
        if self.all_matches > 0:
            return self.all_matches == self.played_matches
        else:
            return False

    @property
    def league_winner(self):
        #TODO: zrobic winnera ligi ASAP
        pass


class Team(models.Model):
    team_name = models.CharField(max_length=10)
    matches_won = models.IntegerField(default=0)
    matches_draw = models.IntegerField(default=0)
    matches_lost = models.IntegerField(default=0)
    league = models.ForeignKey(League, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if self.league.teams_number >= self.league.max_number_of_teams:
            raise ValidationError("Max number of teams exceeded", code="max_teams")
        return super().save(*args, **kwargs)

    @property # TODO:Zuzannka77 add test to check if this property works properly
    def sum_of_points(self):
        return self.matches_won * self.league.points_for_win +\
               self.matches_draw * self.league.points_for_draw +\
               self.matches_lost * self.league.points_for_lost

    @property # TODO:Zuzannka77 add test to check if this property works properly
    def matches_team_played(self):
        return self.matches_won +\
               self.matches_draw +\
               self.matches_lost

    @property
    def players_number(self):
        return self.teamplayer_set.all().count()


class Match(models.Model):
    league = models.ForeignKey(League, on_delete=models.CASCADE)
    # date = models.DateTimeField(default=datetime.now, blank=True)
    match_duration = models.DurationField(default="01:30:00")

    def amount_gols(self):
        # TODO:elzbietagawickaLOVE zrobic ilosc strzelonych goli przez druzyne
        pass

    def winner(self):
        # TODO:elzbietagawickaLOVE zwyciesca meczu
        pass

    def loser(self):
        # TODO:elzbietagawickaLOVE przegrany meczu
        pass

    def drawn(self):
        # TODO:elzbietagawickaLOVE remis w meczu
        pass


class TeamPlayer(models.Model):
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True)
    player_nick = models.CharField(max_length=20)

    @property
    def goals(self):
        # TODO: ilosc goli zdobytych prze gracza
        pass

    def save(self, *args, **kwargs):
        if self.team.players_number >= self.team.league.max_number_of_players_in_team:
            raise ValidationError("Max number of players in that team exceeded", code="max_players_in_team")
        return super().save(*args, **kwargs)


class EventType(Enum): # TODO:Shefour try adding enum to database :)
    MATCH_WON = "Match has been won"
    MATCH_LOST = "Match has been lost"
    MATCH_DRAW = "Match has been drawn"
    MATCH_GOAL = "Goal has been scored"
    MATCH_FIRST_YELLOW = "First yellow card risen"
    MATCH_SECOND_YELLOW = "Second yellow card risen"
    MATCH_RED = "Red card risen"


class Event(models.Model):
    event_type = models.CharField(max_length=20)
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    player = models.ForeignKey(TeamPlayer, on_delete=models.CASCADE)
    event_time = models.DateTimeField(auto_now_add=True)

    @classmethod
    def get_events_for(cls, match, event_type=None):
        ret_qs = cls.objects.filter(match=match)
        if event_type is not None:
            ret_qs = ret_qs.filter(event_type=event_type)
        return ret_qs
