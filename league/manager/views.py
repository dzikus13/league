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

from .models import League

def base(request):
    return render(request, "manager/base.html")

def leagues(request):
    all_leagues = League.objects.all()
    league_context = {"leagues": all_leagues}
    return render(request, "manager/leagues.html", league_context)


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


def league_details(request, league_id):
    try:
        league = League.objects.get(id=league_id)
        return render(request, "manager/league_details.html", {"league": league})
    except ObjectDoesNotExist:
        return render(request, "manager/error.html", {"error_log": "Nie ma elementu o takim id"})
    except:
        return render(request, "manager/error.html", {"error_log": "brak pewnosci co do tego jaki to blad"})
        # sprawic by mi pycharm nie krzyczal ze tak nie mozna


def error(request):
    return render(request, "manager/error.html", {"error_log": "Nie doszlo do zadnego bledu"})
    # sprawic by mi pycharm nie krzyczal ze tak nie mozna


def add_forms(request):
    return render(request, "manager/add_forms.html")
