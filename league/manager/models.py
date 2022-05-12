from django.db import models

# Create your models here.


class League(models.Model):
    name = models.CharField(max_length=50)
    points_for_win = 3
    points_for_lost = 0
    points_for_draw = 1

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
    team_id = models.CharField(max_length=10)
    matches_won = models.IntegerField()
    matches_draw = models.IntegerField()
    matches_lost = models.IntegerField()

    @property
    def sum_of_points(self):
        return self.matches_won * League.points_for_win + self.matches_draw * League.points_for_draw + self.matches_lost * League.points_for_lost

    @property
    def matches_teams_played(self):
        return self.matches_won + self.matches_draw + self.matches_lost


class Match(models.Model):
    match_id = models.IntegerField()
    time = models.DateTimeField()
    result = models.IntegerField()
    teams = models.ManyToManyField(Team)
    league = models.ForeignKey(League, on_delete=models.CASCADE)


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