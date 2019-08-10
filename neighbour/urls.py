from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name= 'neighbour-home'),
    path('', views.about, name='neighbour-about'),
    path('business/', views.business, name='business'),
    # path('neighbourhood/', views.neighbourhood, name='neighbourhood'),
]