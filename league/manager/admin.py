from django.contrib import admin

# Register your models here.
from .models import League, Match

class LeagueManger(admin.ModelAdmin):
    list_display = ["name", "is_ended"]


admin.site.register(League, LeagueManger)
admin.site.register(Match)