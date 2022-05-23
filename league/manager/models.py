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
        if self.is_ended:
            return max(self.team_set.all().sum_of_points)
        else:
            return None

    #TODO: Some a in test for this validation
    def save(self, *args, **kwargs):
        if self.teams_number < self.MIN_NUMBER_OF_TEAMS:
            raise ValidationError("Number of teams is not enough", code="not_enough_teams")
        return super().save(*args, **kwargs)


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

    def goals_amount_team(self, which_team):
        # TODO:elzbietagawickaLOVE Number of goals scored by the team
        return Event.objects.all().filter(Event.event_type == "MATCH_GOAL", Event.team == which_team).count()

    def goals_amount_dict(self):
        my_dict = {}
        for team in self.Match.teams:
            amount = self.goals_amount_team(team)
            my_dict[team] = amount
        return my_dict

    @property
    def winner(self):
        # TODO:elzbietagawickaLOVE Winner in match
        my_dict = self.goals_amount_dict()
        my_dict_sorted = sorted(my_dict.items(), key=lambda x: x[1])
        return list(my_dict_sorted.keys())[0]

    @property
    def loser(self):
        # TODO:elzbietagawickaLOVE Loser in match
        my_dict = self.goals_amount_dict()
        my_dict_sorted = sorted(my_dict.items(), key=lambda x: x[1], reverse=True)
        return list(my_dict_sorted.keys())[0]
    
    @property
    def drawn(self):
        my_dict = self.goals_amount_dict()
        res = True
        test_val = list(my_dict.values())[0]
        for elem in my_dict:
            if my_dict[elem] != test_val:
                res = False
                break
        if res is False:
            return False
        else:
            return True


class TeamPlayer(models.Model):
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True)
    player_nick = models.CharField(max_length=20)

    @property
    def goals(self):
        # TODO: Number of goals scored by the player
        pass


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
    player = models.ForeignKey(TeamPlayer, on_delete=models.CASCADE)
    event_time = models.DateTimeField(auto_now_add=True)

    @classmethod
    def get_events_for(cls, match, event_type=None):
        ret_qs = cls.objects.filter(match=match)
        if event_type is not None:
            ret_qs = ret_qs.filter(event_type=event_type)
        return ret_qs
