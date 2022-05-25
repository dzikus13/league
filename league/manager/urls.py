from django.contrib import admin
from django.urls import path, re_path

from .views import base, main, view, error, manager, add_forms
from .views import leagues, league_details, add_league
from .views import teams, team_details, add_team
from .views import matches, match_details, add_match
from .views import players, player_details, add_player, add_player_stats
from .views import events, add_event
from .views import login, register


urlpatterns = [
    path("", main),
    path("view", view),
    path("manager", manager),
    path("base", base),
    path("error", error),
    path("manager", manager),
    path("add_forms", add_forms),
    path("add_event", add_event),
    path("add_league", add_league),
    path("add_match", add_match),
    path("add_player", add_player),
    path("add_player_stats", add_player_stats),
    path("add_team", add_team),
    path("login", login),
    path("register", register),
    path("events", events),

    path("leagues", leagues, name="league_list"),
    re_path(r"league_details/(?P<league_id>\d+)", league_details, name="league_details"),
    path("league_details", leagues, name="league_list"),

    path("teams", teams, name="team_list"),
    re_path(r"team_details/(?P<team_id>\d+)", team_details, name="team_details"),
    path("team_details", teams, name="team_list"),

    path("matches", matches, name="match_list"),
    re_path(r"match_details/(?P<match_id>\d+)", match_details, name="match_details"),
    path("match_details", matches, name="match_list"),

    path("players", players, name="player_list"),
    re_path(r"player_details/(?P<player_id>\d+)", player_details, name="player_details"),
    path("player_details", players, name="player_list"),

]
