from django.contrib import admin
from django.urls import path, re_path

from .views import base, error, manager, add_forms, main, user_profile
from .views import leagues, league_details, add_league
from .views import teams, team_details, add_team
from .views import matches, match_details, add_match
from .views import players, player_details, add_player, add_player_stats
from .views import event_types, event_type_details, events, event_details, add_event
from .views import register, registered
from .views import login, logged, logout, logged_out
from . import views

urlpatterns = [
    path("base", base),
    path("", manager),
    path("base", base, name="base"),
    path("main", main),
    path("error", error),
    path("manager", manager),
    path("add_forms", add_forms),
    path("add_event", add_event),
    path("user_profile", user_profile),
    path("add_league", add_league),
    path("add_match", add_match),
    path("add_player", add_player),
    path("add_player_stats", add_player_stats),
    path("add_team", add_team),
    path("register", register, name="register"),
    path("login", login, name="login"),
    path("logout", logout),
    path("registered", registered),
    path("logged", logged),
    path("logged_out", logged_out),

    path("leagues", views.Leagues.as_view(), name="leagues"),
    re_path(r"league_details/(?P<pk>[0-9]+)/$", views.LeagueDetail.as_view(), name="league_details"),
    path("league_details", leagues, name="league_list"),
    # jezeli nie podane zostanie id wyswietli liste

    path("teams", views.Teams.as_view(), name="team_list"),
    re_path(r"team_details/(?P<pk>[0-9]+)/$", views.TeamDetail.as_view(), name="team_details"),
    path("team_details", teams, name="team_list"),
    # jezeli nie podane zostanie id wyswietli liste

    path("matches", views.Matches.as_view(), name="match_list"),
    re_path(r"match_details/(?P<pk>[0-9]+)/$", views.MatchDetail.as_view(), name="match_details"),
    path("match_details", matches, name="match_list"),
    # jezeli nie podane zostanie id wyswietli liste

    path("players", views.Players.as_view(), name="player_list"),
    re_path(r"player_details/(?P<pk>[0-9]+)/$", views.PlayerDetail.as_view(), name="player_details"),
    path("player_details", players, name="player_list"),
    # jezeli nie podane zostanie id wyswietli liste

    # path("event_types", views.EventTypes.as_view(), name="event_types_list"),
    # re_path(r"event_type_details/(?P<pk>[0-9]+)/$", views.EventTypeDetail.as_view(), name="event_type_details"),

    path("events", views.Events.as_view(), name="event_list"),
    re_path(r"event_details/(?P<pk>[0-9]+)/$", views.EventDetail.as_view(), name="event_details")
]