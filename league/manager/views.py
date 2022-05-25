from django.shortcuts import render
# from django.shortcuts import HttpResponse
# ^ probowalem uzyc by bezposrednio wyswietlic html

from os import path, listdir
from pathlib import Path
from django.core.exceptions import ObjectDoesNotExist


# skopiowane z settings (i lekko zmienione)
BASE_DIR = Path(__file__).resolve().parent
# .parent jeszcze bylo na koncu
# -----------------------------------------

# Create your views here.
# do tworzenia generic views
from django.views import generic
from .models import League, Match, Team, TeamPlayer, Event, EventType


def base(request):
    return render(request, "manager/base.html")


def list_of_views(request):
    context = {"links_list": []}
    context["links_list"].append("leagues")
    context["links_list"].append("matches")
    context["links_list"].append("teams")
    context["links_list"].append("events")
    context["links_list"].append("players")

    return render(request, "manager/main.html", context)


def debug_manager(request):
    # linki (a wlasciwie to "odnosniki"(ig?) do plikow html z folderu manager)
    directory = path.join(BASE_DIR, "templates/manager")
    model_links = {"links_list": []}
    i = 0
    for filename in listdir(directory):
        f = path.join(directory, filename)
        # checking if it is a .html file
        if path.isfile(f) and path.splitext(f)[1] == '.html':
            model_links["links_list"].append(path.basename(path.splitext(f)[0]))

    return render(request, "manager/manager.html", model_links)


def add_forms(request):
    return render(request, "manager/add_forms.html")

'''
# Stary sposob dla porownania
def leagues(request):
    all_leagues = League.objects.all()
    return render(request, "manager/leagues.html", {"leagues": all_leagues})

def league_details(request, league_id):
    try:
        league = League.objects.get(id=league_id)
        return render(request, "manager/league_details.html", {"league": league})
    except ObjectDoesNotExist:
        return render(request, "manager/error.html", {"error_log": "Nie ma elementu o takim id"})
    except:
        return render(request, "manager/error.html", {"error_log": "brak pewnosci co do tego jaki to blad"})
        # sprawic by mi pycharm nie krzyczal ze tak nie mozna
'''

class Leagues(generic.ListView):
    template_name = 'manager/leagues.html'
    # context_object_name = 'Leagues'
    # gdybym chcial zmienic nazwe, ale wole posluzyc sie default'em (object_list)

    def get_queryset(self):
        return League.objects.all()


class LeagueDetail(generic.DetailView):
    model = League
    template_name = 'manager/league_details.html'


class Teams(generic.ListView):
    template_name = 'manager/teams.html'

    def get_queryset(self):
        return Team.objects.all()
    # TODO wypisac graczy poprawnie


class TeamDetail(generic.DetailView):
    model = Team
    template_name = 'manager/team_details.html'
    # TODO wypisac graczy poprawnie


class Matches(generic.ListView):
    template_name = 'manager/matches.html'

    def get_queryset(self):
        return Match.objects.all()

class MatchDetail(generic.DetailView):
    model = Match
    template_name = 'manager/match_details.html'


class Players(generic.ListView):
    template_name = 'manager/players.html'

    def get_queryset(self):
        return TeamPlayer.objects.all()


class PlayerDetail(generic.DetailView):
    model = TeamPlayer
    template_name = 'manager/player_details.html'

'''
# model zostal calkowicie zmieniony
class EventTypes(generic.ListView):
    template_name = 'manager/event_types.html'

    def get_queryset(self):
        return EventType.objects.all()


class EventTypeDetail(generic.DetailView):
    model = EventType
    template_name = 'manager/event_type_details.html'
'''

class Events(generic.ListView):
    template_name = 'manager/events.html'

    def get_queryset(self):
        return Event.objects.all()


class EventDetail(generic.DetailView):
    model = Event
    template_name = 'manager/event_details.html'

def error_400(request, exception):
    return render(request, 'manager/400.html', status=400)


def error_403(request, exception):
    return render(request, 'manager/403.html', status=403)


def error_404(request, exception):
    return render(request, 'manager/404.html', status=404)


def error_500(request, *args, **argv):
    return render(request, 'manager/500.html', status=500)
