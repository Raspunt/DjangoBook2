from django.urls import path,include, re_path
from . views import *


urlpatterns = [
    path('',MainPage,name ="PureHomeUrl"),
    path('page/<int:pageId>/',MainPage, name= "HomeUrlWithPage"),
    path('Book/<slug:BookSlug>',BookDetail, name = "DetailBook"),
    path('Author/<slug:AuthorSlug>',AuthorDetail, name = "DetailAuthor"),
    path("Book/<slug:BookSlug>/like/",LikeButton,name = "lileButtonUrl"),

    #  Admin Url

    path("CrudActions/", CrudActions, name = "CrudActionsUrl"),
    #  Book
    path("CreateBook/",CreateBookView.as_view(),name= "createBookUrl"),
    path("UpdateBook/<int:pk>/",UpdateBook.as_view(),name= "UpdateBookUrl"),
    path("deleteBook/<slug:slugBook>/",DeleteBook,name = "DeleteBookUrl"),
    # Author
    path("CreateAuthor/",CreateAuthorView.as_view(), name = "CreateAuthorUrl"),
    path("UpdateAuthor/",UpdateAuthorView.as_view(), name = "UpdateAuthorUrl"),
    path("DeleteAuthor/<slug:slugAuthor>/",DeleteAuthor)

]
