from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth import login as django_login
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import logout as django_logout

from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import LeagueForm, MatchForm, TeamForm, TeamPlayerForm, EventForm

from os import path, listdir
from pathlib import Path
from django.views import generic
from .models import League, Match, Team, TeamPlayer, Event, EventType
BASE_DIR = Path(__file__).resolve().parent

# Create your views here.


def main(request):
    all_leagues = League.objects.all()
    all_matches = Match.objects.all()
    all_context = {"leagues": all_leagues, "matches": all_matches}
    return render(request, "manager/main.html", all_context)


def view(request):
    all_leagues = League.objects.all()
    all_matches = Match.objects.all()
    all_events = Event.objects.all()
    all_teams = Team.objects.all()
    all_context = {"leagues": all_leagues, "matches": all_matches, "events": all_events, "teams": all_teams}
    return render(request, "manager/view.html", all_context)


def base(request):
    return render(request, "manager/base.html")


def events(request):
    return render(request, "manager/events.html")


def event_details(request):
    return render(request, "manager/event_details.html")


def manager(request):
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


def user_profile(request):
    return render(request, "manager/user_profile.html")


def error(request):
    return render(request, "manager/error.html", {"error_log": "Nie doszlo do zadnego bledu"})
    # sprawic by mi pycharm nie krzyczal ze tak nie mozna


def add_forms(request):
    return render(request, "manager/add_forms.html")


def add_league(request):
    form = LeagueForm()
    if request.method == 'POST':
        form = LeagueForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/leagues')
    context = {'form': form}
    return render(request, 'manager/add_league.html', context)


def add_match(request):
    form = MatchForm()
    if request.method == 'POST':
        form = MatchForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/matches')
    context = {'form': form}
    return render(request, 'manager/add_match.html', context)


def add_player(request):
    form = TeamPlayerForm()
    if request.method == 'POST':
        form = TeamPlayerForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/players')
    context = {'form': form}
    return render(request, 'manager/add_player.html', context)


def add_team(request):
    form = TeamForm()
    if request.method == 'POST':
        form = TeamForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/teams')
    context = {'form': form}
    return render(request, 'manager/add_team.html', context)


def add_event(request):
    form = EventForm()
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_event')
    context = {'form': form}
    return render(request, 'manager/add_event.html', context)


def register(request):
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
        email = request.POST['email']
        password1 = request.POST['password1']
        myuser = User.objects.create_user(username, email, password1)
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