from django import forms
from .models import Neighbourhood
from django.contrib.auth.models import User



class NeighbourhoodForm(forms.ModelForm):
    class Meta:
        model = Neighbourhood
        fields = ['name']