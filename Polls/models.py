from django.db import models
from mptt.models import MPTTModel ,TreeForeignKey , TreeManyToManyField
from django.contrib.auth.models import User
from users.models import UserProfile

from django.urls import reverse

class Genre(MPTTModel):
    title = models.CharField(max_length = 300)
    slug = models.SlugField(null=True , blank=True , max_length = 50)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    def __str__(self):
        return str(self.title)
    




class Rewiew(models.Model):
    title = models.CharField(max_length=100)
    stars = models.IntegerField()



    def __str__(self):
        return str(self.title) + " " + str(self.stars)
    



class Comments(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE,blank = True, null= True)
    name = models.ForeignKey(UserProfile,on_delete=models.CASCADE,blank = True, null= True)
    text = models.TextField(blank = True,db_index = True,max_length=1000)




    def __str__(self):
        return str(self.name)




class Author(models.Model):
    Name = models.CharField(max_length = 300)
    biog =  models.TextField(blank = True,db_index = True)
    slug = models.SlugField(null=True , blank=True , max_length = 50)
    FaceImg = models.ImageField(blank = True)
    DateBirth = models.DateField(blank = True)

    def __str__(self):
        return str(self.Name)


    


class Book(models.Model):
    title = models.CharField(max_length = 300)
    Author = models.ManyToManyField(Author,blank = True)
    description = models.TextField(blank = True,db_index = True)
    slug = models.SlugField(max_length = 150,unique= True)
    image  = models.ImageField(blank=True)
    comments = models.ManyToManyField(Comments,blank = True)
    Rewiew = models.ForeignKey(Rewiew, on_delete = models.CASCADE)
    genreTree = TreeManyToManyField(Genre,related_name='books')
    like = models.ManyToManyField(User,blank=True,related_name='likes')

    




    def __str__(self):
        return str(self.title)



