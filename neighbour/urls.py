from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name= 'neighbour-home'),
    path('about/', views.about, name='blog-about'),
    path('business/', views.business, name='business'),
    path('neighbourhood/', views.neighbourhood, name='neighbourhood'),
]