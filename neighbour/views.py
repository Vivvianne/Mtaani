from django.shortcuts import render
from .models import Neighbourhood, Post
from .forms import NeighbourhoodForm, BusinessForm, NeighbourhoodUpdateForm, BusinessUpdateForm
from django.views.generic import CreateView



def home(request):
     context = {
         'posts': Post.objects.all()
         }
     return render(request, 'neighbour/home.html', context)
 
 
class CreateNeighbourhoodView(CreateView):
        model = Neighbourhood
        form_class = NeighbourhoodForm
        
        
def business(request):
    b_form = BusinessUpdateForm()
    context = {
        'b_form': b_form
    }
    return render(request, 'neighbour/business.html', context)
        
        
def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
