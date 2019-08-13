from django.urls import path
from . import views
from django.conf import settings
from .views import PostListView, PostUpdateView, PostDeleteView, PostDetailView,UserPostListView, BusinessUpdateView,BusinessDetailView, BusinessListView


urlpatterns = [
    path('home/', PostListView.as_view() , name= 'neighbour-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', views.post_save, name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('', views.about, name='neighbour-about'),
    path('business/new/', views.business_save, name='business-form'),
    path('business/<int:pk>/update/', BusinessUpdateView.as_view(), name='business-update'),
    path('business/', BusinessListView.as_view(), name='business'),
    path('user/<str:busines_name>', BusinessListView.as_view(), name='user-business'),
    path('business/<int:pk>/', BusinessDetailView.as_view(), name='business-detail'),
    path('neighbourhood/new/', views.business, name='neighbourhood-form'),
    path('neighbourhood/<neighbourhood>', views.neighbourhood, name='neighbourhood'),
    path('emergency/', views.emergency , name= 'emergency'),
    
    
]

    