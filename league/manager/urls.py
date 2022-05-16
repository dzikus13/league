from django.contrib import admin
from django.urls import path, re_path

from .views import leagues, league_details, LeagueAddView, LeagueEditView

urlpatterns = [
    path("leagues", leagues, name="league_list"),
    re_path("league/(?P<league_id>\d+)", league_details, name="league_details"),
    path("league_add", LeagueAddView.as_view(), name="league_add"),
    re_path("league_edit/(?P<pk>\d+)", LeagueEditView.as_view(), name="league_edit"),
]