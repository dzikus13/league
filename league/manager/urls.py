from django.urls import path

from .views import leagues, manager, league_details


urlpatterns = [
    path("", manager),
    path("leagues", leagues, name="league_list"),
    re_path("league/(?P<league_id>\d+)", league_details, name="league_details")
]