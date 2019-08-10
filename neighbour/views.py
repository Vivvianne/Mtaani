from django.shortcuts import render, redirect
from .models import Neighbourhood, Post
from django.contrib import messages
from .forms import NeighbourhoodForm, BusinessForm, NeighbourhoodUpdateForm, BusinessUpdateForm
from django.views.generic import CreateView, ListView



def home(request):
     context = {
         'posts': Post.objects.all()
         }
     return render(request, 'neighbour/home.html', context)
 
def neighbourhood(request):
    context = {
         'neighbourhoods': Neighbourhood.objects.all()
         }
    return render(request, 'neighbour/neighbourhood.html', context)
 
class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  
    context_object_name = 'posts'
    ordering = ['-date_posted']

 
class CreateNeighbourhoodView(CreateView):
        model = Neighbourhood
        form_class = NeighbourhoodForm
        
        
def business(request):
    if request.method == 'POST':
        
        b_form = BusinessUpdateForm(instance=request.business)
        if b_form.is_valid():
            b_form.save()
            messages.success(request, f'Your business has been updated!')
            return redirect('business')
        
    else:
        b_form = BusinessUpdateForm(instance=request.business)
        
    context = {
        'b_form': b_form
    }
    return render(request, 'neighbour/business.html', context)
        
        
def about(request):
    return render(request, 'neighbour/about.html', {'title': 'About'})
