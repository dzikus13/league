from django.contrib import admin

# Register your models here.
from .models import League

class LeagueManager(admin.ModelAdmin):
    list_display = ["name", "ended"]


admin.site.register(League, LeagueManager)
