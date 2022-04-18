
from django import forms
from .models import Alerts, Neighbourhood

#update profile email and username
class CreateNeighbourhoodForm(forms.ModelForm):

    class Meta:
        model = Neighbourhood
        exclude = ['admin']

class CreateAlertForm(forms.ModelForm):

    class Meta:
        model = Alerts
        exclude = ['profile', 'neighbourhood']
