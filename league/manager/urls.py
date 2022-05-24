
from django.contrib import admin
from django.urls import path, re_path


from .views import leagues, manager, league_details

handler404 = 'manager.views.error_404'
handler500 = 'manager.views.error_500'
# handler403 = 'manager.views.error_403'
# handler400 = 'manager.views.error_400'


urlpatterns = [
    path("", manager),
    path("leagues", leagues, name="league_list"),
    re_path("league/(?P<league_id>\d+)", league_details, name="league_details")

]