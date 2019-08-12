from django.shortcuts import render, redirect, get_object_or_404
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
            post = form.save(commit=False)
            post.author = request.user
            
            post.save()
            return redirect('neighbour-home')
    else:
        form = PostCreateForm()
        
    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.neighbourhood_id = self.request.neighbourhood
        return super().form_valid(form)
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
    
    
class UserPostListView(ListView):
    model = Post
    template_name = 'upload/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 3
    
    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

class CreateNeighbourhoodView(CreateView):
        model = Neighbourhood
        form_class = NeighbourhoodForm
        success_url = 'neighbour/success.html'
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
