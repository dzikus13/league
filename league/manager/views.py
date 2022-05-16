from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# Create your views here.

from .models import League


def leagues(request):
    all_leagues = League.objects.all()
    return render(request, "manager/leagues.html", {"leagues": all_leagues})

def league_details(request, league_id):
    league = League.objects.get(id=league_id)
    return render(request, "manager/league_details.html", {"league": league})


class LeagueAddView(CreateView):
    model = League
    fields = ["name", "max_number_of_teams"]
    success_url = reverse_lazy("league_list")


class LeagueEditView(UpdateView):
    model = League
    fields = ["name", "max_number_of_teams"]
    success_url = reverse_lazy("league_list")
