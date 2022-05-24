from django.shortcuts import render
from django.shortcuts import HttpResponse


from os import path, listdir
from pathlib import Path

# Create your views here.

from .models import League


def leagues(request):
    all_leagues = League.objects.all()
    return render(request, "manager/leagues.html", {"leagues": all_leagues})

def manager(request):
    # linki
    all_views_context = {}
    directory = 'manager'
    for filename in listdir("manager"):
        f = path.join(directory, filename)
        # checking if it is a file
        if path.isfile(f):
            print(f)

    return render(request, "manager/manager.html", all_views_context)

def league_details(request, league_id):
    league = League.objects.get(id=league_id)
    return render(request, "manager/league_details.html", {"league": league})


def error_400(request, exception):
    return render(request, 'manager/400.html', status=400)


def error_403(request, exception):
    return render(request, 'manager/403.html', status=403)


def error_404(request, exception):
    return render(request, 'manager/404.html', status=404)


def error_500(request, *args, **argv):
    return render(request, 'manager/500.html', status=500)
