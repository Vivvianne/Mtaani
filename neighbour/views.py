from django.shortcuts import render
from .models import Neighbourhood
from .forms import NeighbourhoodForm
from django.views.generic import CreateView


posts = [
    {
        'author': 'CoreyMS',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'August 28, 2018'
    }
]



def home(request):
     context = {
         'posts': posts
         }
     return render(request, 'neighbour/home.html', context)
 
 
class CreateNeighbourhoodView(CreateView):
        model = Neighbourhood
        form_class = NeighbourhoodForm
