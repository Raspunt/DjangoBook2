from django.db import models
from django.contrib.auth.models import User
from Polls.models import *


class UserProfile(models.Model):
    name = models.ForeignKey(User,on_delete=models.CASCADE)
    desc = models.TextField(max_length=1000,blank=True, null=True)
    rating = models.FloatField(blank=True,null=True)
    img = models.ImageField(blank=True)

    def __str__(self):
        return str(self.name)
