from django.core.exceptions import ValidationError
from django.test import TestCase
from django.utils import timezone

# Create your tests here.

from .models import League, Team, TeamPlayer, Match, Event


class LeagueTest(TestCase):
    def test_league_adding(self):
        self.assertEqual(League.objects.all().count(), 0)
        league = League(name="Test league 1")
        league.save()
        self.assertEqual(League.objects.all().count(), 1)
        l = League.objects.create(name="Test League 2")
        self.assertEqual(League.objects.all().count(), 2)

    def test_max_league_teams(self):
        self.assertEqual(League.objects.all().count(), 0)
        league = League(name="Test league 1", max_number_of_teams=0)
        league.save()
        with self.assertRaises(ValidationError):
            team = Team.objects.create(league=league, team_name="Test team name")


class LeagueAddedTest(TestCase):
    def setUp(self):
        self.league = League.objects.create(name="Test league")
    def test_league_name(self):
        self.assertEqual(self.league.name,"Test league")

    def test_league_teams(self):
        self.assertEqual(self.league.teams_number, 0)

    def tearDown(self):
        self.league.delete()

    def test_teams_number(self):
        self.assertEqual(Team.objects.all().count(), 0)
        self.team = Team.objects.create(league=self.league, team_name="Test team name")
        self.assertEqual(Team.objects.all().count(), 1)
        self.assertEqual(self.league.teams_number, 1)
        self.league2 = League(name="Test league 2")
        self.league2.save()
        self.team2 = Team.objects.create(league=self.league2, team_name="Test 2")
        self.assertEqual(Team.objects.all().count(), 2)
        self.assertEqual(self.league.teams_number, 1)
        self.assertEqual(self.league2.teams_number, 1)


class MaxPlayersTest(TestCase):
    def setUp(self):
        self.league = League.objects.create(name="Test league")

    def test_league_name(self):
        self.assertEqual(self.league.name,"Test league")

    def test_league_teams(self):
        self.assertEqual(self.league.teams_number, 0)

    def tearDown(self):
        self.league.delete()

    def test_players_max_number(self):
        self.assertEqual(Team.objects.all().count(), 0)
        self.team = Team.objects.create(league=self.league, team_name="Test team name")
        self.assertEqual(Team.objects.all().count(), 1)
        self.assertEqual(self.league.teams_number, 1)
        self.team_player = TeamPlayer.objects.create(team=self.team, player_nick="player1")
        self.team_player = TeamPlayer.objects.create(team=self.team, player_nick="player2")
        self.assertEqual(TeamPlayer.objects.all().count(), 2)