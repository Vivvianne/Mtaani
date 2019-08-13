from django.shortcuts import render, redirect, get_object_or_404
from .models import Neighbourhood, Post, Business
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import BusinessForm, PostCreateForm,  BusinessUpdateForm
# from .forms import NeighbourhoodForm, BusinessForm, PostCreateForm, NeighbourhoodUpdateForm,  BusinessUpdateForm
from django.views.generic import CreateView, ListView, DetailView, CreateView, UpdateView, DeleteView



def home(request):
     context = {
         'posts': Post.objects.all()
         }
     return render(request, 'neighbour/home.html', context)
 
def neighbourhood(request, neighbourhood):
    context = {
         'neighbourhood': Neighbourhood.objects.all()
         }
    return render(request, 'neighbour/neighbourhood.html', context)

 
class PostListView(ListView):
    model = Post
    template_name = 'neighbour/home.html'  
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 4
    
    
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
    template_name = 'neighbour/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 3
    
    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')
    

# class CreateNeighbourhoodView(CreateView):
#         model = Neighbourhood
#         form_class = NeighbourhoodForm
#         success_url = 'neighbour/success.html'
#         context_object_name = 'neighbourhood'
#         template_name = 'neighbour/neighbourhood.html'
        
        
def business_save(request):
    if request.method =='POST':
        form = BusinessForm(request.POST, request.FILES)
        if form.is_valid():
            business = form.save(commit=False)
            business.user = request.user
            
            business.save()
            return redirect('business')
    else:
        form = BusinessForm()
        
    # def form_valid(self, form):
    #     form.instance.author = self.request.user
    #     form.instance.neighbourhood_id = self.request.neighbourhood
    #     return super().form_valid(form)
    return render(request,'neighbour/business_form.html',{'form':form})
        
        
def business(request):
    if request.method == 'POST':
        
        b_form = BusinessUpdateForm()
        if b_form.is_valid():
            b_form.save()
            messages.success(request, f'Your business has been updated!')
            return redirect('business')
        
    else:
        b_form = BusinessUpdateForm()
        
    context = {
        'b_form': b_form
    }
    return render(request, 'neighbour/business.html', context)

class BusinessUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['business_name', 'business_email']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == business.bisiness_name:
            return True
        return False
    
    
    
class BusinessListView(ListView):
    model = Business
    template_name = 'neighbour/business.html'  
    context_object_name = 'businesses'
    # ordering = ['-date_posted']
    paginate_by = 4
    
    
    
class BusinessDetailView(DetailView):
    model = Business
    template_name ='neighbourhood/business_detail.html'
        
        
def about(request):
    return render(request, 'neighbour/about.html', {'title': 'About'})

def emergency(request):
    return render(request, 'neighbour/emergency.html', {'title': 'Emergency'})


def search_results(request):
    
    if 'business' in request.GET and request.GET["business"]:
        search_term = request.GET.get("business")
        searched_businesses = Business.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'neighbour/search.html',{"message":message,"businesses": searched_businesses})

    else:
        message = "You haven't searched for any term"
        return render(request, 'neighbour/search.html',{"message":message})