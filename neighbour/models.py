from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Neighbourhood(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=30,unique=True)
    population = models.IntegerField()
    
    
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE )
    business_email = models.EmailField() 


class Business(models.Model):
    business_name = models.CharField(max_length=100)
    business_email = models.CharField(max_length=30)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE )
    business_email = models.EmailField()
    
    

    
