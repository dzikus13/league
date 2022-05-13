from django.contrib import admin
from django.urls import path

from .views import leagues
from .views import manager


urlpatterns = [
    path("", manager),
    path("leagues", leagues)
]