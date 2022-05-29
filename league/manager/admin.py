from django.contrib import admin

# Register your models here.
from .models import League, Match, Team, Event, TeamPlayer


class LeagueManger(admin.ModelAdmin):
    list_display = ["league_name", "league_is_ended"]


class MatchManger(admin.ModelAdmin):
    list_display = ["match_winner", "match_loser", "match_draw"]


class TeamPlayerManger(admin.ModelAdmin):
    list_display = ["goals_scored_by_player"]


admin.site.register(League, LeagueManger)
admin.site.register(Match, MatchManger)
admin.site.register(Team)
admin.site.register(Event)
admin.site.register(TeamPlayer, TeamPlayerManger)
