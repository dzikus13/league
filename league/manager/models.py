from enum import Enum
from django.core.exceptions import ValidationError
from django.db import models
from datetime import datetime
from django.utils import timezone


class League(models.Model):
    league_name = models.CharField(max_length=50)
    points_for_win = models.IntegerField(default=3)
    points_for_lost = models.IntegerField(default=0)
    points_for_draw = models.IntegerField(default=1)
    max_number_of_teams_in_league = models.IntegerField(default=10)
    max_number_of_players_in_team = models.IntegerField(default=2)

    def __str__(self):
        return f"{self.id};{self.name}"

    @property
    def number_of_teams_in_league(self):
        return self.team_set.all().count()

    @property
    def number_of_all_matches_in_league(self):
        return self.match_set.all().count()

    @property
    def played_matches(self):
        return self.match_set.filter(event__isnull=False).count()

    @property
    def league_is_ended(self):
        if self.number_of_all_matches_in_league > 0:
            return self.number_of_all_matches_in_league == self.number_of_played_matches_in_league
        else:
            return False

    @property
    def league_winner(self):
        if self.league_is_ended:
            teams = []
            team_points = []
            for team in self.team_set.all():
                teams.append(team)
                team_points.append(team.sum_of_points)
            return teams[team_points.index(max(team_points))]
        else:
            return None


class Team(models.Model):
    team_league = models.ForeignKey(League, on_delete=models.CASCADE)
    team_name = models.CharField(max_length=10)
    MAX_NUMBER_OF_PLAYERS = 4

    def __str__(self):
        return f"{self.id};{self.team_name}"

    def save(self, *args, **kwargs):
        if self.team_league.number_of_teams_in_league >= self.team_league.max_number_of_teams_in_league:
            raise ValidationError("Max number of teams exceeded", code="max_teams")
        return super().save(*args, **kwargs)

    @property  # TODO:Zuzannka77 add test to check if this property works properly
    def sum_of_points(self):
        return self.number_of_matches_won * self.team_league.points_for_win + \
               self.number_of_matches_drawn * self.team_league.points_for_draw + \
               self.number_of_matches_lost * self.team_league.points_for_lost

    @property  # TODO:Zuzannka77 add test to check if this property works properly
    def number_of_played_matches_by_team(self):
        return self.number_of_matches_won + \
               self.number_of_matches_lost + \
               self.number_of_matches_drawn

    @property
    def number_of_players_in_team(self):
        return self.teamplayer_set.all().count()

    @property
    def number_of_matches_won(self):
        return Event.objects.filter(event_type=EventType.MATCH_WON, team=self).count()

    @property
    def number_of_matches_lost(self):
        return Event.objects.filter(event_type=EventType.MATCH_LOST, team=self).count()

    @property
    def number_of_matches_drawn(self):
        return Event.objects.filter(event_type=EventType.MATCH_DRAW, team=self).count()


class Match(models.Model):
    league = models.ForeignKey(League, on_delete=models.CASCADE)
    teams = models.ManyToManyField(Team)
    match_is_ended = models.BooleanField(default=False)
    match_date = models.DateTimeField(default=timezone.now, blank=True)
    match_duration = models.DurationField(default="01:30:00")

    def __str__(self):
        return f"Match #{self.id}"

    def goals_amount_team(self, which_team):
        return Event.objects.filter(event_type=EventType.MATCH_GOAL, team=which_team, match=self).count()

    def goals_amount_dict(self):
        my_dict = {}
        for team in self.teams.all():
            amount = self.goals_amount_team(team)
            my_dict[team.id] = amount
        return my_dict

    @property
    def match_winner(self):
        if not self.match_draw and self.match_is_ended:
            my_dict = self.goals_amount_dict()
            my_dict_sorted = sorted(my_dict.items(), key=lambda x: x[1], reverse=True)
            winner_id = my_dict_sorted[0][0]
            event = Event.objects.get_or_create(event_type=EventType.MATCH_WON, match=self, team=Team.objects.get(pk=winner_id))
            return Team.objects.get(pk=winner_id)
        else:
            return False

    @property
    def match_loser(self):
        if not self.match_draw and self.match_is_ended:
            my_dict = self.goals_amount_dict()
            my_dict_sorted = sorted(my_dict.items(), key=lambda x: x[1])
            loser_id = my_dict_sorted[0][0]
            event = Event.objects.get_or_create(event_type=EventType.MATCH_LOST, match=self, team=Team.objects.get(pk=loser_id))
            return Team.objects.get(pk=loser_id)
        else:
            return False

    @property
    def match_draw(self):
        if self.match_is_ended:
            my_dict = self.goals_amount_dict()
            test_val = list(my_dict.values())[0]
            for elem in my_dict:
                if my_dict[elem] != test_val:
                    return False
            for team in self.teams.all():
                event = Event.objects.get_or_create(event_type=EventType.MATCH_DRAW, match=self, team=Team.objects.get(pk=team.id))
            return True
        else:
            return False


class TeamPlayer(models.Model):
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True)
    player_nick = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.id};{self.player_nick}"

    def save(self, *args, **kwargs):
        if TeamPlayer.objects.filter(team=self.team).count() >= Team.MAX_NUMBER_OF_PLAYERS:
            raise ValidationError("Maximum number of players in this team exceeded", code="too_much_players")
        return super().save(*args, **kwargs)

    @property
    def goals_scored_by_player(self):
        return Event.objects.filter(event_type=EventType.MATCH_GOAL, player=self).count()

    def save(self, *args, **kwargs):
        if self.team.number_of_players_in_team >= self.team.team_league.max_number_of_players_in_team:
            raise ValidationError("Max number of players in that team exceeded", code="max_players_in_team")
        return super().save(*args, **kwargs)


class EventType(models.TextChoices):
    MATCH_WON = "Match has been won"
    MATCH_LOST = "Match has been lost"
    MATCH_DRAW = "Match has been drawn"
    MATCH_GOAL = "Goal has been scored"
    MISSING = "Event not specified"


class Event(models.Model):
    event_type = models.CharField(max_length=20, choices=EventType.choices, default=EventType.MISSING)
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    player = models.ForeignKey(TeamPlayer, on_delete=models.CASCADE, null=True, blank=True)
    event_time = models.TimeField(default=timezone.now, blank=True)

    def __str__(self):
        return f"{self.id}"

    def save(self, *args, **kwargs):
        if self.event_type == EventType.MATCH_GOAL:
            if self.player.team != self.team:
                raise ValidationError("This player doesn't belong to that team", code="invalid_player")
        return super().save(*args, **kwargs)

    @classmethod
    def get_events_for(cls, match, event_type=None):
        ret_qs = cls.objects.filter(match=match)
        if event_type is not None:
            ret_qs = ret_qs.filter(event_type=event_type)
        return ret_qs
