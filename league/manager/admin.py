from django.contrib import admin

# Register your models here.
from .models import League, Match, Team, TeamPlayer, Event, EventType

class LeagueManager(admin.ModelAdmin):
    list_display = ["name", "max_number_of_teams", "points_for_win", "points_for_lost", "points_for_draw",
                    "teams_number", "all_matches", "played_matches", "ended", "winner"]


class TeamManager(admin.ModelAdmin):
    list_display = ["team_name", "matches_won", "matches_draw", "matches_lost", "league", "max_players_number",
                    "number_of_players", "sum_of_points", "matches_teams_played"]


class MatchManager(admin.ModelAdmin):
    list_display = ["time", "result", "league"]
    # list_display.append("teams") wywala blad
    # list_display.append("save") to chyba nie jest nawet property ale sie nie znam na tym co backend zrobil


class TeamPlayerManager(admin.ModelAdmin):
    list_display = ["team", "score", "nick"]


class EventTypeManager(admin.ModelAdmin):
    list_display = ["name"]


class EventManager(admin.ModelAdmin):
    list_display = ["time", "player", "event_type", "match"]


admin.site.register(League, LeagueManager)
admin.site.register(Team, TeamManager)
admin.site.register(Match, MatchManager)
admin.site.register(TeamPlayer, TeamPlayerManager)
admin.site.register(Event, EventManager)
admin.site.register(EventType, EventTypeManager)


