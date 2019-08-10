from django.shortcuts import render
from .models import Neighbourhood, Post
from .forms import NeighbourhoodForm
from django.views.generic import CreateView


def home(request):
     context = {
         'posts': Post.objects.all()
         }
     return render(request, 'neighbour/home.html', context)
 
 
class CreateNeighbourhoodView(CreateView):
        model = Neighbourhood
        form_class = NeighbourhoodForm
        
        
def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
