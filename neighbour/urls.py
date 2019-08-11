from django.urls import path
from . import views
from django.conf import settings
from .views import PostListView, PostUpdateView, PostDeleteView, PostDetailView


urlpatterns = [
    path('home/', PostListView.as_view() , name= 'neighbour-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', views.post_save, name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('', views.about, name='neighbour-about'),
    path('business/', views.business, name='business'),
    path('neighbourhood/', views.neighbourhood, name='neighbourhood'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    
]

    