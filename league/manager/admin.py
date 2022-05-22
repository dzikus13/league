from django.contrib import admin

# Register your models here.
from .models import League, Match, Team, TeamPlayer, Event, EventType

class LeagueManager(admin.ModelAdmin):
    list_display = []
    list_display.append("name")
    list_display.append("ended")
    list_display.append("max_number_of_teams")
    list_display.append("points_for_win")
    list_display.append("points_for_lost")
    list_display.append("points_for_draw")
    list_display.append("teams_number")
    list_display.append("all_matches")
    list_display.append("played_matches")
    list_display.append("ended")
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


class MatchManager(admin.ModelAdmin):
    list_display = []
    list_display.append("match_duration")
    list_display.append("amount_gols")
    list_display.append("winner")
    list_display.append("loser")
    list_display.append("drawn")
    list_display.append("league")


class TeamPlayerManager(admin.ModelAdmin):
    list_display = []
    list_display.append("team")
    list_display.append("player_nick")
    list_display.append("goals")

'''
# zmieniono ten model od czasu napisania tej linijki
class EventTypeManager(models.Model):
    list_display = []
'''


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
# admin.site.register(EventType, EventTypeManager)

