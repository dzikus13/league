from django.contrib import admin

# Register your models here.
from .models import League, Match, Team, TeamPlayer, Event, EventType


class LeagueManager(admin.ModelAdmin):
    list_display = ["name",
                    "is_ended",
                    "max_number_of_teams",
                    "points_for_win",
                    "points_for_lost",
                    "points_for_draw",
                    "teams_number",
                    "all_matches",
                    "league_winner"]


class TeamManager(admin.ModelAdmin):
    list_display = ["league",
                    "team_name",
                    "sum_of_points",
                    "matches_team_played",
                    "number_of_matches_won",
                    "number_of_matches_lost",
                    "number_of_matches_drawn"
                    ]


class MatchManager(admin.ModelAdmin):
    list_display = [
                    "league",
                    "match_date",
                    "match_duration",
                   # "teams",
                    "match_ended",
                    "winner",
                    "loser",
                    "draw_match"
                    ]


class TeamPlayerManager(admin.ModelAdmin):
    list_display = ["team",
                    "player_nick",
                    "goals_scored_by_player"]


class EventManager(admin.ModelAdmin):
    list_display = ["event_type",
                    "match",
                    "team",
                    "player"]


admin.site.register(League, LeagueManager)
admin.site.register(Team, TeamManager)
admin.site.register(Match, MatchManager)
admin.site.register(TeamPlayer, TeamPlayerManager)
admin.site.register(Event, EventManager)

