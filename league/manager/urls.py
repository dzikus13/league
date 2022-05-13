from django.contrib import admin
from django.urls import path, re_path

from .views import leagues, league_details

urlpatterns = [
    path("leagues", leagues, name="league_list"),
    re_path("league/(?P<league_id>\d+)", league_details, name="league_details")
]