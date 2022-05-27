from django.contrib import admin

# Register your models here.
from .models import League, Match, Team, TeamPlayer, Event, EventType

class LeagueManager(admin.ModelAdmin):
    list_display = []
    list_display.append("name")
    list_display.append("max_number_of_teams")
    list_display.append("points_for_win")
    list_display.append("points_for_lost")
    list_display.append("points_for_draw")
    list_display.append("teams_number")
    list_display.append("all_matches")
    list_display.append("played_matches")
    list_display.append("ended")
    list_display.append("winner")


class TeamManager(admin.ModelAdmin):
    list_display = []
    list_display.append("team_name")
    list_display.append("matches_won")
    list_display.append("matches_draw")
    list_display.append("matches_lost")
    list_display.append("league")
    list_display.append("max_players_number")
    list_display.append("number_of_players")
    list_display.append("sum_of_points")
    list_display.append("matches_teams_played")


class MatchManager(admin.ModelAdmin):
    list_display = []
    list_display.append("time")
    list_display.append("result")
    # list_display.append("teams") wywala blad
    list_display.append("league")
    # list_display.append("save") to chyba nie jest nawet property ale sie nie znam na tym co backend zrobil


class TeamPlayerManager(admin.ModelAdmin):
    list_display = []
    list_display.append("team")
    list_display.append("score")
    list_display.append("nick")


class EventTypeManager(admin.ModelAdmin):
    list_display = []
    list_display.append("name")


class EventManager(admin.ModelAdmin):
    list_display = []
    list_display.append("time")
    list_display.append("player")
    list_display.append("event_type")
    list_display.append("match")


admin.site.register(League, LeagueManager)
admin.site.register(Team, TeamManager)
admin.site.register(Match, MatchManager)
admin.site.register(TeamPlayer, TeamPlayerManager)
admin.site.register(Event, EventManager)
admin.site.register(EventType, EventTypeManager)


