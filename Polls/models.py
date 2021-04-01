from django.db import models
from mptt.models import MPTTModel ,TreeForeignKey , TreeManyToManyField
from django.contrib.auth.models import User

class Genre(MPTTModel):
    title = models.CharField(max_length = 300)
    slug = models.SlugField(null=True , blank=True , max_length = 50)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    def __str__(self):
        return str(self.title)
    



class Comments(models.Model):
    name = models.ForeignKey(User,on_delete=models.CASCADE,blank = True, null= True)
    text = models.TextField(blank = True,db_index = True)


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


class Rating(models.Model):
    title = models.CharField(max_length=100)
    stars = models.IntegerField()


    def __str__(self):
        return str(self.title)
    
    


class Book(models.Model):
    title = models.CharField(max_length = 300)
    Author = models.ManyToManyField(Author,blank = True)
    description = models.TextField(blank = True,db_index = True)
    slug = models.SlugField(max_length = 150,unique= True)
    image  = models.ImageField(blank=True)
    comments = models.ManyToManyField(Comments,blank = True)
    rating = models.ForeignKey(Rating, on_delete = models.CASCADE)
    genreTree = TreeManyToManyField(Genre,related_name='books')



    def __str__(self):
        return str(self.title)



