from django.shortcuts import render

# Create your views here.

from .models import League


def leagues(request):
    all_leagues = League.objects.all()
    return render(request, "manager/leagues.html", {"leagues": all_leagues})

def league_details(request, league_id):
    league = League.objects.get(id=league_id)
    return render(request, "manager/league_details.html", {"league": league})
