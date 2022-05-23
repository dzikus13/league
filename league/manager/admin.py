from django.contrib import admin

# Register your models here.
from .models import League, Match, Team, TeamPlayer, Event, EventType


class LeagueManager(admin.ModelAdmin):
    list_display = []
    list_display.append("name")
    list_display.append("ended")
    list_display.append("points_for_win")
    list_display.append("points_for_lost")
    list_display.append("points_for_draw")
    list_display.append("max_number_of_teams")
    list_display.append("max_number_of_players_in_team")
    list_display.append("teams_number")
    list_display.append("all_matches")
    list_display.append("played_matches")
    list_display.append("league_winner")


class TeamManager(admin.ModelAdmin):
    list_display = []
    list_display.append("team_name")
    list_display.append("matches_won")
    list_display.append("matches_draw")
    list_display.append("matches_lost")
    list_display.append("league")
    list_display.append("sum_of_points")
    list_display.append("matches_team_played")
    list_display.append("players_number")


class MatchManager(admin.ModelAdmin):
    list_display = []
    list_display.append("league")
    list_display.append("match_duration")


class TeamPlayerManager(admin.ModelAdmin):
    list_display = []
    list_display.append("team")
    list_display.append("player_nick")


class EventTypeManager(admin.ModelAdmin):
    list_display = []
    list_display.append("MATCH_WON")
    list_display.append("MATCH_LOST")
    list_display.append("MATCH_DRAW")
    list_display.append("MATCH_GOAL")
    list_display.append("MATCH_FIRST_YELLOW")
    list_display.append("MATCH_SECOND_YELLOW")
    list_display.append("MATCH_RED")


class EventManager(admin.ModelAdmin):
    list_display = []
    list_display.append("event_type")
    list_display.append("match")
    list_display.append("team")
    list_display.append("player")
    list_display.append("event_time")


admin.site.register(League, LeagueManager)
admin.site.register(Team, TeamManager)
admin.site.register(Match, MatchManager)
admin.site.register(TeamPlayer, TeamPlayerManager)
admin.site.register(Event, EventManager)
