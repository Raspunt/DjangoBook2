from django.urls import path,include, re_path
from . views import *


urlpatterns = [
    path('',MainPage,name ="PureHomeUrl"),
    path('page/<int:pageId>/',MainPage, name= "HomeUrlWithPage"),
    path('Book/<slug:BookSlug>',BookDetail, name = "DetailBook"),
    path('Author/<slug:AuthorSlug>',AuthorDetail, name = "DetailAuthor"),
    path('Authors/',AuthorsAll, name = "AllAuthorsUrl")

]
