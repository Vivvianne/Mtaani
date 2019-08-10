from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Neighbourhood
from .models import Business
from django.contrib.auth.models import User
from .models import Post



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
        
        
class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','content']
        exlude =  ['author', 'neighbourhood','date_posted']