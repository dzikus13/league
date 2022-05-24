from django.shortcuts import render
# from django.shortcuts import HttpResponse
# ^ probowalem uzyc by bezposrednio wyswietlic html

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

from django.shortcuts import render


def handler404(request, exception, template_name="404.html"):
    response = render_to_response(template_name)
    response.status_code = 404
    return response

def handler500(request, *args, **argv):
    return render(request, '500.html', status=500)