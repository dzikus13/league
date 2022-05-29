from django.contrib import admin

# Register your models here.
from .models import League, Match, Team, TeamPlayer, Event, EventType

class LeagueManager(admin.ModelAdmin):
    list_display = ["name", "max_number_of_teams", "points_for_win", "points_for_lost", "points_for_draw",
                    "teams_number", "all_matches", "played_matches"]


class TeamManager(admin.ModelAdmin):
    list_display = ["team_name", "league", "sum_of_points"]


class MatchManager(admin.ModelAdmin):
    list_display = ["league"]


class TeamPlayerManager(admin.ModelAdmin):
    list_display = ["team"]


class EventManager(admin.ModelAdmin):
    list_display = ["player", "event_type", "match"]


admin.site.register(League, LeagueManager)
admin.site.register(Team, TeamManager)
admin.site.register(Match, MatchManager)
admin.site.register(TeamPlayer, TeamPlayerManager)
admin.site.register(Event, EventManager)


