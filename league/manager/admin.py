from django.contrib import admin

# Register your models here.
from .models import League, Match, Team, TeamPlayer, Event


class LeagueManager(admin.ModelAdmin):
    list_display = ["id", "league_name", "max_number_of_teams_in_league", "points_for_win", "points_for_lost",
                    "points_for_draw", "number_of_teams_in_league", "number_of_all_matches_in_league", "played_matches"]


class TeamManager(admin.ModelAdmin):
    list_display = ["id", "team_name", "team_league", "sum_of_points"]


class MatchManager(admin.ModelAdmin):
    list_display = ["id", "league"]


class TeamPlayerManager(admin.ModelAdmin):
    list_display = ["id", "team"]


class EventManager(admin.ModelAdmin):
    list_display = ["id", "player", "event_type", "match"]


admin.site.register(League, LeagueManager)
admin.site.register(Team, TeamManager)
admin.site.register(Match, MatchManager)
admin.site.register(TeamPlayer, TeamPlayerManager)
admin.site.register(Event, EventManager)
