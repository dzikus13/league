from django.contrib import admin
from django.urls import path, re_path

from .views import base, error, manager, add_forms
from .views import leagues, league_details
from .views import teams, team_details
from .views import matches, match_details
from .views import players, player_details
from .views import event_types, event_type_details
from .views import events, event_details




urlpatterns = [
    path("", manager),
    path("base", base),
    path("error", error),
    path("manager", manager),
    path("add_forms", add_forms),

    path("leagues", leagues, name="league_list"),
    re_path(r"league_details/(?P<league_id>\d+)", league_details, name="league_details"),
    path("league_details", leagues, name="league_list"),
    # jezeli nie podane zostanie id wyswietli liste

    path("teams", teams, name="team_list"),
    re_path(r"team_details/(?P<team_id>\d+)", team_details, name="team_details"),
    path("team_details", teams, name="team_list"),
    # jezeli nie podane zostanie id wyswietli liste

    path("matches", matches, name="match_list"),
    re_path(r"match_details/(?P<match_id>\d+)", match_details, name="match_details"),
    path("match_details", matches, name="match_list"),
    # jezeli nie podane zostanie id wyswietli liste

    path("players", players, name="player_list"),
    re_path(r"player_details/(?P<player_id>\d+)", player_details, name="player_details"),
    path("player_details", players, name="player_list"),
    # jezeli nie podane zostanie id wyswietli liste

    path("event_types", event_types, name="event_types_list"),
    re_path(r"event_type_details/(?P<event_type_id>\d+)", event_type_details, name="event_type_details"),
    path("event_type_details", event_types, name="event_types_list"),
    # jezeli nie podane zostanie id wyswietli liste

    path("events", events, name="events_list"),
    re_path(r"event_details/(?P<event_id>\d+)", event_details, name="event_details"),
    path("event_details", events, name="event_list"),
    # jezeli nie podane zostanie id wyswietli liste
]
