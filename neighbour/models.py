from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from users.models import Neighbourhood

NEIGHBOURHOOD_CHOICES = (
    ('Kilimani','KILIMANI'),
    ('jamuhuri', 'JAMUHURI'),
    ('kibera','KIBERA'),
    ('lavington','LAVINGTON'),
    ('kileleshwa','KILELESHWA'),
    ('kawangware','KAWANGWARE'),
)


    
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE, null=True,)
    
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk':self.pk})

class Business(models.Model):
    business_name = models.CharField(max_length=100)
    business_email = models.CharField(max_length=30)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE, null=True )
    
    @classmethod
    def search_by_business_name(cls,search_term):
        business = cls.objects.filter(business_name__icontains=search_term)
        return business
    
    def __str__(self):
        return self.business_name
    
    

    
