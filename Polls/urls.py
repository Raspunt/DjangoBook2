from django.urls import path,include
from . views import *


urlpatterns = [
    path('',MainPage, name= "HomeUrl"),
    path('Book/<slug:BookSlug>',BookDetail, name = "DetailBook"),

]
