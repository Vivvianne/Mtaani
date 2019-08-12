from django.test import TestCase
from django.contrib.auth.models import User
from .models import Business, Neighbourhood, Post


def setUp(self):
    self.user1= User(id=1,username='Tester',email='tester@gmail.com',password='testing321')
    self.user1.save()
    self.neighbourhood = Neighbourhood(id=1,name='sar',location='kibera')
    self.neibourhood.create_neigborhood()
    self.post = Post(title= 1,content='sar',author='tester')
    self.neibourhood.create_neigborhood()


def tearDown(self):
    Post.objects.all().delete()
    User.objects.all().delete()
    Neighbourhood.objects.all().delete()
    
    
def test_is_instance(self):
    self.assertTrue(isinstance(self.user1,User))
    self.assertTrue(isinstance(self.post,Post))
    self.assertTrue(isinstance(self.neiba,Neighbourhood))
    
    
def test_save_method(self):
    self.post.create_post()
    all_objects = Post.objects.all()
    self.assertTrue(len(all_objects)>0)
    
    
def test_save_method(self):
    self.neibourhood.create_neigborhood()
    all_objects = Neighbourhood.objects.all()
    self.assertTrue(len(all_objects)>0)
