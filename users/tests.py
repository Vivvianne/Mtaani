from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile


class ProfileTestClass(TestCase):
    def setUp(self):
        self.test_profile = Profile(title=list('Beautiful butterflies'))
        self.test_profile.save_profile()

       

    def tearDown(self):
        Profile.objects.all().delete()