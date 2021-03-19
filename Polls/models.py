from django.db import models
from mptt.models import MPTTModel ,TreeForeignKey , TreeManyToManyField

class Genre(MPTTModel):
    title = models.CharField(max_length = 300)
    slug = models.SlugField(null=True , blank=True , max_length = 50)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    def __str__(self):
        return self.title
    



class Comments(models.Model):
    name = models.CharField(max_length = 100)
    text = models.TextField(blank = True,db_index = True)




class Author(models.Model):
    Name = models.CharField(max_length = 300)
    biog =  models.TextField(blank = True,db_index = True)
    FaceImg = models.ImageField(blank = True)
    DateBirth = models.DateField(blank = True)

    def __str__(self):
        return self.Name


class Book(models.Model):
    title = models.CharField(max_length = 300)
    Author = models.ManyToManyField(Author,blank = True)
    description = models.TextField(blank = True,db_index = True)
    slug = models.SlugField(max_length = 150,unique= True)
    image  = models.ImageField(blank=True)
    comments = models.ManyToManyField(Comments,blank = True)
    genreTree = TreeManyToManyField(Genre,related_name='books')



    def __str__(self):
        return self.title





