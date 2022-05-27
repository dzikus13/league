from django.core.exceptions import ValidationError
from django.db import models
from datetime import datetime


class League(models.Model):
    name = models.CharField(max_length=50)
    points_for_win = models.IntegerField(default=3)
    points_for_lost = models.IntegerField(default=0)
    points_for_draw = models.IntegerField(default=1)
    max_number_of_teams = models.IntegerField(default=10)

    def __str__(self):
        return self.name

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
        if self.is_ended:
            teams = []
            team_points = []
            for team in self.team_set.all():
                teams.append(team)
                team_points.append(team.sum_of_points)
            return teams[team_points.index(max(team_points))]
        else:
            return None


class Team(models.Model):
    league = models.ForeignKey(League, on_delete=models.CASCADE)
    team_name = models.CharField(max_length=10)
    MAX_NUMBER_OF_PLAYERS = 4
    
    def save(self, *args, **kwargs):
        if self.league.teams_number >= self.league.max_number_of_teams:
            raise ValidationError("Max number of teams exceeded", code="max_teams")
        return super().save(*args, **kwargs)

    @property  # TODO:Zuzannka77 add test to check if this property works properly
    def sum_of_points(self):
        return self.number_of_matches_won * self.league.points_for_win + \
               self.number_of_matches_drawn * self.league.points_for_draw + \
               self.number_of_matches_lost * self.league.points_for_lost

    @property  # TODO:Zuzannka77 add test to check if this property works properly
    def matches_team_played(self):
        return self.number_of_matches_won + \
               self.number_of_matches_drawn + \
               self.number_of_matches_lost
    
    @property
    def number_of_matches_won(self):
        return Event.objects.filter(event_type=EventType.MATCH_WON, team=self).count()

    @property
    def number_of_matches_lost(self):
        return Event.objects).filter(event_type=EventType.MATCH_LOST, team=self).count()

    @property
    def number_of_matches_drawn(self):
        return Event.objects.filter(event_type=EventType.MATCH_DRAW, team=self).count()


class Match(models.Model):
    league = models.ForeignKey(League, on_delete=models.CASCADE)
    match_date = models.DateTimeField(default=datetime.now, blank=True)
    match_duration = models.DurationField(default="01:30:00")
    teams = models.ManyToManyField(Team)
    match_ended = models.BooleanField(default=False)

    def goals_amount_team(self, which_team):
        return Event.objects.all().filter(event_type=EventType.MATCH_GOAL, team=which_team, match=self).count()

    def goals_amount_dict(self):
        my_dict = {}
        for team in self.teams.all():
            amount = self.goals_amount_team(team)
            my_dict[team.id] = amount
        return my_dict

    @property
    def winner(self):
        if not self.draw_match and self.match_ended:
            my_dict = self.goals_amount_dict()
            my_dict_sorted = sorted(my_dict.items(), key=lambda x: x[1], reverse=True)
            winner_id = my_dict_sorted[0][0]
            event = Event.objects.get_or_create(event_type=EventType.MATCH_WON, match=self, team=Team.objects.get(pk=winner_id))
            return Team.objects.get(pk=winner_id)
        else:
            return False

    @property
    def loser(self):
        if not self.draw_match and self.match_ended:
            my_dict = self.goals_amount_dict()
            my_dict_sorted = sorted(my_dict.items(), key=lambda x: x[1])
            loser_id = my_dict_sorted[0][0]
            event = Event.objects.get_or_create(event_type=EventType.MATCH_LOST, match=self, team=Team.objects.get(pk=loser_id))
            return Team.objects.get(pk=loser_id)
        else:
            return False

    @property
    def draw_match(self):
        if self.match_ended:
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

    def save(self, *args, **kwargs):
        if TeamPlayer.objects.filter(team=self.team).count() >= Team.MAX_NUMBER_OF_PLAYERS:
            raise ValidationError("Maximum number of players in this team exceeded", code="too_much_players")
        return super().save(*args, **kwargs)
    
    @property
    def goals_scored_by_player(self):
        return Event.objects.filter(event_type=EventType.MATCH_GOAL, player=self).count()


class EventType(models.TextChoices):

    MATCH_WON = "Match has been won"
    MATCH_LOST = "Match has been lost"
    MATCH_DRAW = "Match has been drawn"
    MATCH_GOAL = "Goal has been scored"
    MISSING = "Event not specified"


class Event(models.Model):
    event_type = models.CharField(max_length=20, choices=EventType.choices, default="MISSING")
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    player = models.ForeignKey(TeamPlayer, on_delete=models.CASCADE, null=True, blank=True)

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
