from django.contrib import admin
from django.contrib.auth.models import User
from .models import Neighbourhood, Post, Business

admin.site.register(Neighbourhood)
admin.site.register(Post)
admin.site.register(Business)
