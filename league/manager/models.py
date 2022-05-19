from enum import Enum
from django.core.exceptions import ValidationError
from django.db import models


class League(models.Model):
    MIN_NUMBER_OF_TEAMS = 2
    name = models.CharField(max_length=50)
    points_for_win = models.IntegerField(default=3)
    points_for_lost = models.IntegerField(default=0)
    points_for_draw = models.IntegerField(default=1)
    max_number_of_teams = models.IntegerField(default=10)

    @property
    def teams_number(self):
        return self.team_set.all().count()

    @property
    def all_matches(self):
        return self.match_set.all().count()

    @property
    def played_matches(self):
        return self.match_set.filter(winner__isnull=False, drawn__isnull=False).count()

    @property
    def is_ended(self):
        if self.all_matches > 0:
            return self.all_matches == self.played_matches
        else:
            return False

    @property
    def league_winner(self):
        # TODO: Implement condition for winning a league ASAP
        pass

    #TODO: Some a in test for this validation
    '''
    def save(self, *args, **kwargs):
        if self.teams_number < self.MIN_NUMBER_OF_TEAMS:
            raise ValidationError("Number of teams is not enough", code="not_enough_teams")
        return super().save(*args, **kwargs)
    '''

class Team(models.Model):
    league = models.ForeignKey(League, on_delete=models.CASCADE)
    team_name = models.CharField(max_length=10)
    matches_won = models.IntegerField(default=0)
    matches_draw = models.IntegerField(default=0)
    matches_lost = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        if self.league.teams_number >= self.league.max_number_of_teams:
            raise ValidationError("Max number of teams exceeded", code="max_teams")
        return super().save(*args, **kwargs)

    @property  # TODO:Zuzannka77 add test to check if this property works properly
    def sum_of_points(self):
        return self.matches_won * self.league.points_for_win + \
               self.matches_draw * self.league.points_for_draw + \
               self.matches_lost * self.league.points_for_lost

    @property  # TODO:Zuzannka77 add test to check if this property works properly
    def matches_team_played(self):
        return self.matches_won + \
               self.matches_draw + \
               self.matches_lost


class Match(models.Model):
    league = models.ForeignKey(League, on_delete=models.CASCADE)
    match_date = models.DateTimeField(auto_now_add=True)
    match_duration = models.DurationField(default="01:30:00")
    teams = models.ManyToManyField(Team)

    def gols_amount_team(self, which_team):
        # TODO:elzbietagawickaLOVE Number of goals scored by the team2
        return Event.objects.all().filter(Event.event_type == "MATCH_GOAL", Event.team == which_team).count()

    def gols_amount_list(self):
        array = []
        for team in self.Match.teams:
            amount = self.gols_amount_team(team)
            array.append(amount)
        array.sort()
        return array

    @property
    def winner(self):
        # TODO:elzbietagawickaLOVE Winner in match
        array = self.gols_amount_list()
        if array[0] == array[1]:
            return False
        return array[0]

    @property
    def loser(self):
        # TODO:elzbietagawickaLOVE Loser in match
        array = self.gols_amount_list()
        return array[-1]

    @property
    def drawn(self):
        # TODO:elzbietagawickaLOVE Draw in match
        array = self.gols_amount_list()
        if array.count(array[0]) == len(array):
            return True
        return False


class TeamPlayer(models.Model):
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True)
    player_nick = models.CharField(max_length=20)

    @property
    def goals(self):
        # TODO: Number of goals scored by the player
        pass


class EventType(models.TextChoices):  # TODO:Shefour try adding enum to database :)
    MATCH_WON = "Match has been won"
    MATCH_LOST = "Match has been lost"
    MATCH_DRAW = "Match has been drawn"
    MATCH_GOAL = "Goal has been scored"


class Event(models.Model):
    event_type = models.CharField(max_length=20, choices=EventType.choices)
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
