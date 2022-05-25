from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth import login as django_login
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import logout as django_logout

from os import path, listdir
from pathlib import Path
from .forms import NewUserForm
from .models import League, Match, Team, TeamPlayer, Event, EventType
BASE_DIR = Path(__file__).resolve().parent

# Create your views here.


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


def add_event(request):
    return render(request, "manager/add_event.html")


def add_league(request):
    return render(request, "manager/add_league.html")


def add_match(request):
    return render(request, "manager/add_match.html")


def add_player(request):
    return render(request, "manager/add_player.html")


def add_player_stats(request):
    return render(request, "manager/add_player_stats.html")


def add_team(request):
    return render(request, "manager/add_team.html")


def register(request):
    if request.method == "POST":
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        myuser = User.objects.create_user(username, password2, password1)

        myuser.save()

        messages.success(request, "Your Account has been successfully created.")

        return redirect("login")

    return render(request, "manager/register.html")


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']

        user = authenticate(username=username, password=password1)

        if user is not None:
            django_login(request, user)
            return render(request, "manager/logged.html")

        else:
            return redirect('login')

    return render(request, "manager/login.html")


def logout(request):
    django_logout(request)
    return render('/base')


def registered(request):
    if request.method == "POST":
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        myuser = User.objects.create_user(username, password2, password1)

        myuser.save()

        messages.success(request, "Your Account has been successfully created.")

        return redirect("login")

    return render(request, "manager/registered.html")


def logged(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']

        user = authenticate(username=username, password=password1)

        if user is not None:
            django_login(request, user)
            return render(request, "manager/logged.html")

        else:
            return redirect('login')

    return render(request, "manager/logged.html")


def logged_out(request):
    django_logout(request)
    return render(request, "manager/logged_out.html")


def leagues(request):
    all_leagues = League.objects.all()
    league_context = {"leagues": all_leagues}
    return render(request, "manager/leagues.html", league_context)


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
