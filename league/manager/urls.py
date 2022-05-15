from django.contrib import admin
from django.urls import path, re_path

from .views import leagues, manager, league_details, base, add_forms, error


urlpatterns = [
    path("", manager),
    path("manager", manager),
    path("leagues", leagues, name="league_list"),
    path("base", base),
    path("add_forms", add_forms),
    path("error", error),
    re_path(r"league_details/(?P<league_id>\d+)", league_details, name="league_details"),
    path("league_details", leagues, name="league_list"), # jezeli nie podane zostanie id wyswietli liste
]
