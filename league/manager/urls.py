from django.contrib import admin
<<<<<<< HEAD
from django.urls import path

from .views import leagues
from .views import manager


urlpatterns = [
    path("", manager),
    path("leagues", leagues)
=======
from django.urls import path, re_path

from .views import leagues, league_details

urlpatterns = [
    path("leagues", leagues, name="league_list"),
    re_path("league/(?P<league_id>\d+)", league_details, name="league_details")
>>>>>>> BACKEND
]