from django.contrib import admin
from django.urls import path, re_path

from .views import base, error, manager, add_forms, user_profile, list_of_views
from .views import add_match, add_event, add_team, add_league, add_player
from .views import register, registered
from .views import login, logged, logout, logged_out
from . import views
# ^^^ do obslugiwania generic views

urlpatterns = [
    path("", list_of_views),
    path("base", base, name="base"),
    path("main", list_of_views),
    path("error", error),
    path("manager", manager),
    path("add_forms", add_forms),
    path("add_event", add_event),
    path("user_profile", user_profile),
    path("add_league", add_league),
    path("add_match", add_match),
    path("add_player", add_player),
    path("add_team", add_team),
    path("register", register, name="register"),
    path("login", login, name="login"),
    path("logout", logout),
    path("registered", registered),
    path("logged", logged),
    path("logged_out", logged_out),

    path("leagues", views.Leagues.as_view(), name="leagues"),
    re_path(r"league_details/(?P<pk>[0-9]+)/$", views.LeagueDetail.as_view(), name="league_details"),

    path("teams", views.Teams.as_view(), name="team_list"),
    re_path(r"team_details/(?P<pk>[0-9]+)/$", views.TeamDetail.as_view(), name="team_details"),
    # TODO wypisac graczy poprawnie

    path("matches", views.Matches.as_view(), name="match_list"),
    re_path(r"match_details/(?P<pk>[0-9]+)/$", views.MatchDetail.as_view(), name="match_details"),

    path("players", views.Players.as_view(), name="player_list"),
    re_path(r"player_details/(?P<pk>[0-9]+)/$", views.PlayerDetail.as_view(), name="player_details")
]