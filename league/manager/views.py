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


def manager(request):
    # linki (a wlasciwie to "odnosniki"(ig?) do plikow html z folderu manager)
    directory = path.join(BASE_DIR, "templates\manager")
    model_links = {"links_list": []}
    i = 0
    for filename in listdir(directory):
        f = path.join(directory, filename)
        # checking if it is a .html file
        if path.isfile(f) and path.splitext(f)[1] == '.html':
            model_links["links_list"].append(path.basename(path.splitext(f)[0]))

    return render(request, "manager/manager.html", model_links)


def error(request):
    return render(request, "manager/error.html", {"error_log": "Nie doszlo do zadnego bledu"})
    # sprawic by mi pycharm nie krzyczal ze tak nie mozna


def add_forms(request):
    return render(request, "manager/add_forms.html")


def leagues(request):
    all_leagues = League.objects.all()
    league_context = {"leagues": all_leagues}
    return render(request, "manager/leagues.html", league_context)


class Leagues(generic.ListView):
    template_name = 'manager/manager.html'

    def get_queryset(self):
        return League.objects.all()


class LeagueDetailView(generic.DetailView):
    model = League
    template_name = 'league_details.html'


def league_details(request, league_id):
    try:
        league = League.objects.get(id=league_id)
        return render(request, "manager/league_details.html", {"league": league})
    except ObjectDoesNotExist:
        return render(request, "manager/error.html", {"error_log": "Nie ma elementu o takim id"})
    except:
        return render(request, "manager/error.html", {"error_log": "brak pewnosci co do tego jaki to blad"})
        # sprawic by mi pycharm nie krzyczal ze tak nie mozna


def teams(request):
    all_teams = Team.objects.all()
    teams_context = {"teams": all_teams}
    return render(request, "manager/teams.html", teams_context)


def team_details(request, team_id):
    try:
        team = Team.objects.get(id=team_id)
        return render(request, "manager/team_details.html", {"team": team})
    except ObjectDoesNotExist:
        return render(request, "manager/error.html", {"error_log": "Nie ma elementu o takim id"})
    except:
        return render(request, "manager/error.html", {"error_log": "brak pewnosci co do tego jaki to blad"})


def matches(request):
    all_matches = Match.objects.all()
    matches_context = {"matches": all_matches}
    return render(request, "manager/matches.html", matches_context)


def match_details(request, match_id):
    try:
        match = Match.objects.get(id=match_id)
        return render(request, "manager/match_details.html", {"match": match})
    except ObjectDoesNotExist:
        return render(request, "manager/error.html", {"error_log": "Nie ma elementu o takim id"})
    except:
        return render(request, "manager/error.html", {"error_log": "brak pewnosci co do tego jaki to blad"})


def players(request):
    all_players = TeamPlayer.objects.all()
    players_context = {"players": all_players}
    return render(request, "manager/players.html", players_context)


def player_details(request, player_id):
    try:
        player = TeamPlayer.objects.get(id=player_id)
        return render(request, "manager/player_details.html", {"player": player})
    except ObjectDoesNotExist:
        return render(request, "manager/error.html", {"error_log": "Nie ma elementu o takim id"})
    except:
        return render(request, "manager/error.html", {"error_log": "brak pewnosci co do tego jaki to blad"})


def event_types(request):
    all_event_types = EventType.objects.all()
    event_types_context = {"event_types": all_event_types}
    return render(request, "manager/event_types.html", event_types_context)


def event_type_details(request, event_type_id):
    try:
        event_type = EventType.objects.get(id=event_type_id)
        return render(request, "manager/event_type_details.html", {"event_type": event_type})
    except ObjectDoesNotExist:
        return render(request, "manager/error.html", {"error_log": "Nie ma elementu o takim id"})
    except:
        return render(request, "manager/error.html", {"error_log": "brak pewnosci co do tego jaki to blad"})


def events(request):
    all_events = Event.objects.all()
    events_context = {"events": all_events}
    return render(request, "manager/events.html", events_context)


def event_details(request, event_id):
    try:
        event = Event.objects.get(id=event_id)
        return render(request, "manager/event_details.html", {"event": event})
    except ObjectDoesNotExist:
        return render(request, "manager/error.html", {"error_log": "Nie ma elementu o takim id"})
    except:
        return render(request, "manager/error.html", {"error_log": "brak pewnosci co do tego jaki to blad"})



