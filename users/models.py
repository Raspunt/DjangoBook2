from django.db import models
from django.contrib.auth.models import User
from Polls.models import *


class UserProfile(models.Model):
    name = models.ForeignKey(User,on_delete=models.CASCADE)
    desc = models.CharField(max_length=300)
    rating = models.FloatField()
    img = models.ImageField(blank=True)

    def __str__(self):
        return str(self.name)
