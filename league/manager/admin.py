from django.contrib import admin

from .models import League, Match, Team, TeamPlayer, Event, EventType

class LeagueManager(admin.ModelAdmin):
    list_display = [
        "name",
        "max_number_of_teams",
        "points_for_win",
        "points_for_lost",
        "points_for_draw",
        "teams_number",
        "all_matches",
        "played_matches",
        "is_ended",
        "league_winner"]


class TeamManager(admin.ModelAdmin):
    list_display = [
        "team_name", "matches_won", "matches_draw",
        "matches_lost", "league", "sum_of_points",
        "matches_team_played"]


class MatchManager(admin.ModelAdmin):
    list_display = [
        "match_duration",
        "winner", "loser", "draw_match", "league"]


class TeamPlayerManager(admin.ModelAdmin):
    list_display = [
        "team", "player_nick"]


class EventManager(admin.ModelAdmin):
    list_display = ["event_type", "match", "team", "player"]


admin.site.register(League, LeagueManager)
admin.site.register(Team, TeamManager)
admin.site.register(Match, MatchManager)
admin.site.register(TeamPlayer, TeamPlayerManager)
admin.site.register(Event, EventManager)
