from django.contrib import admin

# Register your models here.
from .models import League

class LeagueManger(admin.ModelAdmin):
    list_display = ["name"]

admin.site.register(League, LeagueManger)