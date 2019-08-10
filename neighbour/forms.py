from django import forms
from .models import Neighbourhood
from .models import Business
from django.contrib.auth.models import User



class NeighbourhoodForm(forms.ModelForm):
    class Meta:
        model = Neighbourhood
        fields = ['name', 'location', 'population']
        
class NeighbourhoodUpdateForm(forms.ModelForm):
    class Meta:
        model = Neighbourhood
        fields = ['name', 'location','population']
        
        
        
class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        fields = ['business_name', 'business_email']
        
class BusinessUpdateForm(forms.ModelForm):
    class Meta:
        model = Business
        fields = ['business_name', 'business_email']