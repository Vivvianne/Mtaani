from django.shortcuts import render, redirect
from .models import Neighbourhood, Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from .forms import NeighbourhoodForm, BusinessForm, PostCreateForm, NeighbourhoodUpdateForm, BusinessUpdateForm
from django.views.generic import CreateView, ListView, DetailView, CreateView, UpdateView, DeleteView



def home(request):
     context = {
         'posts': Post.objects.all()
         }
     return render(request, 'neighbour/home.html', context)
 
def neighbourhood(request):
    context = {
         'neighbourhood': Neighbourhood.objects.all()
         }
    return render(request, 'neighbour/neighbourhood.html', context)

 
class PostListView(ListView):
    model = Post
    template_name = 'neighbour/home.html'  
    context_object_name = 'posts'
    ordering = ['-date_posted']
    
    
class PostDetailView(DetailView):
    model = Post
    

    
    
def post_save(request):
    if request.method =='POST':
        form = PostCreateForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.author = request.user
            
            image.save()
            return redirect('neighbour-home')
    else:
        form = PostCreateForm()
    return render(request,'neighbour/post_form.html',{'form':form})
    
    
    
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class CreateNeighbourhoodView(CreateView):
        model = Neighbourhood
        form_class = NeighbourhoodForm
        context_object_name = 'neighbourhood'
        template_name = 'neighbour/neighbourhood.html'
        
        
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
