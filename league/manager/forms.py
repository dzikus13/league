from django.forms import ModelForm
from .models import League, Team, TeamPlayer, Event, Match


class LeagueForm(ModelForm):
    class Meta:
        model = League
        fields = '__all__'


class TeamForm(ModelForm):
    class Meta:
        model = Team
        fields = '__all__'


class TeamPlayerForm(ModelForm):
    class Meta:
        model = TeamPlayer
        fields = '__all__'


class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = '__all__'


class MatchForm(ModelForm):
    class Meta:
        model = Match
        fields = '__all__'
