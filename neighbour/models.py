from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


NEIGHBOURHOOD_CHOICES = (
    ('Kilimani','KILIMANI'),
    ('jamuhuri', 'JAMUHURI'),
    ('kibera','KIBERA'),
    ('lavington','LAVINGTON'),
    ('kileleshwa','KILELESHWA'),
    ('kawangware','KAWANGWARE'),
)


class Neighbourhood(models.Model):
    name = models.CharField(max_length=50, choices=NEIGHBOURHOOD_CHOICES, default='kilimani')
    location = models.CharField(max_length=30,unique=True)
    population = models.IntegerField()
    
    def __str__(self):
         return self.name
    
    
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE )
    business_email = models.EmailField() 
    
    
    def __str__(self):
        return self.title


class Business(models.Model):
    business_name = models.CharField(max_length=100)
    business_email = models.CharField(max_length=30)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE )
    business_email = models.EmailField()
    
    def __str__(self):
        return self.business_name
    
    

    
