from django.contrib import admin

# Register your models here.
from .models import League, Match, Team, TeamPlayer, Event, EventType


class LeagueManager(admin.ModelAdmin):
    list_display = ["name", "is_ended", "points_for_win", "points_for_lost", "points_for_draw", "max_number_of_teams",
                    "max_number_of_players_in_team", "teams_number", "all_matches", "played_matches", "league_winner"]


class TeamManager(admin.ModelAdmin):
    list_display = ["team_name", "matches_won", "matches_draw", "matches_lost", "league", "sum_of_points",
                    "matches_team_played", "players_number"]


class MatchManager(admin.ModelAdmin):
    list_display = ["league", "match_duration"]


class TeamPlayerManager(admin.ModelAdmin):
    list_display = ["team", "player_nick"]


class EventTypeManager(admin.ModelAdmin):
    list_display = ["MATCH_WON", "MATCH_LOST", "MATCH_DRAW", "MATCH_GOAL", "MATCH_FIRST_YELLOW", "MATCH_SECOND_YELLOW",
                    "MATCH_RED"]


class EventManager(admin.ModelAdmin):
    list_display = ["event_type", "match", "team", "player", "event_time"]


admin.site.register(League, LeagueManager)
admin.site.register(Team, TeamManager)
admin.site.register(Match, MatchManager)
admin.site.register(TeamPlayer, TeamPlayerManager)
admin.site.register(Event, EventManager)
