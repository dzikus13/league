from django.core.exceptions import ValidationError
from django.test import TestCase

# Create your tests here.

from .models import League, Team

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
            team = Team.objects.create(league=league, team_id="Test team name")



class LeagueAddedTest(TestCase):
    def setUp(self):
        self.league = League.objects.create(name="Test league")

    def test_league_name(self):
        self.assertEqual(self.league.name,"Test league")

    def test_league_teams(self):
        self.assertEqual(self.league.teams_number, 0)

    def tearDown(self):
        self.league.delete()