
from django import forms
from .models import Neighbourhood

#update profile email and username
class CreateNeighbourhoodForm(forms.ModelForm):

    class Meta:
        model = Neighbourhood
        exclude = ['admin']

