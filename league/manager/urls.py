from django.contrib import admin
from django.urls import path, re_path

# do korzystania z generic views
from . import views
# ------------------------------

from .views import base, error, debug_manager, add_forms, list_of_views
# '''
# To nie jest wykorzystywane z generic views
# from .views import leagues, league_details
# '''

urlpatterns = [
    path("", list_of_views),
    path("base", base),
    path("main", list_of_views),
    # TODO change the way of handling the errors
    path("error", error),
    path("manager", debug_manager),
    path("add_forms", add_forms),

    # stary sposob
    # path("leagues", leagues, name="league_list"),
    # re_path(r"league_details/(?P<league_id>\d+)", league_details, name="league_details"),
    # path("league_details", leagues, name="league_list"),
    # jezeli nie podane zostanie id wyswietli liste

    # nowy sposob
    path("leagues", views.Leagues.as_view(), name="leagues"),
    re_path(r"league_details/(?P<pk>[0-9]+)/$", views.LeagueDetail.as_view(), name="league_details"),
    # (?P<pk>[0-9]+)/$ ---> pk = primary key
    # nowy reg-ex z https://youtu.be/c3yB0_4Yd48
    # '''

    path("teams", views.Teams.as_view(), name="team_list"),
    re_path(r"team_details/(?P<pk>[0-9]+)/$", views.TeamDetail.as_view(), name="team_details"),
    # TODO wypisac graczy poprawnie

    path("matches", views.Matches.as_view(), name="match_list"),
    re_path(r"match_details/(?P<pk>[0-9]+)/$", views.MatchDetail.as_view(), name="match_details"),

    path("players", views.Players.as_view(), name="player_list"),
    re_path(r"player_details/(?P<pk>[0-9]+)/$", views.PlayerDetail.as_view(), name="player_details"),

    #path("event_types", views.EventTypes.as_view(), name="event_types_list"),
    #re_path(r"event_type_details/(?P<pk>[0-9]+)/$", views.EventTypeDetail.as_view(), name="event_type_details"),

    path("events", views.Events.as_view(), name="events_list"),
    re_path(r"event_details/(?P<pk>[0-9]+)/$", views.EventDetail.as_view(), name="event_details"),
]
