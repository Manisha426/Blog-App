from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class User_Profile(models.Model):
        user = models.OneToOneField(User, related_name= 'User_profile', on_delete=models.CASCADE)
        profile_pic =  models.ImageField(upload_to = 'profile_pics')
